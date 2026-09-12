import React, { useState, useRef, useEffect } from 'react';
import { 
  Trophy, 
  Radio, 
  Layers, 
  Clock, 
  CheckCircle2, 
  Calendar,
  PlayCircle,
  ChevronDown
} from 'lucide-react';

export default function MidTopTabs({ 
  activeSection = 'matches',
  setActiveSection,
  selectedStatus = 'all',
  setSelectedStatus,
  selectedLeague = 'all',
  setSelectedLeague,
  totalMatches = 0,
  liveCount = 0,
  upcomingCount = 0,
  finishedCount = 0,
  channelsCount = 0,
  replaysCount = 14,
  favoritesCount = 0,
  leagues = [],
  sportName = 'Football'
}) {
  const [isStatusOpen, setIsStatusOpen] = useState(false);
  const [isLeagueOpen, setIsLeagueOpen] = useState(false);
  const statusRef = useRef(null);
  const leagueRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (statusRef.current && !statusRef.current.contains(event.target)) {
        setIsStatusOpen(false);
      }
      if (leagueRef.current && !leagueRef.current.contains(event.target)) {
        setIsLeagueOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    document.addEventListener('touchstart', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('touchstart', handleClickOutside);
    };
  }, []);

  const LEAGUE_PILLS = [
    { id: 'all', label: 'All Leagues', short: 'ALL' },
    { id: 'epl', label: 'Premier League', short: 'EPL' },
    { id: 'ucl', label: 'Champions League', short: 'UCL' },
    { id: 'uel', label: 'Europa League', short: 'UEL' },
    { id: 'laliga', label: 'La Liga', short: 'ESP' },
    { id: 'seriea', label: 'Serie A', short: 'ITA' },
    { id: 'bundesliga', label: 'Bundesliga', short: 'GER' },
    { id: 'fra1', label: 'Ligue 1', short: 'FRA' },
    { id: 'spl', label: 'Saudi Pro League', short: 'SPL' },
  ];

  const displayLeagues = (leagues && leagues.length > 0)
    ? [
        { id: 'all', label: `All ${sportName || 'Sport'} Leagues`, short: 'ALL' },
        ...leagues.map(l => ({
          id: l.id,
          label: l.name,
          short: l.short_code || l.code || l.id.toUpperCase()
        }))
      ]
    : LEAGUE_PILLS;

  const STATUS_BUTTONS = [
    { id: 'all', shortLabel: 'All', label: 'All Fixtures', count: totalMatches, icon: Calendar },
    { id: 'live', shortLabel: 'Live', label: 'Live Now', count: liveCount, isLive: true },
    { id: 'upcoming', shortLabel: 'Upcoming', label: 'Upcoming', count: upcomingCount, icon: Clock },
    { id: 'finished', shortLabel: 'Results', label: 'Results & Replays', count: finishedCount, icon: CheckCircle2 },
  ];

  const currentStatusObj = STATUS_BUTTONS.find(b => b.id === (selectedStatus || 'all')) || STATUS_BUTTONS[0];
  const StatusIcon = currentStatusObj.icon;
  const currentLeagueObj = displayLeagues.find(l => l.id === selectedLeague) || displayLeagues[0];

  return (
    <div className="space-y-2.5 sm:space-y-3.5 my-2.5 sm:my-4">
      {/* 1. TOP-LEVEL PRIMARY VIEW SWITCHER */}
      <div className="w-full max-w-4xl mx-auto p-1 sm:p-1.5 bg-slate-200/80 dark:bg-slate-900 rounded-2xl border border-slate-300/80 dark:border-slate-800 shadow-xs flex items-center gap-1 sm:gap-1.5">
        
        {/* Option 1: Match Fixtures & Live Feeds */}
        <button
          onClick={() => setActiveSection('matches')}
          className={`flex-1 min-w-0 flex items-center justify-center gap-1 sm:gap-2 py-2 sm:py-3 px-1.5 sm:px-4 rounded-xl text-xs sm:text-sm font-black transition-all cursor-pointer select-none ${
            activeSection === 'matches'
              ? 'bg-white dark:bg-slate-800 text-slate-950 dark:text-white shadow-sm border border-slate-200/80 dark:border-slate-700 scale-[1.01]'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white hover:bg-slate-300/40 dark:hover:bg-slate-800/50'
          }`}
        >
          <Calendar className={`w-3.5 h-3.5 sm:w-4.5 sm:h-4.5 shrink-0 ${activeSection === 'matches' ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-400'}`} />
          <span className="truncate">Fixtures</span>
          {liveCount > 0 ? (
            <>
              <span className="sm:hidden w-2 h-2 rounded-full bg-red-500 animate-pulse shrink-0" />
              <span className="hidden sm:inline-block text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 bg-red-500 text-white">
                {liveCount} LIVE
              </span>
            </>
          ) : (
            <span className="hidden sm:inline-block text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 bg-slate-300/80 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
              {totalMatches}
            </span>
          )}
        </button>

        {/* Option 2: Replays & Classics Vault */}
        <button
          onClick={() => setActiveSection('replays')}
          className={`flex-1 min-w-0 flex items-center justify-center gap-1 sm:gap-2 py-2 sm:py-3 px-1.5 sm:px-4 rounded-xl text-xs sm:text-sm font-black transition-all cursor-pointer select-none ${
            activeSection === 'replays'
              ? 'bg-emerald-600 text-white shadow-sm scale-[1.01]'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white hover:bg-slate-300/40 dark:hover:bg-slate-800/50'
          }`}
        >
          <PlayCircle className={`w-3.5 h-3.5 sm:w-4.5 sm:h-4.5 shrink-0 ${activeSection === 'replays' ? 'text-white' : 'text-slate-400'}`} />
          <span className="truncate">
            <span className="sm:hidden">Replays</span>
            <span className="hidden sm:inline">{sportName || 'Sports'} Replays</span>
          </span>
          <span className="hidden sm:inline-block text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 bg-slate-950 text-white">
            Classics
          </span>
        </button>

        {/* Option 3: 24/7 Global TV Channels */}
        <button
          onClick={() => setActiveSection('channels')}
          className={`flex-1 min-w-0 flex items-center justify-center gap-1 sm:gap-2 py-2 sm:py-3 px-1.5 sm:px-4 rounded-xl text-xs sm:text-sm font-black transition-all cursor-pointer select-none ${
            activeSection === 'channels'
              ? 'bg-emerald-600 text-white shadow-sm scale-[1.01]'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white hover:bg-slate-300/40 dark:hover:bg-slate-800/50'
          }`}
        >
          <Radio className={`w-3.5 h-3.5 sm:w-4.5 sm:h-4.5 shrink-0 ${activeSection === 'channels' ? 'text-white' : 'text-slate-400'}`} />
          <span className="truncate">24/7 TV</span>
          <span className="hidden sm:inline-block text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 bg-slate-950 text-white">
            {channelsCount}
          </span>
        </button>

        {/* Option 4: Dual Multi-View */}
        <button
          onClick={() => setActiveSection('multiview')}
          className={`px-2.5 sm:px-3.5 py-2 sm:py-3 rounded-xl text-xs font-bold transition-all cursor-pointer select-none flex items-center gap-1 sm:gap-1.5 shrink-0 ${
            activeSection === 'multiview'
              ? 'bg-indigo-600 text-white shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white hover:bg-slate-300/40 dark:hover:bg-slate-800/50'
          }`}
          title="Dual Screen Multi-View"
        >
          <Layers className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
          <span className="hidden lg:inline">Multi-View</span>
        </button>
      </div>

      {/* 2. SUB-FILTERS: COMPACT DROPDOWNS POSITIONED AT CORNERS OF CENTRAL SECTION */}
      {activeSection === 'matches' && (
        <div className="w-full flex items-center justify-between gap-3 pt-1.5 pb-0.5">
          
          {/* Left Corner: Status Filter Dropdown */}
          <div ref={statusRef} className="relative w-auto min-w-[140px] sm:min-w-[190px]">
            <button
              type="button"
              onClick={() => {
                setIsStatusOpen(!isStatusOpen);
                setIsLeagueOpen(false);
              }}
              className={`w-full flex items-center justify-between gap-2.5 px-3 sm:px-3.5 py-2 sm:py-2.5 rounded-xl sm:rounded-2xl text-xs sm:text-sm font-bold border transition-all duration-200 cursor-pointer select-none shadow-2xs ${
                isStatusOpen 
                  ? 'bg-white dark:bg-slate-900 border-emerald-500 ring-2 ring-emerald-500/20 text-slate-900 dark:text-white shadow-md' 
                  : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 hover:border-emerald-500/50 dark:hover:border-emerald-500/50 text-slate-800 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400'
              }`}
            >
              <div className="flex items-center gap-2 truncate">
                {currentStatusObj?.isLive ? (
                  <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse shrink-0" />
                ) : (
                  StatusIcon && <StatusIcon className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                )}
                <span className="truncate">{currentStatusObj?.label || 'All Fixtures'}</span>
              </div>
              <div className="flex items-center gap-1.5 shrink-0">
                <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-black ${
                  currentStatusObj?.isLive 
                    ? 'bg-red-500 text-white' 
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                }`}>
                  {currentStatusObj?.count || 0}
                </span>
                <ChevronDown className={`w-3.5 h-3.5 text-slate-400 transition-transform duration-200 ${isStatusOpen ? 'rotate-180 text-emerald-500' : ''}`} />
              </div>
            </button>

            {/* Status Dropdown Menu (Left-aligned) */}
            {isStatusOpen && (
              <div className="absolute top-full left-0 mt-1.5 w-56 sm:w-64 p-1.5 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200/90 dark:border-slate-800 shadow-2xl z-50 animate-in fade-in slide-in-from-top-1 duration-150 space-y-1">
                {STATUS_BUTTONS.map((item) => {
                  const isSelected = (selectedStatus || 'all') === item.id;
                  const ItemIcon = item.icon;
                  return (
                    <button
                      key={item.id}
                      onClick={() => {
                        setSelectedStatus(item.id);
                        setIsStatusOpen(false);
                      }}
                      className={`w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl text-xs font-bold transition-all duration-150 cursor-pointer select-none ${
                        isSelected
                          ? (item.isLive ? 'bg-red-500 text-white font-black shadow-xs' : 'bg-emerald-600 text-white font-black shadow-xs')
                          : 'text-slate-700 dark:text-slate-300 hover:bg-emerald-500/10 hover:text-emerald-600 dark:hover:text-emerald-400'
                      }`}
                    >
                      <div className="flex items-center gap-2 truncate">
                        {item.isLive ? (
                          <span className={`w-2 h-2 rounded-full ${isSelected ? 'bg-white' : 'bg-red-500'} animate-pulse shrink-0`} />
                        ) : (
                          ItemIcon && <ItemIcon className={`w-3.5 h-3.5 shrink-0 ${isSelected ? 'text-white' : 'text-slate-400'}`} />
                        )}
                        <span className="truncate">{item.label}</span>
                      </div>
                      <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-black ${
                        isSelected ? 'bg-black/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                      }`}>
                        {item.count}
                      </span>
                    </button>
                  );
                })}
              </div>
            )}
          </div>

          {/* Right Corner: League Filter Dropdown */}
          <div ref={leagueRef} className="relative w-auto min-w-[150px] sm:min-w-[210px]">
            <button
              type="button"
              onClick={() => {
                setIsLeagueOpen(!isLeagueOpen);
                setIsStatusOpen(false);
              }}
              className={`w-full flex items-center justify-between gap-2.5 px-3 sm:px-3.5 py-2 sm:py-2.5 rounded-xl sm:rounded-2xl text-xs sm:text-sm font-bold border transition-all duration-200 cursor-pointer select-none shadow-2xs ${
                isLeagueOpen 
                  ? 'bg-white dark:bg-slate-900 border-emerald-500 ring-2 ring-emerald-500/20 text-slate-900 dark:text-white shadow-md' 
                  : 'bg-white dark:bg-slate-900 border-slate-200/90 dark:border-slate-800 hover:border-emerald-500/50 dark:hover:border-emerald-500/50 text-slate-800 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400'
              }`}
            >
              <div className="flex items-center gap-2 truncate">
                <Trophy className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                <span className="truncate">{currentLeagueObj?.label || 'All Leagues'}</span>
              </div>
              <div className="flex items-center gap-1.5 shrink-0">
                <span className="text-[10px] font-black px-1.5 py-0.2 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                  {currentLeagueObj?.short || 'ALL'}
                </span>
                <ChevronDown className={`w-3.5 h-3.5 text-slate-400 transition-transform duration-200 ${isLeagueOpen ? 'rotate-180 text-emerald-500' : ''}`} />
              </div>
            </button>

            {/* League Dropdown Menu (Right-aligned) */}
            {isLeagueOpen && (
              <div className="absolute top-full right-0 mt-1.5 w-60 sm:w-72 p-1.5 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200/90 dark:border-slate-800 shadow-2xl z-50 max-h-72 overflow-y-auto scrollbar-thin animate-in fade-in slide-in-from-top-1 duration-150 space-y-1">
                {displayLeagues.map((l) => {
                  const isSelected = selectedLeague === l.id;
                  return (
                    <button
                      key={l.id}
                      onClick={() => {
                        setSelectedLeague(l.id);
                        setIsLeagueOpen(false);
                      }}
                      className={`w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl text-xs font-bold transition-all duration-150 cursor-pointer select-none ${
                        isSelected
                          ? 'bg-emerald-600 text-white font-black shadow-xs'
                          : 'text-slate-700 dark:text-slate-300 hover:bg-emerald-500/10 hover:text-emerald-600 dark:hover:text-emerald-400'
                      }`}
                    >
                      <span className="truncate">{l.label}</span>
                      <span className={`text-[10px] font-black px-1.5 py-0.2 rounded ${
                        isSelected ? 'bg-black/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                      }`}>
                        {l.short}
                      </span>
                    </button>
                  );
                })}
              </div>
            )}
          </div>

        </div>
      )}
    </div>
  );
}
