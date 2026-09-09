import React, { useEffect, useRef, useState, useCallback } from 'react';
import Hls from 'hls.js';
import { 
  Play, 
  Pause, 
  Volume2, 
  VolumeX, 
  Maximize, 
  Minimize, 
  RefreshCw, 
  Tv, 
  Star, 
  Activity, 
  AlertCircle,
  X,
  Radio,
  Video,
  PlayCircle,
  Calendar,
  Clock,
  ShieldCheck,
  Zap
} from 'lucide-react';
import { getProxiedStreamUrl, checkStreamHealth, fetchReplayStreams } from '../services/api';

export default function VideoPlayer({ 
  streamItem, 
  onClose, 
  isFavorite = false, 
  onToggleFavorite, 
  onSwitchToMultiView 
}) {
  const videoRef = useRef(null);
  const hlsRef = useRef(null);
  const containerRef = useRef(null);

  const [isPlaying, setIsPlaying] = useState(true);
  const [isMuted, setIsMuted] = useState(false);
  const [volume, setVolume] = useState(1);
  const [isFullscreen, setIsFullscreen] = useState(false);
  
  const [selectedServerIndex, setSelectedServerIndex] = useState(0);
  const [useProxy, setUseProxy] = useState(false);
  const [streamError, setStreamError] = useState(null);
  const [isBuffering, setIsBuffering] = useState(false);
  const [autoFailoverMessage, setAutoFailoverMessage] = useState('');
  const [failedServerIndices, setFailedServerIndices] = useState(new Set());
  const [serverHealthMap, setServerHealthMap] = useState({});
  const [dynamicReplayStreams, setDynamicReplayStreams] = useState([]);
  const [isResolvingReplay, setIsResolvingReplay] = useState(false);
  const [isHelperDismissed, setIsHelperDismissed] = useState(false);
  const [neverShowHelper, setNeverShowHelper] = useState(() => {
    try {
      return localStorage.getItem('sportx_hide_server_helper') === 'true';
    } catch {
      return false;
    }
  });

  const handleNeverShowHelperAgain = () => {
    try {
      localStorage.setItem('sportx_hide_server_helper', 'true');
    } catch (e) {}
    setNeverShowHelper(true);
  };

  const matchData = streamItem?.data || streamItem;
  const isMatch = streamItem?.type === 'match' || !streamItem?.type;

  useEffect(() => {
    setSelectedServerIndex(streamItem?.data?.defaultServerIndex || 0);
    setUseProxy(false);
    setStreamError(null);
    setIsBuffering(false);
    setAutoFailoverMessage('');
    setFailedServerIndices(new Set());
    setDynamicReplayStreams([]);

    const home = matchData?.home_team?.name;
    const away = matchData?.away_team?.name;
    const isFinishedMatch = isMatch && (
      matchData?.status === 'FINISHED' || 
      matchData?.status === 'FT' || 
      matchData?.is_recent ||
      Boolean(matchData?.duration) ||
      matchData?.category === 'recent'
    );

    // If it's a finished match/replay, dynamically resolve the exact match's YouTube & Dailymotion highlights
    if (isFinishedMatch && home && away) {
      setIsResolvingReplay(true);
      fetchReplayStreams(home, away, matchData?.competition || matchData?.league)
        .then(res => {
          if (res?.servers && res.servers.length > 0) {
            setDynamicReplayStreams(res.servers);
          }
        })
        .catch(err => console.warn('Replay resolution error:', err))
        .finally(() => setIsResolvingReplay(false));
    }
  }, [matchData?.id, matchData?.home_team?.name, matchData?.away_team?.name]);

  const getStreamsList = () => {
    if (!streamItem) return [];
    if (dynamicReplayStreams.length > 0) {
      return dynamicReplayStreams;
    }
    if (matchData?.streams?.length > 0) {
      return matchData.streams;
    }
    if (streamItem?.streams?.length > 0) {
      return streamItem.streams;
    }
    const mainStream = {
      id: 'main-srv',
      label: `Server 1: ${matchData?.name || matchData?.title || 'Football HD'}`,
      network: matchData?.country || matchData?.competition || 'Global Feed',
      quality: matchData?.quality || '1080p HD',
      url: matchData?.stream_url || matchData?.url || 'https://epiembeds.online/embed/sky-sports-premier-league',
      is_embed: matchData?.is_embed ?? !(matchData?.stream_url || matchData?.url || '').includes('.m3u8'),
      language: matchData?.language || 'English',
      coverage: 'Official Channel Stream',
      is_replay: false
    };
    const backups = (matchData?.backup_streams || []).map((bUrl, idx) => ({
      id: `backup-${idx + 1}`,
      label: `Server ${idx + 2}: Backup Feed`,
      network: 'Backup Server',
      quality: '1080p',
      url: bUrl,
      is_embed: !bUrl.includes('.m3u8'),
      language: matchData?.language || 'English',
      coverage: 'Backup Stream',
      is_replay: false
    }));
    return [mainStream, ...backups];
  };

  const streams = getStreamsList();
  const currentStream = streams[selectedServerIndex] || streams[0];
  const isFinished = isMatch && (
    matchData?.status === 'FINISHED' || 
    matchData?.status === 'FT' || 
    Boolean(matchData?.category) || 
    Boolean(matchData?.duration)
  );
  const isLive = isMatch && matchData?.status === 'LIVE';

  const isEmbedStream = currentStream?.is_embed || 
    (currentStream?.url && (
      currentStream.url.includes('/embed') || 
      currentStream.url.includes('youtube') || 
      currentStream.url.includes('youtu.be') || 
      !currentStream.url.includes('.m3u8')
    ));

  const activeStreamUrl = currentStream 
    ? (useProxy && !isEmbedStream ? getProxiedStreamUrl(currentStream.url) : currentStream.url)
    : '';

  // Background health probing for non-embed streams
  useEffect(() => {
    if (!streams.length) return;
    streams.forEach((s) => {
      if (!s.url || s.is_embed) return;
      checkStreamHealth(s.url)
        .then(health => {
          if (health) {
            setServerHealthMap(prev => ({
              ...prev,
              [s.id || s.url]: health
            }));
          }
        })
        .catch(() => {});
    });
  }, [streamItem?.data?.id]);

  // Automatic failover handler (finds next working server in rotation)
  const triggerAutoFailover = useCallback((currentIdx) => {
    if (!streams.length || streams.length <= 1) {
      setStreamError(`Broadcast feed interrupted. Please try another match or check back shortly.`);
      return;
    }

    setFailedServerIndices(prev => {
      const updated = new Set(prev).add(currentIdx);
      
      // Look for next server index that hasn't failed yet
      let nextIdx = (currentIdx + 1) % streams.length;
      let attempts = 0;
      while (updated.has(nextIdx) && attempts < streams.length) {
        nextIdx = (nextIdx + 1) % streams.length;
        attempts++;
      }

      // If all servers failed, reset failure memory and start from Server 1
      if (attempts >= streams.length) {
        setAutoFailoverMessage(`All servers attempted. Cycling back to Server 1...`);
        setTimeout(() => {
          setSelectedServerIndex(0);
          setFailedServerIndices(new Set());
          setStreamError(null);
          setTimeout(() => setAutoFailoverMessage(''), 3000);
        }, 1000);
        return updated;
      }

      const nextServer = streams[nextIdx];
      setAutoFailoverMessage(`Server ${currentIdx + 1} unavailable. Auto-switching to Server ${nextIdx + 1} (${nextServer.network || nextServer.label || 'Alternative Feed'})...`);
      
      setTimeout(() => {
        setSelectedServerIndex(nextIdx);
        setUseProxy(false);
        setStreamError(null);
        setTimeout(() => setAutoFailoverMessage(''), 4500);
      }, 800);

      return updated;
    });
  }, [streams]);

  // Listen for iframe postMessage error events (YouTube Iframe API & Dailymotion error events)
  useEffect(() => {
    if (!isEmbedStream) return;

    const handleWindowMessage = (event) => {
      try {
        let msg = event.data;
        if (typeof msg === 'string') {
          try {
            msg = JSON.parse(msg);
          } catch (err) {}
        }

        // 1. YouTube error event: event === 'onError' or info has error codes (100, 101, 150, 2, 5)
        const isYtError = 
          msg?.event === 'onError' || 
          msg?.info === 100 || 
          msg?.info === 101 || 
          msg?.info === 150 || 
          msg?.info === 2 || 
          msg?.info === 5;

        // 2. Dailymotion player errors
        const isDmError = msg?.event === 'error' || msg?.type === 'error';

        if (isYtError || isDmError) {
          console.warn('Embed player error detected, triggering auto-failover to next server:', msg);
          triggerAutoFailover(selectedServerIndex);
        }
      } catch (e) {}
    };

    window.addEventListener('message', handleWindowMessage);
    return () => window.removeEventListener('message', handleWindowMessage);
  }, [isEmbedStream, selectedServerIndex, triggerAutoFailover]);

  useEffect(() => {
    if (isEmbedStream) return;

    const video = videoRef.current;
    if (!video || !activeStreamUrl) return;

    setStreamError(null);
    setIsBuffering(true);

    if (hlsRef.current) {
      hlsRef.current.destroy();
      hlsRef.current = null;
    }

    if (Hls.isSupported()) {
      const hls = new Hls({
        enableWorker: true,
        lowLatencyMode: true,
        backBufferLength: 30,
        maxBufferLength: 15,
        liveSyncDurationCount: 3,
        xhrSetup: (xhr) => {
          xhr.withCredentials = false;
        }
      });
      hlsRef.current = hls;
      hls.loadSource(activeStreamUrl);
      hls.attachMedia(video);

      hls.on(Hls.Events.MANIFEST_PARSED, () => {
        setIsBuffering(false);
        video.play().catch(() => setIsPlaying(false));
      });

      hls.on(Hls.Events.ERROR, (event, data) => {
        if (data.fatal) {
          setIsBuffering(false);
          switch (data.type) {
            case Hls.ErrorTypes.NETWORK_ERROR:
              if (!useProxy) {
                setAutoFailoverMessage(`Direct stream connection blocked. Switching to Secure Proxy Relay...`);
                setUseProxy(true);
                setTimeout(() => setAutoFailoverMessage(''), 3000);
              } else {
                triggerAutoFailover(selectedServerIndex);
              }
              break;
            case Hls.ErrorTypes.MEDIA_ERROR:
              hls.recoverMediaError();
              break;
            default:
              hls.destroy();
              triggerAutoFailover(selectedServerIndex);
              break;
          }
        }
      });
    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
      video.src = activeStreamUrl;
      video.addEventListener('loadedmetadata', () => {
        setIsBuffering(false);
        video.play().catch(() => setIsPlaying(false));
      });
      video.onerror = () => {
        setIsBuffering(false);
        triggerAutoFailover(selectedServerIndex);
      };
    }

    return () => {
      if (hlsRef.current) {
        hlsRef.current.destroy();
        hlsRef.current = null;
      }
    };
  }, [activeStreamUrl, isEmbedStream, useProxy, selectedServerIndex, triggerAutoFailover]);

  const togglePlay = () => {
    if (!videoRef.current) return;
    if (isPlaying) {
      videoRef.current.pause();
      setIsPlaying(false);
    } else {
      videoRef.current.play();
      setIsPlaying(true);
    }
  };

  const toggleMute = () => {
    if (!videoRef.current) return;
    videoRef.current.muted = !isMuted;
    setIsMuted(!isMuted);
  };

  const toggleFullscreen = () => {
    if (!containerRef.current) return;
    if (!document.fullscreenElement) {
      containerRef.current.requestFullscreen().catch(err => console.error(err));
      setIsFullscreen(true);
    } else {
      document.exitFullscreen();
      setIsFullscreen(false);
    }
  };

  if (!streamItem) return null;

  const matchTitle = matchData?.title || (
    isMatch && matchData?.home_team?.name && matchData?.away_team?.name
      ? `${matchData.home_team.name} vs ${matchData.away_team.name}`
      : matchData?.name || 'Live Broadcast Feed'
  );

  const competitionLabel = matchData?.competition || matchData?.league || matchData?.country || 'Official Football Feed';
  const matchDateLabel = matchData?.date || matchData?.kickoff_date;

  return (
    <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/90 dark:border-slate-800 shadow-xl overflow-hidden p-4 sm:p-5 space-y-4 transition-colors">
      {/* Top Header Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-800 dark:text-slate-100 font-bold shrink-0 border border-slate-200 dark:border-slate-700">
            {isFinished ? (
              <Video className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
            ) : isMatch ? (
              <Tv className="w-5 h-5 text-slate-700 dark:text-slate-300" />
            ) : (
              <Radio className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
            )}
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm sm:text-base font-black text-slate-900 dark:text-slate-100 truncate max-w-md">
                {matchTitle}
              </h3>
              
              {isFinished ? (
                <span className="px-2.5 py-0.5 rounded-full bg-slate-900 dark:bg-slate-800 text-white text-[10px] font-black uppercase tracking-wider">
                  MATCH REPLAY & HIGHLIGHTS
                </span>
              ) : isLive ? (
                <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-red-100 dark:bg-red-950/60 text-red-700 dark:text-red-400 text-[10px] font-black uppercase tracking-wider border border-red-200 dark:border-red-800">
                  <span className="w-1.5 h-1.5 rounded-full bg-red-600 dark:bg-red-500 animate-pulse"></span>
                  LIVE
                </span>
              ) : (
                <span className="px-2 py-0.5 rounded-full bg-sky-100 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 text-[10px] font-black uppercase tracking-wider border border-sky-200 dark:border-sky-800">
                  SCHEDULED
                </span>
              )}
            </div>
            
            <p className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-2 mt-0.5">
              <span>{competitionLabel}</span>
              {matchDateLabel && (
                <>
                  <span>&bull;</span>
                  <span className="font-semibold text-slate-700 dark:text-slate-300">{matchDateLabel}</span>
                </>
              )}
            </p>
          </div>
        </div>

        {/* Right Tools */}
        <div className="flex items-center gap-2">
          {/* Proxy Relay Toggle Button */}
          {!isEmbedStream && (
            <button
              onClick={() => setUseProxy(!useProxy)}
              className={`px-2.5 py-1.5 rounded-xl border text-xs font-bold transition-colors cursor-pointer flex items-center gap-1.5 ${
                useProxy
                  ? 'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-300 dark:border-emerald-700 text-emerald-700 dark:text-emerald-300'
                  : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
              title={useProxy ? 'Proxy Relay Active (Bypassing CORS blocks)' : 'Click to enable Secure Backend Proxy Relay'}
            >
              <ShieldCheck className={`w-3.5 h-3.5 ${useProxy ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-400'}`} />
              <span className="hidden sm:inline">Proxy Relay</span>
              <span className={`w-1.5 h-1.5 rounded-full ${useProxy ? 'bg-emerald-500 animate-pulse' : 'bg-slate-400'}`}></span>
            </button>
          )}

          {onToggleFavorite && (
            <button
              onClick={() => onToggleFavorite(streamItem)}
              className={`p-2 rounded-xl border transition-colors cursor-pointer ${
                isFavorite 
                  ? 'bg-rose-50 dark:bg-rose-950/50 border-rose-200 dark:border-rose-800 text-rose-600 dark:text-rose-400' 
                  : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100'
              }`}
              title="Bookmark Feed"
            >
              <Star className={`w-4 h-4 ${isFavorite ? 'fill-rose-600 dark:fill-rose-400' : ''}`} />
            </button>
          )}

          {onSwitchToMultiView && (
            <button
              onClick={() => onSwitchToMultiView(streamItem)}
              className="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-bold border border-slate-200 dark:border-slate-700 transition-colors cursor-pointer"
              title="Watch in Dual Screen"
            >
              Dual Multi-View
            </button>
          )}

          {onClose && (
            <button
              onClick={onClose}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-rose-100 dark:hover:bg-rose-950 text-slate-600 dark:text-slate-400 hover:text-rose-700 dark:hover:text-rose-400 border border-slate-200 dark:border-slate-700 transition-colors cursor-pointer"
              title="Close Player"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Top Helper Banner: Doesn't work? Try switching to another server */}
      {streams.length > 1 && !isHelperDismissed && !neverShowHelper && (
        <div className="flex flex-wrap items-center justify-between gap-2.5 px-3.5 py-2.5 rounded-2xl bg-amber-500/10 dark:bg-amber-500/15 border border-amber-500/25 text-xs animate-in fade-in duration-200">
          <div className="flex items-center gap-2 text-amber-900 dark:text-amber-200">
            <AlertCircle className="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0" />
            <span className="font-semibold">
              Doesn't work or highlights buffering?
            </span>
            <span className="text-amber-700/90 dark:text-amber-300/80 hidden md:inline">
              Multiple official servers (YouTube, Dailymotion & TV Vault) available.
            </span>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => {
                const nextIdx = (selectedServerIndex + 1) % streams.length;
                setSelectedServerIndex(nextIdx);
                setAutoFailoverMessage(`Switched to Server ${nextIdx + 1} (${streams[nextIdx]?.network || streams[nextIdx]?.label || 'Next Feed'})`);
                setTimeout(() => setAutoFailoverMessage(''), 3500);
              }}
              className="flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs transition-all cursor-pointer shadow-xs hover:scale-[1.02] active:scale-[0.98]"
              title="Switch to next broadcast server"
            >
              <span>Try switching to another server &rarr;</span>
            </button>

            <button
              onClick={handleNeverShowHelperAgain}
              className="px-2 py-1 text-[11px] font-medium text-amber-800/80 hover:text-amber-950 dark:text-amber-300/70 dark:hover:text-amber-200 hover:underline transition-colors cursor-pointer"
              title="Never show this banner again"
            >
              Don't show again
            </button>

            <button
              onClick={() => setIsHelperDismissed(true)}
              className="p-1 rounded-lg hover:bg-amber-500/20 text-amber-800 dark:text-amber-300 transition-colors cursor-pointer"
              title="Dismiss banner"
              aria-label="Dismiss banner"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}

      {/* Video Cinema Container */}
      <div 
        ref={containerRef}
        className="relative aspect-video w-full rounded-2xl bg-black overflow-hidden shadow-2xl flex items-center justify-center group"
      >
        {/* Floating Auto-Failover Notification Banner */}
        {autoFailoverMessage && (
          <div className="absolute top-4 left-1/2 -translate-x-1/2 z-30 max-w-[90%] bg-slate-900/95 border border-emerald-500/50 backdrop-blur-md text-white px-4 py-2 rounded-2xl shadow-2xl flex items-center gap-2.5 text-xs font-bold">
            <RefreshCw className="w-4 h-4 text-emerald-400 animate-spin shrink-0" />
            <span className="text-slate-100">{autoFailoverMessage}</span>
          </div>
        )}

        {isEmbedStream ? (
          <iframe
            key={activeStreamUrl}
            src={activeStreamUrl.includes('youtube') && !activeStreamUrl.includes('enablejsapi=1')
              ? `${activeStreamUrl}${activeStreamUrl.includes('?') ? '&' : '?'}enablejsapi=1`
              : activeStreamUrl}
            title={matchTitle}
            className="w-full h-full border-0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowFullScreen
            onError={() => {
              console.warn('Iframe failed to load, triggering auto-failover');
              triggerAutoFailover(selectedServerIndex);
            }}
          />
        ) : (
          <>
            <video
              ref={videoRef}
              className="w-full h-full object-contain"
              playsInline
              autoPlay
              muted={isMuted}
            />

            {/* Buffering Indicator */}
            {isBuffering && (
              <div className="absolute inset-0 bg-black/60 flex items-center justify-center">
                <div className="w-12 h-12 rounded-full border-4 border-slate-700 border-t-emerald-500 animate-spin"></div>
              </div>
            )}

            {/* Error Overlay with Smart Failover Actions */}
            {streamError && (
              <div className="absolute inset-0 bg-slate-950/90 backdrop-blur-sm flex flex-col items-center justify-center p-6 text-center space-y-4 z-20">
                <div className="w-12 h-12 rounded-2xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center">
                  <AlertCircle className="w-6 h-6 text-rose-500" />
                </div>
                <div className="max-w-md">
                  <p className="text-sm font-bold text-white mb-1">Broadcast Feed Interrupted</p>
                  <p className="text-xs text-slate-300 leading-relaxed">{streamError}</p>
                </div>
                <div className="flex flex-wrap items-center justify-center gap-2 pt-1">
                  <button
                    onClick={() => {
                      setFailedServerIndices(new Set());
                      setSelectedServerIndex(0);
                      setStreamError(null);
                      setUseProxy(false);
                    }}
                    className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-colors cursor-pointer flex items-center gap-1.5 shadow-lg shadow-emerald-600/30"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    Retry from Server 1
                  </button>
                  <button
                    onClick={() => {
                      setStreamError(null);
                      setUseProxy(!useProxy);
                    }}
                    className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition-colors cursor-pointer flex items-center gap-1.5"
                  >
                    <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
                    {useProxy ? 'Try Direct Connection' : 'Retry with Proxy Relay'}
                  </button>
                  {streams.length > 1 && (
                    <button
                      onClick={() => {
                        setStreamError(null);
                        setSelectedServerIndex((prev) => (prev + 1) % streams.length);
                      }}
                      className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition-colors cursor-pointer"
                    >
                      Next Server
                    </button>
                  )}
                </div>
              </div>
            )}

            {/* Video Controls Overlay */}
            <div className="absolute bottom-0 left-0 right-0 p-3 bg-gradient-to-t from-black/80 via-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-between">
              <div className="flex items-center gap-3">
                <button onClick={togglePlay} className="text-white hover:text-emerald-400 p-1 cursor-pointer">
                  {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5" />}
                </button>
                <button onClick={toggleMute} className="text-white hover:text-emerald-400 p-1 cursor-pointer">
                  {isMuted ? <VolumeX className="w-5 h-5" /> : <Volume2 className="w-5 h-5" />}
                </button>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-[11px] font-bold text-slate-300">1080p Full HD</span>
                <button onClick={toggleFullscreen} className="text-white hover:text-emerald-400 p-1 cursor-pointer">
                  {isFullscreen ? <Minimize className="w-5 h-5" /> : <Maximize className="w-5 h-5" />}
                </button>
              </div>
            </div>
          </>
        )}
      </div>

      {/* Multi-Server / Replay Selector Bar */}
      <div className="space-y-2 pt-1">
        <div className="flex items-center justify-between">
          <span className="text-xs font-extrabold text-slate-700 dark:text-slate-200 uppercase tracking-wider flex items-center gap-1.5">
            {isFinished ? (
              <Video className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            ) : (
              <Tv className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            )}
            <span>{isFinished ? 'Select Official Highlights & Replay Feed:' : 'Select Live Broadcast Server:'}</span>
          </span>
          <span className="text-xs text-slate-500 dark:text-slate-400 font-medium flex items-center gap-1.5">
            {isResolvingReplay ? (
              <span className="text-emerald-500 animate-pulse text-xs font-bold flex items-center gap-1">
                <RefreshCw className="w-3 h-3 animate-spin" />
                <span>Locating match replay feeds...</span>
              </span>
            ) : (
              <span>{streams.length} Verified Feeds Available</span>
            )}
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
          {streams.map((srv, idx) => {
            const isSelected = selectedServerIndex === idx;
            const isFailed = failedServerIndices.has(idx);
            const health = serverHealthMap[srv.id || srv.url];

            return (
              <button
                key={srv.id || idx}
                onClick={() => {
                  setSelectedServerIndex(idx);
                  setStreamError(null);
                }}
                className={`p-3 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between ${
                  isSelected
                    ? 'bg-emerald-600 text-white border-emerald-600 shadow-md shadow-emerald-600/20 font-bold'
                    : isFailed
                    ? 'bg-rose-50/60 dark:bg-rose-950/20 text-slate-500 dark:text-slate-400 border-rose-200 dark:border-rose-900/40 hover:bg-rose-100/50'
                    : 'bg-slate-50 dark:bg-slate-800/80 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200 border-slate-200/90 dark:border-slate-700'
                }`}
              >
                <div className="flex items-center justify-between mb-1.5">
                  <div className="flex items-center gap-1.5">
                    {/* Health dot */}
                    <span 
                      className={`w-2 h-2 rounded-full shrink-0 ${
                        isSelected 
                          ? 'bg-white animate-pulse'
                          : isFailed
                          ? 'bg-rose-500'
                          : health?.is_working
                          ? 'bg-emerald-500'
                          : health?.is_working === false
                          ? 'bg-amber-500'
                          : 'bg-slate-400'
                      }`}
                    />
                    <span className={`text-[10px] uppercase font-black tracking-wider ${isSelected ? 'text-emerald-100' : 'text-slate-400 dark:text-slate-400'}`}>
                      {isFinished ? `Replay Feed ${idx + 1}` : `Server ${idx + 1}`}
                    </span>
                  </div>

                  <div className="flex items-center gap-1.5">
                    {health?.latency_ms && !isSelected && (
                      <span className="text-[10px] font-semibold text-emerald-600 dark:text-emerald-400">
                        {health.latency_ms}ms
                      </span>
                    )}
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-bold ${
                      isSelected 
                        ? 'bg-black/20 text-white' 
                        : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                    }`}>
                      {srv.quality || '1080p'}
                    </span>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold truncate pr-2">
                    {srv.label || srv.network || `Feed ${idx + 1}`}
                  </span>
                  {isFailed && !isSelected && (
                    <span className="text-[9px] font-black uppercase text-rose-600 dark:text-rose-400">
                      Failed
                    </span>
                  )}
                  {isSelected && (
                    <span className="text-[9px] font-black uppercase text-emerald-200 tracking-wider">
                      Active
                    </span>
                  )}
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
