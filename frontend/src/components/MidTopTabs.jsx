import React from 'react';
import { 
  Trophy, 
  Radio, 
  Layers, 
  Clock, 
  CheckCircle2, 
  Calendar,
  PlayCircle
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

  return (
    <div className="space-y-3.5 my-3 sm:my-4">
      {/* 1. TOP-LEVEL PRIMARY VIEW SWITCHER (Robust, responsive, zero text overflow) */}
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
          <span className={`text-[9px] sm:text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 ${
            activeSection === 'matches' 
              ? (liveCount > 0 ? 'bg-red-500 text-white' : 'bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300')
              : 'bg-slate-300/80 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
          }`}>
            {liveCount > 0 ? `${liveCount} LIVE` : `${totalMatches}`}
          </span>
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
          <span className={`text-[9px] sm:text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 ${
            activeSection === 'replays' ? 'bg-slate-950 text-white' : 'bg-slate-300/80 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
          }`}>
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
          <span className={`text-[9px] sm:text-[10px] px-1.5 py-0.5 rounded-full font-black shrink-0 ${
            activeSection === 'channels' ? 'bg-slate-950 text-white' : 'bg-slate-300/80 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
          }`}>
            {channelsCount}
          </span>
        </button>

        {/* Option 4: Dual Multi-View */}
        <button
          onClick={() => setActiveSection('multiview')}
          className={`px-2 sm:px-3.5 py-2 sm:py-3 rounded-xl text-xs font-bold transition-all cursor-pointer select-none flex items-center gap-1 sm:gap-1.5 shrink-0 ${
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

      {/* 2. SUB-FILTERS (Status Buttons & League Pills) */}
      {activeSection === 'matches' && (
        <div className="space-y-2.5">
          {/* Status Buttons */}
          <div className="flex items-center justify-start sm:justify-center overflow-x-auto scrollbar-none -mx-4 px-4 sm:mx-0 sm:px-0">
            <div className="flex items-center gap-1 sm:gap-1.5 p-1 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-2xs whitespace-nowrap">
              {STATUS_BUTTONS.map((btn) => {
                const isActive = (selectedStatus || 'all') === btn.id;
                const IconComponent = btn.icon;
                return (
                  <button
                    key={btn.id}
                    onClick={() => setSelectedStatus(btn.id)}
                    className={`flex items-center gap-1.5 sm:gap-2 px-2.5 sm:px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer whitespace-nowrap select-none ${
                      isActive
                        ? (btn.isLive
                            ? 'bg-red-600 text-white shadow-xs font-black'
                            : 'bg-slate-900 dark:bg-emerald-600 text-white shadow-xs font-black')
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                  >
                    {btn.isLive ? (
                      <span className="w-2 h-2 rounded-full bg-white animate-pulse"></span>
                    ) : (
                      IconComponent && <IconComponent className="w-3.5 h-3.5 shrink-0" />
                    )}
                    <span>
                      <span className="sm:hidden">{btn.shortLabel}</span>
                      <span className="hidden sm:inline">{btn.label}</span>
                    </span>
                    <span className={`text-[9px] sm:text-[10px] px-1.5 py-0.2 rounded-full font-black ${
                      isActive ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400'
                    }`}>
                      {btn.count}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* League Pills (Clean professional text badges with horizontal scroll) */}
          <div className="flex items-center justify-start sm:justify-center overflow-x-auto scrollbar-none -mx-4 px-4 sm:mx-0 sm:px-0">
            <div className="flex items-center gap-1 sm:gap-1.5 py-1 px-1.5 bg-slate-100/90 dark:bg-slate-900 rounded-xl border border-slate-200/80 dark:border-slate-800 whitespace-nowrap">
              {displayLeagues.map((l) => {
                const isSelected = selectedLeague === l.id;
                return (
                  <button
                    key={l.id}
                    onClick={() => setSelectedLeague(l.id)}
                    className={`flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer whitespace-nowrap select-none ${
                      isSelected
                        ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs border border-slate-200 dark:border-slate-700 font-black'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-white/60 dark:hover:bg-slate-800/60'
                    }`}
                  >
                    <span className="text-[9px] sm:text-[10px] font-black px-1 py-0.2 rounded bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300">
                      {l.short}
                    </span>
                    <span>{l.label}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
