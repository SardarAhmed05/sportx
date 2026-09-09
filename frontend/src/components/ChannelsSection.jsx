import React, { useState } from 'react';
import { 
  Tv, 
  Play, 
  Globe, 
  Search, 
  Radio,
  Sparkles,
  ArrowDownAZ
} from 'lucide-react';

export default function ChannelsSection({ 
  channels = [], 
  categories = [], 
  countries = [], 
  onSelectChannel,
  sportName = 'Football'
}) {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedCountry, setSelectedCountry] = useState('ALL');
  const [channelSearch, setChannelSearch] = useState('');
  const [sortBy, setSortBy] = useState('popular'); // 'popular' | 'alpha'

  const filteredChannels = channels.filter(ch => {
    if (selectedCategory !== 'all') {
      const matchSport = ch.sport?.toLowerCase() === selectedCategory.toLowerCase() ||
                         ch.category?.toLowerCase().includes(selectedCategory.toLowerCase());
      if (!matchSport) return false;
    }

    if (selectedCountry !== 'ALL') {
      if (ch.country_code !== selectedCountry) return false;
    }

    if (channelSearch) {
      const q = channelSearch.toLowerCase();
      const matchQuery = ch.name?.toLowerCase().includes(q) ||
                         ch.sport?.toLowerCase().includes(q) ||
                         ch.description?.toLowerCase().includes(q);
      if (!matchQuery) return false;
    }

    return true;
  });

  // Sort channels by popularity (featured & viewers) or alphabetically (A to Z)
  const sortedChannels = [...filteredChannels].sort((a, b) => {
    if (sortBy === 'alpha') {
      return (a.name || '').localeCompare(b.name || '');
    }
    // Default: 'popular'
    if (a.featured && !b.featured) return -1;
    if (!a.featured && b.featured) return 1;
    return (b.viewers || 0) - (a.viewers || 0);
  });

  return (
    <section className="space-y-4">
      {/* Header & Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 dark:border-slate-800 pb-3">
        <div>
          <h3 className="text-base font-black text-slate-900 dark:text-white flex items-center gap-2">
            <Radio className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            <span>24/7 Global {sportName || 'Sports'} TV Channels</span>
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">Live 24/7 Official {sportName || 'Sports'} Broadcast Networks</p>
        </div>

        {/* Filters & Sorting Toggle */}
        <div className="flex flex-wrap items-center gap-2">
          {/* Popularity vs Alphabetical Order Toggle */}
          <div className="flex items-center p-0.5 bg-slate-100 dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 shadow-2xs text-xs">
            <button
              onClick={() => setSortBy('popular')}
              className={`px-2.5 py-1.5 rounded-lg font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
                sortBy === 'popular'
                  ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
              title="Sort by Popularity (Marquee Networks First)"
            >
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              <span className="hidden sm:inline">Popular First</span>
              <span className="sm:hidden">Popular</span>
            </button>
            <button
              onClick={() => setSortBy('alpha')}
              className={`px-2.5 py-1.5 rounded-lg font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
                sortBy === 'alpha'
                  ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
              title="Sort Alphabetically (A to Z)"
            >
              <ArrowDownAZ className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
              <span className="hidden sm:inline">A-Z Order</span>
              <span className="sm:hidden">A-Z</span>
            </button>
          </div>

          <div className="flex items-center gap-1.5 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl px-2.5 py-1.5 text-xs text-slate-700 dark:text-slate-300 shadow-2xs">
            <Globe className="w-3.5 h-3.5 text-slate-400" />
            <select
              value={selectedCountry}
              onChange={(e) => setSelectedCountry(e.target.value)}
              className="bg-transparent text-slate-900 dark:text-slate-100 focus:outline-none cursor-pointer text-xs font-bold"
            >
              {countries.map((c) => (
                <option key={c.code} value={c.code} className="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">
                  {c.name}
                </option>
              ))}
            </select>
          </div>

          <div className="relative">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Filter channel..."
              value={channelSearch}
              onChange={(e) => setChannelSearch(e.target.value)}
              className="pl-8 pr-3 py-1.5 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-emerald-500 shadow-2xs"
            />
          </div>
        </div>
      </div>

      {/* Sport Category Filter */}
      <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
        <button
          onClick={() => setSelectedCategory('all')}
          className={`px-3 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer whitespace-nowrap ${
            selectedCategory === 'all'
              ? 'bg-slate-900 dark:bg-emerald-600 text-white font-extrabold shadow-xs'
              : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white border border-slate-200 dark:border-slate-800 shadow-2xs'
          }`}
        >
          All Networks ({channels.length})
        </button>
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className={`px-3 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer whitespace-nowrap ${
              selectedCategory === cat.id
                ? 'bg-slate-900 dark:bg-emerald-600 text-white font-extrabold shadow-xs'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white border border-slate-200 dark:border-slate-800 shadow-2xs'
            }`}
          >
            {cat.name}
          </button>
        ))}
      </div>

      {/* Channels Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {sortedChannels.map((ch) => (
          <div
            key={ch.id}
            className="bg-white dark:bg-slate-900 border border-slate-200/90 dark:border-slate-800 hover:border-emerald-500/60 dark:hover:border-emerald-500/60 rounded-2xl p-4 transition-all duration-200 flex flex-col justify-between group shadow-2xs hover:shadow-xl hover:shadow-emerald-500/5 dark:hover:shadow-emerald-950/30 hover:-translate-y-0.5"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2.5">
                <span className="text-[10px] font-black px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                  {ch.country || 'Global'}
                </span>
                <span className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/80 text-emerald-800 dark:text-emerald-300 text-[10px] font-black uppercase">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 animate-pulse"></span>
                  24/7 ON AIR
                </span>
              </div>

              <div className="flex items-center gap-3 my-2">
                <div className="w-11 h-11 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center text-slate-800 dark:text-slate-200 shrink-0 shadow-2xs">
                  <Tv className="w-5 h-5 text-slate-700 dark:text-slate-300" />
                </div>
                <div className="min-w-0">
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 truncate group-hover:text-emerald-700 dark:group-hover:text-emerald-400 transition-colors">
                    {ch.name}
                  </h4>
                  <p className="text-xs text-slate-500 dark:text-slate-400 truncate">{ch.category || `Live ${sportName || 'Sports'} Network`}</p>
                </div>
              </div>
            </div>

            <div className="mt-4 pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-2">
              <span className="text-[11px] font-bold text-slate-500 dark:text-slate-400">{ch.quality || '1080p HD'}</span>
              <button
                onClick={() => onSelectChannel({ type: 'channel', sport: sportName || 'Football', data: ch })}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all cursor-pointer shadow-sm shadow-emerald-600/20"
              >
                <Play className="w-3.5 h-3.5 fill-white" />
                <span>Watch Channel</span>
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
