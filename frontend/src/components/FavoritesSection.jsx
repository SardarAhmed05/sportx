import React from 'react';
import { Star, Play, Trash2, Tv, Calendar } from 'lucide-react';

export default function FavoritesSection({ favorites = [], onSelectFavorite, onRemoveFavorite }) {
  if (favorites.length === 0) {
    return (
      <div className="p-12 text-center bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm">
        <Star className="w-12 h-12 text-slate-300 dark:text-slate-700 mx-auto mb-3" />
        <h3 className="text-base font-bold text-slate-800 dark:text-slate-200 mb-1">No Saved Favorites Yet</h3>
        <p className="text-xs text-slate-500 dark:text-slate-400 max-w-sm mx-auto">
          Click the star icon on any match or sports TV channel to add it to your quick-access favorites list.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
        <div>
          <h2 className="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
            <Star className="w-5 h-5 text-rose-500 fill-rose-500" />
            <span>My Bookmarked Streams ({favorites.length})</span>
          </h2>
          <p className="text-xs text-slate-500 dark:text-slate-400">Your pinned live matches and channels</p>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {favorites.map((fav, idx) => {
          const isMatch = fav.type === 'match';
          const title = isMatch
            ? `${fav.data?.home_team?.name} vs ${fav.data?.away_team?.name}`
            : fav.data?.name;

          return (
            <div
              key={idx}
              className="bg-white dark:bg-slate-900 rounded-2xl p-4 border border-slate-200 dark:border-slate-800 hover:border-rose-300 dark:hover:border-rose-800 transition-all flex flex-col justify-between shadow-sm hover:shadow-md"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                    {fav.data?.league || 'Football'}
                  </span>
                  <button
                    onClick={() => onRemoveFavorite(fav)}
                    className="p-1 text-slate-400 hover:text-rose-600 dark:hover:text-rose-400 transition-colors cursor-pointer"
                    title="Remove favorite"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>

                <div className="flex items-center gap-3 my-2">
                  <div className="w-10 h-10 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center shrink-0">
                    {isMatch ? <Calendar className="w-5 h-5 text-slate-700 dark:text-slate-300" /> : <Tv className="w-5 h-5 text-slate-700 dark:text-slate-300" />}
                  </div>
                  <div className="min-w-0">
                    <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 truncate">{title}</h4>
                    <p className="text-xs text-slate-500 dark:text-slate-400 truncate">{fav.data?.kickoff_date || fav.data?.category}</p>
                  </div>
                </div>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-200 dark:border-slate-800 flex items-center justify-end">
                <button
                  onClick={() => onSelectFavorite(fav)}
                  className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all cursor-pointer shadow-sm shadow-emerald-600/20"
                >
                  <Play className="w-3.5 h-3.5 fill-white" />
                  <span>Watch Stream</span>
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
