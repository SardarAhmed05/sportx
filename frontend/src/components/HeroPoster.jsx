import React, { useState, useEffect, useCallback } from 'react';
import { 
  Play, 
  BarChart2, 
  Tv, 
  ChevronLeft, 
  ChevronRight, 
  Calendar, 
  Clock, 
  MapPin, 
  Trophy, 
  Video,
  PlayCircle
} from 'lucide-react';
import { handleLogoError } from '../utils/avatar';

export default function HeroPoster({ 
  matches = [], 
  onWatchMatch, 
  onOpenStats,
  sportName = 'Football'
}) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAutoPlaying, setIsAutoPlaying] = useState(true);

  // Filter top featured matches (prioritize LIVE first, then marquee UPCOMING, then recent FINISHED)
  const featuredMatches = matches.length > 0
    ? [...matches].sort((a, b) => {
        if (a.status === 'LIVE' && b.status !== 'LIVE') return -1;
        if (b.status === 'LIVE' && a.status !== 'LIVE') return 1;
        if (a.status === 'UPCOMING' && b.status === 'FINISHED') return -1;
        if (b.status === 'UPCOMING' && a.status === 'FINISHED') return 1;
        return (b.viewers_count || 0) - (a.viewers_count || 0);
      }).slice(0, 8)
    : [];

  useEffect(() => {
    if (!isAutoPlaying || featuredMatches.length <= 1) return;
    const timer = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % featuredMatches.length);
    }, 7000);
    return () => clearInterval(timer);
  }, [isAutoPlaying, featuredMatches.length]);

  if (featuredMatches.length === 0) return null;

  const currentMatch = featuredMatches[currentIndex] || featuredMatches[0];
  const isLive = currentMatch.status === 'LIVE';
  const isUpcoming = currentMatch.status === 'UPCOMING' || currentMatch.status === 'SCHEDULED';
  const isFinished = currentMatch.status === 'FINISHED' || currentMatch.status === 'FT';
  const streams = currentMatch.streams || [];

  const isCricketOrLong = Boolean(
    sportName?.toLowerCase() === 'cricket' ||
    currentMatch.sport_id === 'cricket' ||
    String(currentMatch.home_team?.display_score || '').includes('&') ||
    String(currentMatch.home_team?.display_score || '').includes('/') ||
    String(currentMatch.away_team?.display_score || '').includes('&') ||
    String(currentMatch.away_team?.display_score || '').includes('/') ||
    (String(currentMatch.home_team?.display_score || '').length + String(currentMatch.away_team?.display_score || '').length > 7)
  );

  const handlePrev = useCallback(() => {
    setIsAutoPlaying(false);
    setCurrentIndex((prev) => (prev === 0 ? featuredMatches.length - 1 : prev - 1));
  }, [featuredMatches.length]);

  const handleNext = useCallback(() => {
    setIsAutoPlaying(false);
    setCurrentIndex((prev) => (prev + 1) % featuredMatches.length);
  }, [featuredMatches.length]);

  // Keyboard navigation for HeroPoster fixture carousel (Left/Right Arrow keys)
  useEffect(() => {
    const handleKeyDown = (e) => {
      const activeEl = document.activeElement;
      const tagName = activeEl ? activeEl.tagName.toLowerCase() : '';
      if (tagName === 'input' || tagName === 'textarea' || activeEl?.isContentEditable) {
        return;
      }

      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        handleNext();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        handlePrev();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleNext, handlePrev]);

  return (
    <div 
      className="relative w-full rounded-3xl overflow-hidden shadow-xl border border-slate-200/90 dark:border-slate-800 bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950 text-white transition-all"
      onMouseEnter={() => setIsAutoPlaying(false)}
      onMouseLeave={() => setIsAutoPlaying(true)}
    >
      {/* Subtle luxury background radial gradients */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-emerald-500/20 via-slate-900/40 to-transparent pointer-events-none" />
      <div className="absolute -left-20 -bottom-20 w-80 sm:w-96 h-80 sm:h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -right-20 -top-20 w-80 sm:w-96 h-80 sm:h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none" />

      {/* Main Responsive Container */}
      <div className="relative z-10 p-4 sm:p-7 lg:p-9 flex flex-col justify-between min-h-[300px] sm:min-h-[360px] lg:min-h-[400px]">
        
        {/* 1. TOP BADGES ROW (Clean, compact on mobile, spacious on desktop) */}
        <div className="flex items-center justify-between gap-2 border-b border-white/10 pb-3 sm:pb-4">
          <div className="flex flex-wrap items-center gap-1.5 sm:gap-2">
            {/* Status Indicator */}
            {isLive && (
              <span className="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-full bg-red-600 text-white text-[10px] sm:text-xs font-black uppercase tracking-wider shadow-md shadow-red-600/30">
                <span className="w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-white animate-ping"></span>
                <span>LIVE &bull; {currentMatch.minute || 'LIVE'}</span>
              </span>
            )}
            {isUpcoming && (
              <span className="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-full bg-sky-500/20 text-sky-300 text-[10px] sm:text-xs font-extrabold uppercase tracking-wider border border-sky-400/30">
                <Clock className="w-3 h-3 text-sky-400" />
                <span>UPCOMING &bull; {currentMatch.kickoff_time || 'Scheduled'}</span>
              </span>
            )}
            {isFinished && (
              <span className="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-full bg-slate-700/80 text-slate-200 text-[10px] sm:text-xs font-bold uppercase tracking-wider border border-slate-600">
                <Video className="w-3 h-3 text-emerald-400" />
                <span>FULL TIME</span>
              </span>
            )}

            {/* League Badge */}
            <span className="inline-flex items-center gap-1 px-2.5 sm:px-3 py-1 rounded-full bg-white/10 backdrop-blur text-slate-100 text-[10px] sm:text-xs font-bold border border-white/15 truncate max-w-[180px] sm:max-w-none">
              <Trophy className="w-3 h-3 text-emerald-400 shrink-0" />
              <span className="truncate">{currentMatch.league}</span>
            </span>

            {/* Date Tag */}
            <span className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 backdrop-blur text-emerald-300 text-xs font-extrabold border border-emerald-500/30">
              <Calendar className="w-3.5 h-3.5 text-emerald-400" />
              <span>{currentMatch.kickoff_date || currentMatch.formatted_date_time || 'Upcoming Fixture'}</span>
            </span>
          </div>

          {/* Carousel Arrows on Top for Mobile / Venue on Desktop */}
          <div className="flex items-center gap-1.5">
            <div className="hidden lg:flex items-center gap-1.5 text-xs text-slate-300 font-medium mr-3">
              <MapPin className="w-3.5 h-3.5 text-emerald-400" />
              <span>{currentMatch.stadium}</span>
            </div>

            <button
              onClick={handlePrev}
              aria-label="Previous Match"
              className="p-1.5 sm:p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white border border-white/15 transition-all cursor-pointer"
            >
              <ChevronLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
            </button>
            <button
              onClick={handleNext}
              aria-label="Next Match"
              className="p-1.5 sm:p-2 rounded-xl bg-white/10 hover:bg-white/20 text-white border border-white/15 transition-all cursor-pointer"
            >
              <ChevronRight className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
            </button>
          </div>
        </div>

        {/* 2. MATCH SHOWCASE: Mobile Side-by-Side vs Desktop Full Layout */}
        <div className="my-4 sm:my-6 lg:my-8 flex items-center justify-between gap-2 sm:gap-6 lg:gap-12">
          
          {/* Home Team */}
          <div className="flex-1 flex flex-col md:flex-row items-center gap-2 sm:gap-4 text-center md:text-left min-w-0">
            <div className="w-14 h-14 sm:w-20 sm:h-20 lg:w-24 lg:h-24 rounded-2xl bg-white/10 backdrop-blur-md p-2 sm:p-3 flex items-center justify-center border border-white/20 shadow-2xl shrink-0">
              <img 
                src={currentMatch.home_team?.logo} 
                alt={currentMatch.home_team?.name}
                onError={(e) => handleLogoError(e, currentMatch.home_team?.name)}
                className="w-full h-full object-contain filter drop-shadow-md"
              />
            </div>
            <div className="min-w-0">
              <span className="hidden sm:block text-[10px] sm:text-xs font-extrabold uppercase tracking-widest text-emerald-400">HOME</span>
              <h2 className="text-sm sm:text-xl lg:text-2xl font-black text-white tracking-tight leading-snug truncate">
                {currentMatch.home_team?.name}
              </h2>
              {isCricketOrLong && (currentMatch.home_team?.display_score || currentMatch.home_team?.score) ? (
                <div className="text-base sm:text-2xl font-black text-emerald-400 font-mono mt-0.5">
                  {currentMatch.home_team?.display_score || currentMatch.home_team?.score}
                </div>
              ) : (
                <span className="hidden sm:block text-xs text-slate-300 font-medium">{currentMatch.home_team?.form || 'Form: W-D-W'}</span>
              )}
            </div>
          </div>

          {/* Center Score / VS Box */}
          <div className="flex flex-col items-center justify-center shrink-0 px-3 sm:px-6 py-2 sm:py-3 rounded-2xl bg-black/40 backdrop-blur-md border border-white/15 shadow-inner">
            {isUpcoming ? (
              <div className="text-center">
                <span className="text-lg sm:text-2xl lg:text-3xl font-black text-sky-400 tracking-wider font-mono">VS</span>
                <div className="text-[9px] sm:text-[11px] font-bold text-slate-300 uppercase tracking-wider mt-0.5">
                  {currentMatch.kickoff_time || 'Scheduled'}
                </div>
              </div>
            ) : isCricketOrLong ? (
              <div className="text-center">
                <div className="text-base sm:text-xl font-black text-emerald-400 tracking-wider font-mono">
                  {isLive ? 'LIVE' : 'FINAL'}
                </div>
                <div className="text-[9px] sm:text-[11px] font-bold text-slate-300 uppercase tracking-wider mt-0.5 flex items-center justify-center gap-1">
                  {isLive && <span className="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></span>}
                  <span>{currentMatch.minute || (isLive ? 'In Play' : 'Full Time')}</span>
                </div>
              </div>
            ) : (
              <div className="text-center">
                <div className="text-xl sm:text-3xl lg:text-4xl font-black text-emerald-400 tracking-wider font-mono">
                  {(currentMatch.home_team?.display_score || currentMatch.home_team?.score) ?? 0} : {(currentMatch.away_team?.display_score || currentMatch.away_team?.score) ?? 0}
                </div>
                <div className="text-[9px] sm:text-[11px] font-bold text-slate-300 uppercase tracking-wider mt-0.5 flex items-center justify-center gap-1">
                  {isLive && <span className="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></span>}
                  <span>{isLive ? currentMatch.minute : 'FULL TIME'}</span>
                </div>
              </div>
            )}
          </div>

          {/* Away Team */}
          <div className="flex-1 flex flex-col md:flex-row-reverse items-center gap-2 sm:gap-4 text-center md:text-right min-w-0">
            <div className="w-14 h-14 sm:w-20 sm:h-20 lg:w-24 lg:h-24 rounded-2xl bg-white/10 backdrop-blur-md p-2 sm:p-3 flex items-center justify-center border border-white/20 shadow-2xl shrink-0">
              <img 
                src={currentMatch.away_team?.logo} 
                alt={currentMatch.away_team?.name}
                onError={(e) => handleLogoError(e, currentMatch.away_team?.name)}
                className="w-full h-full object-contain filter drop-shadow-md"
              />
            </div>
            <div className="min-w-0">
              <span className="hidden sm:block text-[10px] sm:text-xs font-extrabold uppercase tracking-widest text-sky-400">AWAY</span>
              <h2 className="text-sm sm:text-xl lg:text-2xl font-black text-white tracking-tight leading-snug truncate">
                {currentMatch.away_team?.name}
              </h2>
              {isCricketOrLong && (currentMatch.away_team?.display_score || currentMatch.away_team?.score) ? (
                <div className="text-base sm:text-2xl font-black text-emerald-400 font-mono mt-0.5">
                  {currentMatch.away_team?.display_score || currentMatch.away_team?.score}
                </div>
              ) : (
                <span className="hidden sm:block text-xs text-slate-300 font-medium">{currentMatch.away_team?.form || 'Form: D-W-L'}</span>
              )}
            </div>
          </div>

        </div>

        {/* 3. BOTTOM ACTION BAR: Clean, spacious, mobile-optimized */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-3 sm:pt-4 border-t border-white/10">
          
          {/* Main CTA Buttons */}
          <div className="flex items-center gap-2 w-full sm:w-auto">
            <button
              onClick={() => onWatchMatch({ type: 'match', sport: sportName || currentMatch.sport || 'Football', data: currentMatch })}
              className="flex-1 sm:flex-initial flex items-center justify-center gap-2 px-5 sm:px-7 py-2.5 sm:py-3 rounded-xl sm:rounded-2xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs sm:text-sm tracking-wide shadow-lg shadow-emerald-500/30 hover:scale-[1.02] active:scale-[0.98] transition-all cursor-pointer"
            >
              {isFinished ? (
                <>
                  <PlayCircle className="w-4 h-4 fill-slate-950" />
                  <span>WATCH REPLAY</span>
                </>
              ) : isLive ? (
                <>
                  <Play className="w-4 h-4 fill-slate-950" />
                  <span>WATCH LIVE (HD)</span>
                </>
              ) : (
                <>
                  <Clock className="w-4 h-4" />
                  <span>STREAM PREVIEW</span>
                </>
              )}
            </button>

            {onOpenStats && (
              <button
                onClick={() => onOpenStats(currentMatch)}
                className="flex items-center justify-center gap-1.5 px-3.5 sm:px-4 py-2.5 sm:py-3 rounded-xl sm:rounded-2xl bg-white/10 hover:bg-white/20 text-white text-xs font-bold border border-white/15 transition-all cursor-pointer"
              >
                <BarChart2 className="w-3.5 h-3.5 text-emerald-400" />
                <span className="hidden sm:inline">Match Center</span>
                <span className="sm:hidden">Stats</span>
              </button>
            )}
          </div>

          {/* Quick Server Selector */}
          {streams.length > 0 && (
            <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none w-full sm:w-auto justify-start sm:justify-end">
              <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider shrink-0 flex items-center gap-1">
                <Tv className="w-3 h-3 text-emerald-400" />
                <span className="hidden sm:inline">{isFinished ? 'Replays:' : 'Servers:'}</span>
              </span>
              <div className="flex items-center gap-1">
                {streams.slice(0, 3).map((s, idx) => (
                  <button
                    key={s.id || idx}
                    onClick={() => {
                      const matchCopy = { ...currentMatch, defaultServerIndex: idx };
                      onWatchMatch({ type: 'match', sport: sportName || currentMatch.sport || 'Football', data: matchCopy });
                    }}
                    className="px-2.5 py-1 rounded-lg bg-white/10 hover:bg-emerald-500 hover:text-slate-950 text-slate-200 text-[11px] font-bold border border-white/15 transition-all cursor-pointer whitespace-nowrap"
                  >
                    {s.network || `Server ${idx + 1}`}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Dots Indicator */}
          <div className="hidden sm:flex items-center gap-1.5">
            {featuredMatches.map((_, idx) => (
              <button
                key={idx}
                onClick={() => {
                  setIsAutoPlaying(false);
                  setCurrentIndex(idx);
                }}
                className={`h-1.5 rounded-full transition-all cursor-pointer ${
                  currentIndex === idx ? 'w-5 bg-emerald-400' : 'w-1.5 bg-white/30 hover:bg-white/60'
                }`}
                aria-label={`Go to slide ${idx + 1}`}
              />
            ))}
          </div>

        </div>

      </div>
    </div>
  );
}
