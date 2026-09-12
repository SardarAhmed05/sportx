import React, { useState, useEffect } from 'react';
import { 
  Trophy, 
  Play, 
  Tv, 
  BarChart2, 
  Clock, 
  Calendar, 
  CheckCircle2, 
  Video, 
  PlayCircle,
  ChevronLeft,
  ChevronRight,
  ArrowRight
} from 'lucide-react';
import { handleLogoError } from '../utils/avatar';

export default function FootballSection({ 
  matches = [], 
  selectedLeague = 'all', 
  selectedStatus = 'all', 
  onSelectMatch, 
  onOpenStats,
  onSwitchToReplays,
  sportName = 'Football'
}) {
  const PAGE_SIZE = 15;
  const [currentPage, setCurrentPage] = useState(1);

  // Reset page to 1 whenever filters change
  useEffect(() => {
    setCurrentPage(1);
  }, [selectedLeague, selectedStatus, sportName]);

  // 1. Filter by league and status
  const filteredMatches = matches.filter(m => {
    if (selectedLeague !== 'all') {
      const matchLeague = m.league_id === selectedLeague || 
                          m.league?.toLowerCase().includes(selectedLeague.toLowerCase());
      if (!matchLeague) return false;
    }

    if (selectedStatus && selectedStatus !== 'all') {
      const st = m.status?.toUpperCase();
      if (selectedStatus === 'live') {
        if (st !== 'LIVE') return false;
      } else if (selectedStatus === 'upcoming') {
        if (st !== 'UPCOMING' && st !== 'SCHEDULED') return false;
      } else if (selectedStatus === 'finished') {
        if (st !== 'FINISHED' && st !== 'FT') return false;
      }
    }

    return true;
  });

  // Popularity scoring: top teams and top leagues float to the top within each status tier
  const TOP_LEAGUES = {
    'champions league': 100, 'ucl': 100,
    'premier league': 95, 'epl': 95,
    'la liga': 90, 'bundesliga': 85, 'serie a': 85, 'ligue 1': 80,
    'europa league': 75, 'fa cup': 65, 'carabao cup': 60,
    'world cup': 100, 'euros': 90, 'copa america': 85,
    'nations league': 70, 'conference league': 65,
    'ipl': 90, 'psl': 85, 'big bash': 75, 'test': 80,
    'wimbledon': 90, 'us open': 85, 'french open': 85, 'australian open': 85,
  };

  const TOP_TEAMS = {
    'manchester city': 95, 'man city': 95,
    'real madrid': 95, 'barcelona': 93, 'atletico madrid': 80,
    'manchester united': 88, 'man utd': 88, 'man united': 88,
    'liverpool': 90, 'arsenal': 85, 'chelsea': 84, 'tottenham': 80, 'spurs': 80,
    'bayern munich': 90, 'borussia dortmund': 82, 'bvb': 82,
    'juventus': 85, 'inter milan': 84, 'ac milan': 83, 'napoli': 78,
    'psg': 88, 'paris saint-germain': 88,
    'ajax': 75, 'benfica': 74, 'porto': 74, 'celtic': 70,
    'india': 90, 'pakistan': 85, 'australia': 82, 'england': 80,
    'south africa': 75, 'new zealand': 74, 'west indies': 72,
    'novak djokovic': 90, 'carlos alcaraz': 88, 'jannik sinner': 85,
    'iga swiatek': 88, 'aryna sabalenka': 85,
  };

  const getPopularityScore = (match) => {
    let score = 0;
    const league = (match.league || match.competition || '').toLowerCase();
    const homeTeam = (match.home_team?.name || '').toLowerCase();
    const awayTeam = (match.away_team?.name || '').toLowerCase();

    // League score
    for (const [key, val] of Object.entries(TOP_LEAGUES)) {
      if (league.includes(key)) { score = Math.max(score, val); break; }
    }
    // Team score (take highest of both teams)
    for (const [key, val] of Object.entries(TOP_TEAMS)) {
      if (homeTeam.includes(key) || awayTeam.includes(key)) {
        score = Math.max(score, val);
      }
    }
    // Viewer count as tiebreaker
    score += (match.viewers_count || 0) * 0.001;
    return score;
  };

  // 2. Sort matches:
  // - LIVE first (popular LIVE matches within LIVE tier)
  // - Then UPCOMING (popular upcoming matches first)
  // - Then FINISHED (most recent first)
  const sortedMatches = [...filteredMatches].sort((a, b) => {
    const isLiveA = a.status === 'LIVE';
    const isLiveB = b.status === 'LIVE';

    if (isLiveA && !isLiveB) return -1;
    if (!isLiveA && isLiveB) return 1;

    if (isLiveA && isLiveB) {
      // Within LIVE: popular matches first
      return getPopularityScore(b) - getPopularityScore(a);
    }

    const isUpcomingA = a.status === 'UPCOMING' || a.status === 'SCHEDULED';
    const isUpcomingB = b.status === 'UPCOMING' || b.status === 'SCHEDULED';

    if (isUpcomingA && !isUpcomingB) return -1;
    if (!isUpcomingA && isUpcomingB) return 1;

    if (isUpcomingA && isUpcomingB) {
      // Within UPCOMING: popular matches first
      const popDiff = getPopularityScore(b) - getPopularityScore(a);
      if (Math.abs(popDiff) > 1) return popDiff;
      // Tiebreak by kickoff time (sooner first)
      const timeA = a.raw_date ? new Date(a.raw_date).getTime() : Infinity;
      const timeB = b.raw_date ? new Date(b.raw_date).getTime() : Infinity;
      return timeA - timeB;
    }

    // Both finished: most recent first
    const timeA = a.raw_date ? new Date(a.raw_date).getTime() : 0;
    const timeB = b.raw_date ? new Date(b.raw_date).getTime() : 0;
    return timeB - timeA;
  });

  // 3. 15 Matches Per Page Pagination Slicing
  const totalPages = Math.max(1, Math.ceil(sortedMatches.length / PAGE_SIZE));
  const displayedMatches = sortedMatches.slice((currentPage - 1) * PAGE_SIZE, currentPage * PAGE_SIZE);

  return (
    <section className="space-y-4">
      {/* Grid Subheader */}
      <div className="flex flex-wrap items-center justify-between gap-2 pb-2 border-b border-slate-200 dark:border-slate-800">
        <h3 className="text-sm font-extrabold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Match Fixtures & Live Feeds</span>
          <span className="text-xs px-2.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 font-bold border border-emerald-200 dark:border-emerald-800">
            Page {currentPage} of {totalPages} &bull; Showing {displayedMatches.length} of {sortedMatches.length}
          </span>
        </h3>
        <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-600 dark:text-slate-300">
          <Clock className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
          <span>All times in PKT (Pakistan Time &bull; UTC+5)</span>
        </div>
      </div>

      {/* Replay Vault Callout for Finished Matches */}
      {selectedStatus === 'finished' && onSwitchToReplays && (
        <div className="bg-emerald-50/90 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800/80 rounded-2xl p-3.5 flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex items-center gap-2 text-emerald-900 dark:text-emerald-200 font-bold">
            <Trophy className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0" />
            <span>Looking for historic finals, World Cup archives & full match classics?</span>
          </div>
          <button
            onClick={onSwitchToReplays}
            className="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs transition-colors cursor-pointer flex items-center gap-1.5 shadow-xs"
          >
            <span>Open {sportName || 'Sports'} Replays Vault</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      )}

      {/* Match Cards Grid */}
      {displayedMatches.length === 0 ? (
        <div className="py-16 text-center bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
          <Calendar className="w-10 h-10 text-slate-400 dark:text-slate-600 mx-auto" />
          <h4 className="text-sm font-bold text-slate-800 dark:text-slate-200">No matches found for this filter</h4>
          <p className="text-xs text-slate-500 dark:text-slate-400">Try selecting 'All Fixtures' or switching league tabs above.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayedMatches.map((m) => {
            const streams = m.streams || [];
            const isLive = m.status === 'LIVE';
            const isUpcoming = m.status === 'UPCOMING' || m.status === 'SCHEDULED';
            const isFinished = m.status === 'FINISHED' || m.status === 'FT';

            // Detect cricket or long test match scoreline
            const isLongScore = Boolean(
              sportName?.toLowerCase() === 'cricket' ||
              m.sport_id === 'cricket' ||
              String(m.home_team?.display_score || m.home_team?.score || '').includes('&') ||
              String(m.home_team?.display_score || m.home_team?.score || '').includes('/') ||
              String(m.away_team?.display_score || m.away_team?.score || '').includes('&') ||
              String(m.away_team?.display_score || m.away_team?.score || '').includes('/') ||
              (String(m.home_team?.display_score || '').length + String(m.away_team?.display_score || '').length > 7)
            );

            return (
              <div
                key={m.id}
                className="bg-white dark:bg-slate-900 rounded-2xl p-4 border border-slate-200/90 dark:border-slate-800 hover:border-emerald-500/60 dark:hover:border-emerald-500/60 transition-all duration-200 flex flex-col justify-between group shadow-2xs hover:shadow-xl hover:shadow-emerald-500/5 dark:hover:shadow-emerald-950/30 hover:-translate-y-0.5"
              >
                <div>
                  {/* League Header & Status Badge */}
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <span className="text-[11px] font-bold text-slate-600 dark:text-slate-400 flex items-center gap-1.5 truncate max-w-[170px]">
                      <Trophy className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                      <span className="truncate">{m.league}</span>
                    </span>
                    
                    {/* Status Badge */}
                    {isLive && (
                      <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-red-100 dark:bg-red-950/60 text-red-700 dark:text-red-300 text-[10px] font-black uppercase tracking-wider border border-red-200 dark:border-red-900">
                        <span className="w-1.5 h-1.5 rounded-full bg-red-600 animate-pulse"></span>
                        <span>LIVE {m.minute || ''}</span>
                      </span>
                    )}

                    {isUpcoming && (
                      <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-sky-50 dark:bg-sky-950/60 text-sky-700 dark:text-sky-300 text-[10px] font-extrabold uppercase tracking-wider border border-sky-200 dark:border-sky-900">
                        <Clock className="w-3 h-3 text-sky-600 dark:text-sky-400" />
                        <span>UPCOMING</span>
                      </span>
                    )}

                    {isFinished && (
                      <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-[10px] font-extrabold uppercase tracking-wider border border-slate-200 dark:border-slate-700">
                        <CheckCircle2 className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
                        <span>FULL TIME</span>
                      </span>
                    )}
                  </div>

                  {/* PROMINENT DATE & KICKOFF TIME BANNER (in PKT) */}
                  <div className="flex items-center gap-1.5 px-2.5 py-1 mb-2.5 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200/60 dark:border-slate-700/50 text-[11px] text-slate-700 dark:text-slate-300 font-semibold">
                    <Calendar className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                    <span className="font-bold text-slate-900 dark:text-white">{m.kickoff_date || m.short_date}</span>
                    <span className="text-slate-400">&bull;</span>
                    <Clock className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                    <span>{isLive ? (m.minute ? (m.minute.includes('Live') ? m.minute : `${m.minute} Live`) : 'Live Now') : isUpcoming ? m.kickoff_time : 'Final Score'}</span>
                  </div>

                  {/* Match Up: Home vs Away */}
                  <div 
                    onClick={() => onSelectMatch({ type: 'match', sport: sportName || 'Football', data: m })}
                    className="cursor-pointer py-3 px-3 bg-slate-50/60 dark:bg-slate-950/40 hover:border-emerald-500/40 dark:hover:border-emerald-500/40 rounded-xl border border-slate-200/70 dark:border-slate-800/70 transition-all duration-200 my-1 group/match"
                  >
                    {isLongScore ? (
                      /* Stacked 2-row layout for cricket / long scores (never overlaps logos or names) */
                      <div className="space-y-2 py-0.5">
                        {/* Home Row */}
                        <div className="flex items-center justify-between gap-2">
                          <div className="flex items-center gap-2.5 min-w-0 flex-1">
                            <div className="w-8 h-8 rounded-lg bg-white dark:bg-slate-900 p-1 flex items-center justify-center shrink-0 border border-slate-200 dark:border-slate-700 shadow-2xs">
                              <img 
                                src={m.home_team?.logo} 
                                alt={m.home_team?.name}
                                onError={(e) => handleLogoError(e, m.home_team?.name)}
                                className="w-full h-full object-contain"
                              />
                            </div>
                            <span className="text-xs font-bold text-slate-900 dark:text-slate-100 truncate group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors">
                              {m.home_team?.name}
                            </span>
                          </div>
                          <div className="font-mono font-black text-xs sm:text-sm text-emerald-700 dark:text-emerald-400 shrink-0 text-right px-2 py-0.5 rounded bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700">
                            {m.home_team?.display_score || m.home_team?.score || (isUpcoming ? 'VS' : '-')}
                          </div>
                        </div>

                        {/* Away Row */}
                        <div className="flex items-center justify-between gap-2">
                          <div className="flex items-center gap-2.5 min-w-0 flex-1">
                            <div className="w-8 h-8 rounded-lg bg-white dark:bg-slate-900 p-1 flex items-center justify-center shrink-0 border border-slate-200 dark:border-slate-700 shadow-2xs">
                              <img 
                                src={m.away_team?.logo} 
                                alt={m.away_team?.name}
                                onError={(e) => handleLogoError(e, m.away_team?.name)}
                                className="w-full h-full object-contain"
                              />
                            </div>
                            <span className="text-xs font-bold text-slate-900 dark:text-slate-100 truncate group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors">
                              {m.away_team?.name}
                            </span>
                          </div>
                          <div className="font-mono font-black text-xs sm:text-sm text-emerald-700 dark:text-emerald-400 shrink-0 text-right px-2 py-0.5 rounded bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700">
                            {m.away_team?.display_score || m.away_team?.score || (isUpcoming ? 'VS' : '-')}
                          </div>
                        </div>
                      </div>
                    ) : (
                      /* Standard 1-row layout for football / short scores */
                      <div className="flex items-center justify-between gap-2">
                        {/* Home Team */}
                        <div className="flex items-center gap-2.5 flex-1 min-w-0">
                          <div className="w-8 h-8 rounded-lg bg-white dark:bg-slate-900 p-1 flex items-center justify-center shrink-0 border border-slate-200 dark:border-slate-700 shadow-2xs">
                            <img 
                              src={m.home_team?.logo} 
                              alt={m.home_team?.name}
                              onError={(e) => handleLogoError(e, m.home_team?.name)}
                              className="w-full h-full object-contain"
                            />
                          </div>
                          <span className="text-xs font-bold text-slate-900 dark:text-slate-100 truncate group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors">
                            {m.home_team?.name}
                          </span>
                        </div>

                        {/* Score or VS Badge */}
                        <div className="px-2.5 py-1 bg-white dark:bg-slate-900 rounded-lg border border-slate-200 dark:border-slate-700 text-center shrink-0 min-w-[54px] shadow-2xs">
                          {isUpcoming ? (
                            <span className="text-[11px] font-black text-sky-700 dark:text-sky-400 tracking-wider uppercase font-mono">
                              VS
                            </span>
                          ) : (
                            <span className="text-xs sm:text-sm font-black text-emerald-700 dark:text-emerald-400 tracking-wider font-mono whitespace-nowrap">
                              {(m.home_team?.display_score || m.home_team?.score) ?? 0} : {(m.away_team?.display_score || m.away_team?.score) ?? 0}
                            </span>
                          )}
                        </div>

                        {/* Away Team */}
                        <div className="flex items-center justify-end gap-2.5 flex-1 min-w-0 text-right">
                          <span className="text-xs font-bold text-slate-900 dark:text-slate-100 truncate group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors">
                            {m.away_team?.name}
                          </span>
                          <div className="w-8 h-8 rounded-lg bg-white dark:bg-slate-900 p-1 flex items-center justify-center shrink-0 border border-slate-200 dark:border-slate-700 shadow-2xs">
                            <img 
                              src={m.away_team?.logo} 
                              alt={m.away_team?.name}
                              onError={(e) => handleLogoError(e, m.away_team?.name)}
                              className="w-full h-full object-contain"
                            />
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Multi-Server / Replay Selector Grid */}
                  <div className="mt-3 space-y-1.5">
                    <span className="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider flex items-center gap-1">
                      {isFinished ? <Video className="w-3 h-3 text-emerald-600 dark:text-emerald-400" /> : <Tv className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />}
                      <span>{isFinished ? 'Video Highlights & Replays:' : 'Broadcast Feeds:'}</span>
                    </span>
                    <div className="grid grid-cols-2 gap-1.5">
                      {streams.slice(0, 4).map((s, sIdx) => (
                        <button
                          key={s.id || sIdx}
                          onClick={() => {
                            const matchCopy = { ...m, defaultServerIndex: sIdx };
                            onSelectMatch({ type: 'match', sport: sportName || 'Football', data: matchCopy });
                          }}
                          className="px-2.5 py-1.5 rounded-lg bg-slate-50 dark:bg-slate-800 hover:bg-emerald-600 hover:text-white dark:hover:bg-emerald-600 text-slate-700 dark:text-slate-300 text-[10px] font-bold border border-slate-200 dark:border-slate-700 transition-all text-left truncate cursor-pointer shadow-2xs flex items-center gap-1"
                          title={s.label}
                        >
                          {isFinished ? (
                            <PlayCircle className="w-3 h-3 shrink-0 text-emerald-500" />
                          ) : (
                            <Tv className="w-3 h-3 shrink-0 text-emerald-500" />
                          )}
                          <span className="truncate">{s.network || `Server ${sIdx + 1}`}</span>
                        </button>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Bottom Action Bar */}
                <div className="mt-4 pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
                  <button
                    onClick={() => onOpenStats && onOpenStats(m)}
                    className="px-3 py-1.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 hover:bg-emerald-50 dark:hover:bg-emerald-950/50 hover:border-emerald-300 dark:hover:border-emerald-700 hover:text-emerald-700 dark:hover:text-emerald-300 text-slate-700 dark:text-slate-300 text-xs font-bold flex items-center gap-1.5 transition-all duration-150 cursor-pointer border border-slate-200/90 dark:border-slate-700"
                    title="Match Statistics"
                  >
                    <BarChart2 className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
                    <span>Stats</span>
                  </button>

                  <button
                    onClick={() => onSelectMatch({ type: 'match', sport: sportName || 'Football', data: m })}
                    className="flex-1 flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs shadow-sm shadow-emerald-600/20 transition-all cursor-pointer group-hover:scale-[1.01]"
                  >
                    {isFinished ? (
                      <>
                        <PlayCircle className="w-3.5 h-3.5 fill-white shrink-0" />
                        <span className="truncate">
                          <span className="sm:hidden">REPLAY</span>
                          <span className="hidden sm:inline">WATCH REPLAY & HIGHLIGHTS</span>
                        </span>
                      </>
                    ) : isLive ? (
                      <>
                        <Play className="w-3.5 h-3.5 fill-white shrink-0" />
                        <span className="truncate">WATCH LIVE</span>
                      </>
                    ) : (
                      <>
                        <Clock className="w-3.5 h-3.5 shrink-0" />
                        <span className="truncate">
                          <span className="sm:hidden">PREVIEW</span>
                          <span className="hidden sm:inline">KICKOFF COUNTDOWN</span>
                        </span>
                      </>
                    )}
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* 15 Per Page Pagination Bar */}
      {totalPages > 1 && (
        <div className="pt-6 pb-2 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-slate-200 dark:border-slate-800">
          <div className="text-xs font-bold text-slate-500 dark:text-slate-400">
            Page <span className="text-slate-900 dark:text-white font-extrabold">{currentPage}</span> of <span className="text-slate-900 dark:text-white font-extrabold">{totalPages}</span> ({sortedMatches.length} matches &bull; 15 per page)
          </div>

          <div className="flex items-center gap-1.5">
            <button
              onClick={() => {
                setCurrentPage((p) => Math.max(1, p - 1));
                window.scrollTo({ top: 350, behavior: 'smooth' });
              }}
              disabled={currentPage === 1}
              className="p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed transition-colors cursor-pointer"
              title="Previous Page"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>

            {/* Page number buttons */}
            {Array.from({ length: totalPages }, (_, i) => i + 1)
              .filter((p) => p === 1 || p === totalPages || Math.abs(p - currentPage) <= 1)
              .map((p, idx, arr) => {
                const prev = arr[idx - 1];
                return (
                  <React.Fragment key={p}>
                    {prev && p - prev > 1 && (
                      <span className="px-1.5 text-xs text-slate-400 font-bold">...</span>
                    )}
                    <button
                      onClick={() => {
                        setCurrentPage(p);
                        window.scrollTo({ top: 350, behavior: 'smooth' });
                      }}
                      className={`w-8 h-8 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                        currentPage === p
                          ? 'bg-emerald-600 text-white shadow-xs font-black'
                          : 'border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300'
                      }`}
                    >
                      {p}
                    </button>
                  </React.Fragment>
                );
              })}

            <button
              onClick={() => {
                setCurrentPage((p) => Math.min(totalPages, p + 1));
                window.scrollTo({ top: 350, behavior: 'smooth' });
              }}
              disabled={currentPage === totalPages}
              className="p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 disabled:opacity-40 disabled:cursor-not-allowed transition-colors cursor-pointer"
              title="Next Page"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}
    </section>
  );
}
