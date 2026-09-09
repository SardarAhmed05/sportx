import React from 'react';

export default function Footer({ totalLiveStreams = 15 }) {
  return (
    <footer className="mt-16 border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 py-8 text-xs text-slate-500 dark:text-slate-400 transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-black text-slate-900 dark:text-white tracking-tight">SPORT<span className="text-emerald-500">X</span> LIVE</span>
          <span>&bull;</span>
          <span>Worldwide Live Football Streaming & Match Center</span>
          <span>&bull;</span>
          <span className="text-emerald-700 dark:text-emerald-400 font-bold">{totalLiveStreams} Live Event Feeds</span>
        </div>
        <p className="text-[11px] text-slate-500 dark:text-slate-400">
          Premier League &bull; Champions League &bull; La Liga &bull; Serie A &bull; Bundesliga &bull; Ligue 1 &bull; 24/7 Global TV
        </p>
      </div>
    </footer>
  );
}
