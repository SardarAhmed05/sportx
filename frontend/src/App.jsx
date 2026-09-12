import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import HeroPoster from './components/HeroPoster';
import MidTopTabs from './components/MidTopTabs';
import VideoPlayer from './components/VideoPlayer';
import MultiViewPlayer from './components/MultiViewPlayer';
import FootballSection from './components/FootballSection';
import ChannelsSection from './components/ChannelsSection';
import FavoritesSection from './components/FavoritesSection';
import FootballReplaysSection from './components/FootballReplaysSection';
import MatchStatsModal from './components/MatchStatsModal';
import CustomStreamModal from './components/CustomStreamModal';
import FeedbackSection from './components/FeedbackSection';
import ErrorBoundary from './components/ErrorBoundary';
import Footer from './components/Footer';

import { 
  fetchOverview, 
  fetchFootballMatches, 
  fetchFootballReplays,
  fetchChannels, 
  fetchCategories, 
  triggerScraper,
  fetchLiveSync
} from './services/api';

import { 
  AlertCircle
} from 'lucide-react';

export default function App() {
  // Theme State (Light / Dark)
  const [theme, setTheme] = useState(() => {
    try {
      return localStorage.getItem('sportx_theme') || 'dark';
    } catch {
      return 'dark';
    }
  });

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    try {
      localStorage.setItem('sportx_theme', theme);
    } catch (e) {
      console.error(e);
    }
  }, [theme]);

  // World-Class Silky-Smooth Theme Transition (Native View Transitions API + GPU Crossfade)
  const toggleTheme = () => {
    const nextTheme = theme === 'dark' ? 'light' : 'dark';

    // 1. Chrome / Edge / Modern Safari: Native View Transitions API
    if (document.startViewTransition) {
      document.documentElement.classList.add('theme-changing');
      const transition = document.startViewTransition(() => {
        if (nextTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
        setTheme(nextTheme);
        try {
          localStorage.setItem('sportx_theme', nextTheme);
        } catch (e) {}
      });

      transition.finished.finally(() => {
        document.documentElement.classList.remove('theme-changing');
      });
      return;
    }

    // 2. Coordinated Fallback for browsers without View Transitions
    document.documentElement.classList.add('theme-changing');
    if (nextTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    setTheme(nextTheme);
    try {
      localStorage.setItem('sportx_theme', nextTheme);
    } catch (e) {}
    requestAnimationFrame(() => {
      document.documentElement.classList.remove('theme-changing');
    });
  };

  // Navigation & View State (Scoped strictly to Football, Cricket, Tennis)
  const [activeSport, setActiveSport] = useState(() => {
    try {
      const saved = localStorage.getItem('sportx_active_sport') || 'football';
      return ['football', 'cricket', 'tennis'].includes(saved) ? saved : 'football';
    } catch {
      return 'football';
    }
  });
  const [activeSection, setActiveSection] = useState('matches'); // 'matches' | 'channels' | 'multiview' | 'favorites'
  const [selectedLeague, setSelectedLeague] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all'); // 'all', 'live', 'upcoming', 'finished'
  const [searchQuery, setSearchQuery] = useState('');
  
  // Cache TTL: only use localStorage cache if it's less than 5 minutes old
  const CACHE_TTL_MS = 5 * 60 * 1000;
  const isCacheFresh = (sport) => {
    try {
      const ts = localStorage.getItem(`sportx_cached_at_${sport}`);
      if (!ts) return false;
      return (Date.now() - parseInt(ts, 10)) < CACHE_TTL_MS;
    } catch { return false; }
  };

  // Data State with Instant Cache Hydration (only if cache is fresh < 5 min)
  const [overview, setOverview] = useState(() => {
    try {
      const initialSport = localStorage.getItem('sportx_active_sport') || 'football';
      if (!isCacheFresh(initialSport)) return null;
      const c = localStorage.getItem(`sportx_cached_overview_${initialSport}`) || localStorage.getItem('sportx_cached_overview');
      return c ? JSON.parse(c) : null;
    } catch { return null; }
  });
  const [footballMatches, setFootballMatches] = useState(() => {
    try {
      const initialSport = localStorage.getItem('sportx_active_sport') || 'football';
      if (!isCacheFresh(initialSport)) return [];
      const c = localStorage.getItem(`sportx_cached_matches_${initialSport}`) || localStorage.getItem('sportx_cached_matches');
      return c ? JSON.parse(c) : [];
    } catch { return []; }
  });
  const [replays, setReplays] = useState(() => {
    try {
      const initialSport = localStorage.getItem('sportx_active_sport') || 'football';
      if (!isCacheFresh(initialSport)) return [];
      const c = localStorage.getItem(`sportx_cached_replays_${initialSport}`) || localStorage.getItem('sportx_cached_replays');
      return c ? JSON.parse(c) : [];
    } catch { return []; }
  });
  const [replaysCategories, setReplaysCategories] = useState([]);
  const [channels, setChannels] = useState(() => {
    try {
      const initialSport = localStorage.getItem('sportx_active_sport') || 'football';
      if (!isCacheFresh(initialSport)) return [];
      const c = localStorage.getItem(`sportx_cached_channels_${initialSport}`) || localStorage.getItem('sportx_cached_channels');
      return c ? JSON.parse(c) : [];
    } catch { return []; }
  });
  const [categories, setCategories] = useState([]);
  const [countries, setCountries] = useState([]);
  
  // Show loading spinner if no fresh cache exists
  const [loading, setLoading] = useState(() => {
    try {
      const initialSport = localStorage.getItem('sportx_active_sport') || 'football';
      return !isCacheFresh(initialSport);
    } catch {
      return true;
    }
  });
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [error, setError] = useState(null);

  // Active Live Video Player State
  const [activeStream, setActiveStream] = useState(null);
  
  // Multi-View Streams State
  const [multiStream1, setMultiStream1] = useState(null);
  const [multiStream2, setMultiStream2] = useState(null);

  // Modals
  const [statsModalMatch, setStatsModalMatch] = useState(null);
  const [isCustomStreamModalOpen, setIsCustomStreamModalOpen] = useState(false);

  // Favorites
  const [favorites, setFavorites] = useState(() => {
    try {
      const saved = localStorage.getItem('sportx_favorites');
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('sportx_favorites', JSON.stringify(favorites));
    } catch (e) {
      console.error(e);
    }
  }, [favorites]);

  const toggleFavorite = (item) => {
    if (!item) return;
    const exists = favorites.some(f => f.data?.id === item.data?.id);

    if (exists) {
      setFavorites(favorites.filter(f => f.data?.id !== item.data?.id));
    } else {
      setFavorites([...favorites, item]);
    }
  };

  const isItemFavorite = (item) => {
    if (!item) return false;
    return favorites.some(f => f.data?.id === item.data?.id);
  };

  // Load data for the requested sport from backend API (with optional silent background refresh)
  const loadData = async (sportToLoad = activeSport, isRefresh = false, isSilent = false) => {
    const targetSport = (typeof sportToLoad === 'string' && sportToLoad.trim()) ? sportToLoad.trim() : activeSport;
    if (!isSilent) {
      if (isRefresh) {
        setIsRefreshing(true);
      } else if (!footballMatches.length) {
        setLoading(true);
      }
    }
    setError(null);

    try {
      const [overviewData, channelsData, catData, replaysData] = await Promise.all([
        fetchOverview(targetSport),
        fetchChannels(targetSport),
        fetchCategories(),
        fetchFootballReplays(null, null, null, targetSport).catch(() => ({ replays: [], categories: [] }))
      ]);

      if (overviewData) {
        setOverview(overviewData);
        const matchesList = overviewData.matches?.matches || overviewData.football?.matches || (Array.isArray(overviewData.matches) ? overviewData.matches : []);
        setFootballMatches(Array.isArray(matchesList) ? matchesList : []);
      } else {
        setFootballMatches([]);
      }

      const chList = channelsData?.channels;
      setChannels(Array.isArray(chList) ? chList : []);

      const repList = replaysData?.replays;
      setReplays(Array.isArray(repList) ? repList : []);

      if (replaysData?.categories) {
        setReplaysCategories(replaysData.categories);
      }
      if (catData?.categories) {
        setCategories(catData.categories);
      }
      if (catData?.countries) {
        setCountries(catData.countries);
      }

      // Cache locally so switching sports has 0.0s instant hydration
      try {
        if (overviewData) localStorage.setItem(`sportx_cached_overview_${targetSport}`, JSON.stringify(overviewData));
        const matchesList = overviewData?.matches?.matches || overviewData?.football?.matches || [];
        if (matchesList.length) localStorage.setItem(`sportx_cached_matches_${targetSport}`, JSON.stringify(matchesList));
        if (repList?.length) localStorage.setItem(`sportx_cached_replays_${targetSport}`, JSON.stringify(repList));
        if (chList?.length) localStorage.setItem(`sportx_cached_channels_${targetSport}`, JSON.stringify(chList));
        // Write timestamp so TTL check knows when this cache was saved
        localStorage.setItem(`sportx_cached_at_${targetSport}`, String(Date.now()));

        if (targetSport === 'football') {
          if (overviewData) localStorage.setItem('sportx_cached_overview', JSON.stringify(overviewData));
          if (matchesList.length) localStorage.setItem('sportx_cached_matches', JSON.stringify(matchesList));
          if (repList?.length) localStorage.setItem('sportx_cached_replays', JSON.stringify(repList));
          if (chList?.length) localStorage.setItem('sportx_cached_channels', JSON.stringify(chList));
        }
      } catch (e) {}
    } catch (err) {
      console.error('Data load error:', err);
      if (!footballMatches.length) {
        setError('Unable to load sports streams from backend. Please ensure the backend server is running.');
      }
    } finally {
      if (!isSilent) {
        setLoading(false);
        setIsRefreshing(false);
      }
    }
  };

  // Sport Switcher Handler
  const handleSelectSport = (newSport) => {
    const s = ['football', 'cricket', 'tennis'].includes(newSport) ? newSport : 'football';
    if (s === activeSport) return;
    setActiveSport(s);
    try {
      localStorage.setItem('sportx_active_sport', s);
    } catch (e) {}

    setSelectedLeague('all');
    setSelectedStatus('all');

    // Instant Hydration from cached data for this sport if available
    try {
      const cachedOverview = localStorage.getItem(`sportx_cached_overview_${s}`);
      const cachedMatches = localStorage.getItem(`sportx_cached_matches_${s}`);
      const cachedReplays = localStorage.getItem(`sportx_cached_replays_${s}`);
      const cachedChannels = localStorage.getItem(`sportx_cached_channels_${s}`);

      if (cachedMatches) {
        if (cachedOverview) setOverview(JSON.parse(cachedOverview));
        setFootballMatches(JSON.parse(cachedMatches));
        if (cachedReplays) setReplays(JSON.parse(cachedReplays));
        if (cachedChannels) setChannels(JSON.parse(cachedChannels));
      } else {
        setFootballMatches([]);
        setOverview(null);
        setReplays([]);
        setChannels([]);
      }
    } catch (e) {}

    loadData(s);
  };

  useEffect(() => {
    loadData(activeSport);
  }, []);

  // 1. Dual-Tier Adaptive Real-Time Polling Engine:
  // When live matches are active: poll lightweight /live-sync every 6 seconds for instant score & referee clock updates
  // When no live matches are active: poll full data every 30 seconds
  useEffect(() => {
    const hasLive = footballMatches.some(m => m.status === 'LIVE');
    const intervalMs = hasLive ? 6000 : 30000;

    const syncScoreboard = async () => {
      if (document.hidden) return;

      if (!hasLive) {
        loadData(activeSport, false, true);
        return;
      }

      try {
        const liveData = await fetchLiveSync(activeSport);
        if (!liveData || !Array.isArray(liveData.matches)) return;

        const currentLiveCount = footballMatches.filter(m => m.status === 'LIVE').length;
        if (liveData.live_count !== currentLiveCount) {
          // A match transitioned from upcoming to live, or finished - do complete silent refresh
          loadData(activeSport, false, true);
          return;
        }

        if (liveData.matches.length === 0) return;

        const nowSec = Date.now() / 1000;

        // In-place atomic update for real-time scores and clocks
        setFootballMatches(prevMatches => {
          let changed = false;
          const updated = prevMatches.map(m => {
            const liveMatch = liveData.matches.find(lm =>
              (lm.id && lm.id === m.id) ||
              (lm.espn_id && lm.espn_id === m.espn_id) ||
              (lm.home_team?.name && m.home_team?.name && lm.home_team.name.toLowerCase() === m.home_team.name.toLowerCase())
            );

            if (!liveMatch) return m;

            const homeScore = liveMatch.home_team?.score ?? m.home_team?.score;
            const awayScore = liveMatch.away_team?.score ?? m.away_team?.score;
            const minute = liveMatch.minute || m.minute;
            const status = liveMatch.status || m.status;

            if (
              m.home_team?.score !== homeScore ||
              m.away_team?.score !== awayScore ||
              m.minute !== minute ||
              m.status !== status
            ) {
              changed = true;
              return {
                ...m,
                minute,
                match_time: minute.includes('Live') ? minute : `${minute} Live`,
                status,
                clock_seconds: liveMatch.clock_seconds ?? m.clock_seconds,
                period: liveMatch.period ?? m.period,
                live_synced_at: liveMatch.live_synced_at || nowSec,
                home_team: { ...m.home_team, score: homeScore, display_score: homeScore },
                away_team: { ...m.away_team, score: awayScore, display_score: awayScore }
              };
            }
            return m;
          });

          return changed ? updated : prevMatches;
        });

        // Update activeStream if it is currently showing this live match
        setActiveStream(prevStream => {
          if (!prevStream || prevStream.type !== 'match' || !prevStream.data) return prevStream;
          const liveMatch = liveData.matches.find(lm =>
            (lm.id && lm.id === prevStream.data.id) ||
            (lm.espn_id && lm.espn_id === prevStream.data.espn_id) ||
            (lm.home_team?.name && prevStream.data.home_team?.name && lm.home_team.name.toLowerCase() === prevStream.data.home_team.name.toLowerCase())
          );
          if (!liveMatch) return prevStream;
          const homeScore = liveMatch.home_team?.score ?? prevStream.data.home_team?.score;
          const awayScore = liveMatch.away_team?.score ?? prevStream.data.away_team?.score;
          const minute = liveMatch.minute || prevStream.data.minute;
          return {
            ...prevStream,
            data: {
              ...prevStream.data,
              minute,
              match_time: minute.includes('Live') ? minute : `${minute} Live`,
              status: liveMatch.status || prevStream.data.status,
              home_team: { ...prevStream.data.home_team, score: homeScore, display_score: homeScore },
              away_team: { ...prevStream.data.away_team, score: awayScore, display_score: awayScore }
            }
          };
        });

        // Update overview marquee match
        setOverview(prevOv => {
          if (!prevOv?.marquee_match) return prevOv;
          const liveMatch = liveData.matches.find(lm =>
            (lm.id && lm.id === prevOv.marquee_match.id) ||
            (lm.espn_id && lm.espn_id === prevOv.marquee_match.espn_id) ||
            (lm.home_team?.name && prevOv.marquee_match.home_team?.name && lm.home_team.name.toLowerCase() === prevOv.marquee_match.home_team.name.toLowerCase())
          );
          if (!liveMatch) return prevOv;
          const homeScore = liveMatch.home_team?.score ?? prevOv.marquee_match.home_team?.score;
          const awayScore = liveMatch.away_team?.score ?? prevOv.marquee_match.away_team?.score;
          const minute = liveMatch.minute || prevOv.marquee_match.minute;
          return {
            ...prevOv,
            marquee_match: {
              ...prevOv.marquee_match,
              minute,
              match_time: minute.includes('Live') ? minute : `${minute} Live`,
              status: liveMatch.status || prevOv.marquee_match.status,
              home_team: { ...prevOv.marquee_match.home_team, score: homeScore, display_score: homeScore },
              away_team: { ...prevOv.marquee_match.away_team, score: awayScore, display_score: awayScore }
            }
          };
        });
      } catch (e) {
        // Silent background catch
      }
    };

    const intervalId = setInterval(syncScoreboard, intervalMs);
    return () => clearInterval(intervalId);
  }, [activeSport, footballMatches]);

  // 2. Client-Side Live Virtual Clock Interpolator:
  // Interpolates match minutes second-by-second so the clock never appears frozen between referee updates
  useEffect(() => {
    const hasLive = footballMatches.some(m => m.status === 'LIVE');
    if (!hasLive) return;

    const clockTicker = setInterval(() => {
      const nowSec = Date.now() / 1000;
      setFootballMatches(prevMatches => {
        let changed = false;
        const updated = prevMatches.map(m => {
          if (m.status !== 'LIVE' || !m.minute) return m;

          // Check if minute is a normal football minute like "60'", "60", "23'"
          const matchResult = String(m.minute).match(/^(\d+)'?$/);
          if (!matchResult) return m;

          const parsedMin = parseInt(matchResult[1], 10);
          if (isNaN(parsedMin) || parsedMin <= 0) return m;

          const syncTime = m.live_synced_at || nowSec;
          const elapsedSec = Math.max(0, nowSec - syncTime);
          const addedMinutes = Math.floor(elapsedSec / 60);

          if (addedMinutes <= 0) return m;

          // Cap at end of half (45' for 1st half, 90' for 2nd half) until referee adds stoppage time
          let targetMin = parsedMin + addedMinutes;
          if (parsedMin <= 45 && targetMin > 45) targetMin = 45;
          if (parsedMin > 45 && parsedMin <= 90 && targetMin > 90) targetMin = 90;

          const formattedMin = `${targetMin}'`;
          if (formattedMin !== m.minute) {
            changed = true;
            return {
              ...m,
              minute: formattedMin,
              match_time: `${formattedMin} Live`
            };
          }
          return m;
        });

        return changed ? updated : prevMatches;
      });
    }, 10000);

    return () => clearInterval(clockTicker);
  }, [footballMatches]);

  const handleGoHome = () => {
    setActiveSection('matches');
    setActiveStream(null);
    setSearchQuery('');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleRefreshScraper = async () => {
    try {
      setIsRefreshing(true);
      // Run background scraper non-blocking so it never hangs UI
      triggerScraper().catch(err => console.warn('Background scraper notice:', err));
      // Refresh current active sport feeds and live scores
      await loadData(activeSport, true, false);
    } catch (err) {
      console.error('Refresh feeds error:', err);
    } finally {
      setIsRefreshing(false);
    }
  };

  const currentSportName = overview?.sport || 'Football';

  const handleSelectStream = (streamItem) => {
    if (!streamItem) return;
    const normalized = (streamItem.type && streamItem.data)
      ? streamItem
      : { type: 'match', sport: currentSportName, data: streamItem };
    setActiveStream(normalized);
    // Smooth scroll to video player
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSwitchToMultiView = (streamItem) => {
    setMultiStream1(streamItem);
    if (!multiStream2 && footballMatches.length > 1) {
      const other = footballMatches.find(m => m.id !== streamItem.data?.id) || footballMatches[0];
      setMultiStream2({ type: 'match', sport: currentSportName, data: other });
    }
    setActiveSection('multiview');
  };

  // Filter matches based on search query
  const filteredMatches = footballMatches.filter(m => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      m.home_team?.name?.toLowerCase().includes(q) ||
      m.away_team?.name?.toLowerCase().includes(q) ||
      m.league?.toLowerCase().includes(q)
    );
  });

  const liveMatchesCount = footballMatches.filter(m => m.status === 'LIVE').length;
  const upcomingMatchesCount = footballMatches.filter(m => m.status === 'UPCOMING' || m.status === 'SCHEDULED').length;
  const finishedMatchesCount = footballMatches.filter(m => m.status === 'FINISHED' || m.status === 'FT').length;

  // Compile all available streams for Multi-View selector
  const allAvailableStreamItems = [
    ...footballMatches.map(m => ({ type: 'match', sport: currentSportName, data: m })),
    ...replays.map(r => ({ type: 'match', sport: currentSportName, data: r })),
    ...channels.map(c => ({ type: 'channel', sport: currentSportName, data: c }))
  ];

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 selection:bg-emerald-500 selection:text-white">
      {/* 1. Top Clean Navbar with Sport Switcher, Theme Toggle, Custom URL & Saved Buttons */}
      <Navbar
        theme={theme}
        onToggleTheme={toggleTheme}
        activeSport={activeSport}
        onSelectSport={handleSelectSport}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        onRefreshScraper={handleRefreshScraper}
        isRefreshing={isRefreshing}
        matchCount={footballMatches.length}
        liveCount={liveMatchesCount}
        favoritesCount={favorites.length}
        onCustomStreamOpen={() => setIsCustomStreamModalOpen(true)}
        onOpenFavorites={() => setActiveSection('favorites')}
        onGoHome={handleGoHome}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-4 sm:space-y-6">
        {/* Error Notification */}
        {error && (
          <div className="p-4 rounded-2xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 text-rose-800 dark:text-rose-200 text-xs flex items-center justify-between">
            <div className="flex items-center gap-2">
              <AlertCircle className="w-5 h-5 text-rose-600 dark:text-rose-400" />
              <span>{error}</span>
            </div>
            <button
              onClick={() => loadData(activeSport, true)}
              className="px-3 py-1 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-lg cursor-pointer"
            >
              Retry
            </button>
          </div>
        )}

        {/* Loading Spinner */}
        {loading && (
          <div className="py-24 flex flex-col items-center justify-center space-y-4">
            <div className="relative">
              <div className="w-16 h-16 rounded-full border-4 border-slate-200 dark:border-slate-800 border-t-emerald-600 animate-spin"></div>
              <div className="w-10 h-10 rounded-full border-4 border-slate-200 dark:border-slate-800 border-t-emerald-400 animate-spin absolute inset-0 m-auto"></div>
            </div>
            <p className="text-sm font-bold text-slate-700 dark:text-slate-300 tracking-wide">
              Connecting to Official {currentSportName} Data Feeds...
            </p>
          </div>
        )}

        {!loading && (
          <>
            {/* Active Cinema Video Player (if user launched a stream) */}
            {activeStream && (
              <ErrorBoundary onClose={() => setActiveStream(null)}>
                <VideoPlayer
                  streamItem={activeStream}
                  onClose={() => setActiveStream(null)}
                  isFavorite={isItemFavorite(activeStream)}
                  onToggleFavorite={toggleFavorite}
                  onSwitchToMultiView={handleSwitchToMultiView}
                />
              </ErrorBoundary>
            )}

            {/* 3. FIRST PAGE BIG POSTER (Marquee Live / Upcoming Match Showcase) */}
            {activeSection === 'matches' && !activeStream && (
              <HeroPoster
                matches={footballMatches}
                onWatchMatch={handleSelectStream}
                onOpenStats={setStatsModalMatch}
                sportName={currentSportName}
              />
            )}

            {/* 4. MIDDLE-TOP PROMINENT SECTION SWITCHER & SUB-TABS */}
            <MidTopTabs
              activeSection={activeSection}
              setActiveSection={setActiveSection}
              selectedStatus={selectedStatus}
              setSelectedStatus={setSelectedStatus}
              selectedLeague={selectedLeague}
              setSelectedLeague={setSelectedLeague}
              totalMatches={footballMatches.length}
              liveCount={liveMatchesCount}
              upcomingCount={upcomingMatchesCount}
              finishedCount={finishedMatchesCount}
              channelsCount={channels.length}
              replaysCount={replays.length}
              favoritesCount={favorites.length}
              leagues={overview?.leagues || []}
              sportName={currentSportName}
            />

            {/* SECTION: REPLAYS & CLASSICS VAULT */}
            {activeSection === 'replays' && (
              <FootballReplaysSection
                replays={replays}
                categories={replaysCategories}
                onSelectReplay={handleSelectStream}
                searchQuery={searchQuery}
                setSearchQuery={setSearchQuery}
                sportName={currentSportName}
              />
            )}

            {/* SECTION 1: MATCH FIXTURES & LIVE FEEDS */}
            {activeSection === 'matches' && (
              <FootballSection
                matches={filteredMatches}
                selectedLeague={selectedLeague}
                selectedStatus={selectedStatus}
                onSelectMatch={handleSelectStream}
                onOpenStats={setStatsModalMatch}
                onSwitchToReplays={() => setActiveSection('replays')}
                sportName={currentSportName}
              />
            )}

            {/* SECTION 2: 24/7 GLOBAL TV CHANNELS */}
            {activeSection === 'channels' && (
              <ChannelsSection
                channels={channels}
                categories={categories}
                countries={countries}
                onSelectChannel={handleSelectStream}
                sportName={currentSportName}
              />
            )}

            {/* SECTION 3: MULTI-VIEW STUDIO */}
            {activeSection === 'multiview' && (
              <MultiViewPlayer
                stream1={multiStream1}
                stream2={multiStream2}
                allAvailableStreams={allAvailableStreamItems}
                onUpdateStream1={setMultiStream1}
                onUpdateStream2={setMultiStream2}
                onClose={() => setActiveSection('matches')}
              />
            )}

            {/* SECTION 4: FAVORITES */}
            {activeSection === 'favorites' && (
              <FavoritesSection
                favorites={favorites}
                onSelectFavorite={handleSelectStream}
                onRemoveFavorite={toggleFavorite}
              />
            )}
          </>
        )}
      </main>

      {/* Football Match Stats Modal */}
      {statsModalMatch && (
        <MatchStatsModal
          match={statsModalMatch}
          onClose={() => setStatsModalMatch(null)}
          onWatchMatch={handleSelectStream}
        />
      )}

      {/* Custom Stream URL Modal */}
      <CustomStreamModal
        isOpen={isCustomStreamModalOpen}
        onClose={() => setIsCustomStreamModalOpen(false)}
        onPlayCustomStream={handleSelectStream}
      />

      {/* Community Feedback & Comments Section */}
      <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <FeedbackSection />
      </div>

      {/* Footer */}
      <Footer
        totalLiveStreams={footballMatches.length + channels.length}
      />
    </div>
  );
}
