import React, { useState, useMemo, useEffect } from 'react';
import { 
  PlayCircle, 
  Trophy, 
  Calendar, 
  Search, 
  Sparkles, 
  Video, 
  Clock, 
  Filter,
  Tv,
  Info,
  Layers,
  ChevronDown
} from 'lucide-react';

export default function FootballReplaysSection({ 
  replays = [], 
  onSelectReplay,
  searchQuery = '',
  setSearchQuery,
  categories = [],
  sportName = 'Football'
}) {
  const [selectedCategory, setSelectedCategory] = useState('recent');
  const [localSearch, setLocalSearch] = useState('');
  const [visibleCount, setVisibleCount] = useState(12);

  const DEFAULT_CATEGORIES = [
    { id: 'recent', label: 'Recent Matches' },
    { id: 'cult_classics', label: 'Greatest Cult Classics (Top 10)', isSpecial: true },
    { id: 'all', label: 'All Replays & Classics' },
    { id: 'premier_league', label: 'Premier League' },
    { id: 'champions_league', label: 'Champions League' },
    { id: 'world_cup', label: 'FIFA World Cup' },
    { id: 'euro_copa', label: 'Euro & Copa' },
    { id: 'el_clasico', label: 'El Clásico' },
  ];

  const activeCategories = (categories && categories.length > 0)
    ? categories.map(c => ({ ...c, isSpecial: c.id === 'cult_classics' }))
    : DEFAULT_CATEGORIES;

  // Reset category when sport changes
  useEffect(() => {
    setSelectedCategory('recent');
    setVisibleCount(12);
  }, [sportName]);

  // Reset pagination when category or search changes
  useEffect(() => {
    setVisibleCount(12);
  }, [selectedCategory, localSearch, searchQuery]);

  const filteredReplays = useMemo(() => {
    return replays.filter(item => {
      // Category filter
      if (selectedCategory !== 'all') {
        if (selectedCategory === 'cult_classics') {
          if (!item.is_cult_classic) return false;
        } else {
          const hasCategory = 
            item.category === selectedCategory ||
            (Array.isArray(item.categories) && item.categories.includes(selectedCategory));
          if (!hasCategory) return false;
        }
      }
      // Search filter (combining global search and local search)
      const q = (localSearch || searchQuery || '').trim().toLowerCase();
      if (!q) return true;

      return (
        item.title?.toLowerCase().includes(q) ||
        item.competition?.toLowerCase().includes(q) ||
        item.description?.toLowerCase().includes(q) ||
        item.home_team?.name?.toLowerCase().includes(q) ||
        item.away_team?.name?.toLowerCase().includes(q) ||
        item.cult_badge?.toLowerCase().includes(q) ||
        String(item.year || '').includes(q)
      );
    });
  }, [replays, selectedCategory, localSearch, searchQuery]);

  const displayedReplays = filteredReplays.slice(0, visibleCount);
  const hasMore = filteredReplays.length > visibleCount;

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 shadow-sm transition-colors">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-2xl bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800 flex items-center justify-center text-emerald-600 dark:text-emerald-400 shrink-0">
              <Trophy className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg sm:text-xl font-black text-slate-900 dark:text-slate-100 tracking-tight">
                  {sportName || 'Football'} Replays & Classics Vault
                </h2>
                <span className="px-2.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 text-[10px] font-black uppercase tracking-wider border border-emerald-200 dark:border-emerald-800">
                  Official Vault
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Official full match replays, historic tournament finals, and extended video archives
              </p>
            </div>
          </div>

          {/* Quick Search */}
          <div className="relative w-full sm:w-64">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={localSearch}
              onChange={(e) => setLocalSearch(e.target.value)}
              placeholder={`Search ${sportName || 'classics'} (e.g. ${sportName === 'Basketball' ? 'Jordan, LeBron, 2016' : sportName === 'Motorsport' ? 'Hamilton, Abu Dhabi, 2021' : '2022, Messi, Istanbul'})...`}
              className="w-full pl-9 pr-3 py-2 text-xs rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
            />
          </div>
        </div>

        {/* Category Pills */}
        <div className="flex items-center gap-2 overflow-x-auto pt-4 mt-4 border-t border-slate-100 dark:border-slate-800 no-scrollbar">
          {activeCategories.map(cat => (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1.5 ${
                selectedCategory === cat.id
                  ? cat.isSpecial 
                    ? 'bg-amber-500 text-slate-950 shadow-md shadow-amber-500/20 font-black'
                    : 'bg-emerald-600 text-white shadow-sm shadow-emerald-600/20'
                  : cat.isSpecial
                    ? 'bg-amber-500/10 dark:bg-amber-500/15 border border-amber-500/30 text-amber-900 dark:text-amber-300 hover:bg-amber-500/20'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-slate-750'
              }`}
            >
              {cat.isSpecial && <Sparkles className="w-3.5 h-3.5 text-amber-500 fill-amber-500" />}
              <span>{cat.label}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Grid of Replay Cards */}
      {filteredReplays.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-12 text-center space-y-3">
          <Video className="w-10 h-10 text-slate-400 mx-auto" />
          <p className="text-sm font-bold text-slate-700 dark:text-slate-300">No classic replays found</p>
          <p className="text-xs text-slate-500 dark:text-slate-400">Try adjusting your category filter or search query</p>
        </div>
      ) : (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {displayedReplays.map((item) => (
              <div
                key={item.id}
                className="group bg-white dark:bg-slate-900 border border-slate-200/90 dark:border-slate-800 rounded-3xl overflow-hidden shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col justify-between"
              >
                <div>
                  {/* Thumbnail Poster with Badges & Play Button */}
                  <div 
                    onClick={() => onSelectReplay({ type: 'match', sport: sportName || 'Football', data: item })}
                    className="relative aspect-video w-full bg-slate-950 overflow-hidden cursor-pointer"
                  >
                    <img
                      src={item.thumbnail}
                      alt={item.title}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-90 group-hover:opacity-100"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-black/30"></div>

                    {/* Top Badges */}
                    <div className="absolute top-3 left-3 right-3 flex items-center justify-between pointer-events-none gap-2">
                      <span className="px-2.5 py-1 rounded-lg bg-black/70 backdrop-blur-md text-white text-[10px] font-black uppercase tracking-wider border border-white/10 flex items-center gap-1.5 truncate">
                        {item.is_cult_classic ? (
                          <Sparkles className="w-3.5 h-3.5 text-amber-400 shrink-0 fill-amber-400" />
                        ) : (
                          <Trophy className="w-3 h-3 text-amber-400 shrink-0" />
                        )}
                        <span className="truncate">{item.cult_badge || item.competition}</span>
                      </span>

                      <span className={`px-2.5 py-1 rounded-lg text-white text-[10px] font-bold shadow-xs shrink-0 ${
                        item.is_cult_classic ? 'bg-amber-600/95 font-black text-amber-100' : 'bg-emerald-600/90'
                      }`}>
                        {item.is_cult_classic ? `#${item.cult_rank} Classic` : item.year}
                      </span>
                    </div>

                    {/* Center Play Button Overlay */}
                    <div className="absolute inset-0 flex items-center justify-center opacity-80 group-hover:opacity-100 transition-opacity">
                      <div className="w-12 h-12 rounded-full bg-emerald-600 text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                        <PlayCircle className="w-7 h-7 fill-white text-emerald-600" />
                      </div>
                    </div>

                    {/* Bottom Duration Badge */}
                    <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between text-white text-[11px] font-semibold">
                      <span className="flex items-center gap-1 bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-md">
                        <Clock className="w-3 h-3 text-emerald-400" />
                        <span>{item.duration || 'Full Match'}</span>
                      </span>
                      <span className="font-mono font-bold bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-md text-amber-300">
                        {item.score}
                      </span>
                    </div>
                  </div>

                  {/* Match Information */}
                  <div className="p-4 sm:p-5 space-y-3">
                    {/* Teams Scoreboard Bar */}
                    <div className="flex items-center justify-between bg-slate-50 dark:bg-slate-800/60 p-2.5 rounded-2xl border border-slate-100 dark:border-slate-800">
                      <div className="flex items-center gap-2 min-w-0">
                        <img src={item.home_team?.logo} alt={item.home_team?.name} className="w-6 h-6 object-contain shrink-0" />
                        <span className="text-xs font-bold text-slate-800 dark:text-slate-200 truncate">{item.home_team?.name}</span>
                      </div>
                      
                      <span className="text-xs font-mono font-black text-emerald-600 dark:text-emerald-400 px-2 py-0.5 rounded-md bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 shadow-2xs">
                        {item.score}
                      </span>

                      <div className="flex items-center gap-2 justify-end min-w-0">
                        <span className="text-xs font-bold text-slate-800 dark:text-slate-200 truncate">{item.away_team?.name}</span>
                        <img src={item.away_team?.logo} alt={item.away_team?.name} className="w-6 h-6 object-contain shrink-0" />
                      </div>
                    </div>

                    {/* Title & Description */}
                    <div>
                      <h3 className="text-sm font-black text-slate-900 dark:text-slate-100 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors line-clamp-1">
                        {item.title}
                      </h3>
                      <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 line-clamp-2 leading-relaxed">
                        {item.description}
                      </p>
                    </div>

                    {/* Available Feeds */}
                    <div className="space-y-1 pt-1">
                      <span className="text-[10px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider flex items-center gap-1">
                        <Tv className="w-3 h-3 text-emerald-500" />
                        <span>{item.streams?.length || 2} Official Broadcast Feeds</span>
                      </span>
                      <div className="flex flex-wrap gap-1.5">
                        {(item.streams || []).map((s, idx) => (
                          <span 
                            key={s.id || idx}
                            className="px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800 text-[10px] font-semibold text-slate-600 dark:text-slate-300"
                          >
                            {s.network || `Server ${idx + 1}`}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>

                {/* Bottom CTA Action Button */}
                <div className="p-4 sm:p-5 pt-0">
                  <button
                    onClick={() => onSelectReplay({ type: 'match', sport: sportName || 'Football', data: item })}
                    className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-black shadow-md shadow-emerald-600/20 transition-all cursor-pointer group-hover:scale-[1.01]"
                  >
                    <PlayCircle className="w-4 h-4 fill-white text-emerald-600" />
                    <span>WATCH FULL REPLAY</span>
                  </button>
                </div>
              </div>
            ))}
          </div>

          {/* Load More Pagination Button */}
          {hasMore && (
            <div className="flex justify-center pt-2 pb-2">
              <button
                onClick={() => setVisibleCount(prev => prev + 12)}
                className="px-6 py-2.5 rounded-2xl bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700 text-xs font-bold transition-all shadow-xs hover:shadow-md cursor-pointer flex items-center gap-2"
              >
                <ChevronDown className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                <span>Show More Matches ({filteredReplays.length - visibleCount} remaining)</span>
              </button>
            </div>
          )}
        </div>
      )}

      {/* Professional Archive & Indexing Notice */}
      <div className="bg-slate-50 dark:bg-slate-900/60 border border-slate-200/90 dark:border-slate-800 rounded-3xl p-5 sm:p-6 transition-colors">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-start sm:items-center gap-3.5">
            <div className="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-950/50 border border-amber-200 dark:border-amber-800/60 flex items-center justify-center text-amber-600 dark:text-amber-400 shrink-0 mt-0.5 sm:mt-0">
              <Info className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                <span>Classics Vault Status & Coverage Notice</span>
                <span className="px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 text-[10px] font-semibold border border-amber-200 dark:border-amber-800">
                  Curated Archive
                </span>
              </h4>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 max-w-2xl leading-relaxed">
                Please note: The Classics Vault is currently in active development with a curated selection of verified classic encounters and recent tournament fixtures. Additional archived matches are continuously indexed.
              </p>
            </div>
          </div>
          <div className="text-xs font-semibold text-slate-400 dark:text-slate-500 shrink-0 self-end sm:self-center">
            Selected Matches Only
          </div>
        </div>
      </div>
    </div>
  );
}
