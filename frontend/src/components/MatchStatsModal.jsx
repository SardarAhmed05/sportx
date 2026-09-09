import React from 'react';
import { X, Play, Trophy, Shield, Activity, BarChart2, MapPin, Calendar, Clock, Video } from 'lucide-react';

export default function MatchStatsModal({ match, onClose, onWatchMatch }) {
  if (!match) return null;
  const isFinished = match.status === 'FINISHED' || match.status === 'FT';

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="relative w-full max-w-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl shadow-2xl overflow-hidden my-8 text-slate-900 dark:text-slate-100">
        {/* Modal Header */}
        <div className="p-5 bg-slate-50 dark:bg-slate-850 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <span className="p-2 rounded-xl bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400 text-base">
              <Trophy className="w-5 h-5" />
            </span>
            <div>
              <h3 className="text-base sm:text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                {match.league}
                <span className={`text-xs font-bold px-2 py-0.5 rounded-full ${
                  isFinished ? 'bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-300' : 'bg-red-100 dark:bg-red-950/60 text-red-700 dark:text-red-300 border border-red-200 dark:border-red-900'
                }`}>
                  {match.minute || 'LIVE'}
                </span>
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-2 mt-0.5">
                <Calendar className="w-3 h-3 text-slate-400" />
                <span>{match.kickoff_date || match.formatted_date_time}</span>
                <span>&bull;</span>
                <MapPin className="w-3 h-3 text-slate-400" />
                <span>{match.stadium}</span>
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-full bg-white dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-slate-500 dark:text-slate-400 hover:text-rose-600 dark:hover:text-rose-300 border border-slate-200 dark:border-slate-700 transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-6 max-h-[70vh] overflow-y-auto">
          {/* Score Header */}
          <div className="flex items-center justify-between p-4 rounded-2xl bg-slate-50 dark:bg-slate-850 border border-slate-200 dark:border-slate-800 text-center">
            <div className="flex-1">
              <div className="w-12 h-12 mx-auto rounded-xl bg-white dark:bg-slate-900 flex items-center justify-center p-1.5 mb-1 border border-slate-200 dark:border-slate-700 shadow-2xs">
                <img 
                  src={match.home_team?.logo} 
                  alt={match.home_team?.name}
                  className="w-full h-full object-contain"
                />
              </div>
              <h4 className="text-xs font-bold text-slate-900 dark:text-slate-100">{match.home_team?.name}</h4>
            </div>

            <div className="px-4">
              <div className="text-3xl font-black text-emerald-700 dark:text-emerald-400 tracking-wider font-mono">
                {match.home_team?.score ?? 0} : {match.away_team?.score ?? 0}
              </div>
              <div className="text-[11px] font-bold text-slate-600 dark:text-slate-400 mt-1">
                {isFinished ? 'Full Time' : match.minute}
              </div>
            </div>

            <div className="flex-1">
              <div className="w-12 h-12 mx-auto rounded-xl bg-white dark:bg-slate-900 flex items-center justify-center p-1.5 mb-1 border border-slate-200 dark:border-slate-700 shadow-2xs">
                <img 
                  src={match.away_team?.logo} 
                  alt={match.away_team?.name}
                  className="w-full h-full object-contain"
                />
              </div>
              <h4 className="text-xs font-bold text-slate-900 dark:text-slate-100">{match.away_team?.name}</h4>
            </div>
          </div>

          {/* Football Detailed Stats Comparison */}
          <div className="space-y-3">
            <h4 className="text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
              <BarChart2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
              Match Statistics
            </h4>

            <div className="space-y-3 bg-slate-50 dark:bg-slate-850 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 text-xs">
              {/* Possession */}
              <div>
                <div className="flex justify-between text-slate-700 dark:text-slate-300 font-bold mb-1">
                  <span>{match.possession?.home || 52}%</span>
                  <span className="text-slate-500 dark:text-slate-400">Ball Possession</span>
                  <span>{match.possession?.away || 48}%</span>
                </div>
                <div className="w-full h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden flex">
                  <div className="bg-emerald-600 h-full" style={{ width: `${match.possession?.home || 52}%` }}></div>
                  <div className="bg-sky-500 h-full" style={{ width: `${match.possession?.away || 48}%` }}></div>
                </div>
              </div>

              {/* Shots on Target */}
              <div className="flex justify-between py-1 border-b border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-semibold">
                <span>{match.shots_on_target?.home || 5}</span>
                <span className="text-slate-500 dark:text-slate-400">Shots on Target</span>
                <span>{match.shots_on_target?.away || 3}</span>
              </div>

              {/* Total Shots */}
              <div className="flex justify-between py-1 border-b border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-semibold">
                <span>{match.total_shots?.home || 12}</span>
                <span className="text-slate-500 dark:text-slate-400">Total Shots</span>
                <span>{match.total_shots?.away || 9}</span>
              </div>

              {/* Corner Kicks */}
              <div className="flex justify-between py-1 border-b border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-semibold">
                <span>{match.corners?.home || 6}</span>
                <span className="text-slate-500 dark:text-slate-400">Corner Kicks</span>
                <span>{match.corners?.away || 4}</span>
              </div>

              {/* Fouls */}
              <div className="flex justify-between py-1 text-slate-700 dark:text-slate-300 font-semibold">
                <span>{match.fouls?.home || 8}</span>
                <span className="text-slate-500 dark:text-slate-400">Fouls</span>
                <span>{match.fouls?.away || 11}</span>
              </div>
            </div>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="p-4 bg-slate-50 dark:bg-slate-850 border-t border-slate-200 dark:border-slate-800 flex items-center justify-end gap-3">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl bg-white dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold border border-slate-200 dark:border-slate-700 cursor-pointer"
          >
            Close
          </button>
          <button
            onClick={() => {
              onWatchMatch({ type: 'match', sport: match.sport || 'Football', data: match });
              onClose();
            }}
            className="flex items-center gap-1.5 px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-black shadow-sm shadow-emerald-600/20 cursor-pointer"
          >
            {isFinished ? <Video className="w-3.5 h-3.5 fill-white" /> : <Play className="w-3.5 h-3.5 fill-white" />}
            <span>{isFinished ? 'Watch Highlights & Replay' : 'Launch Live Stream'}</span>
          </button>
        </div>
      </div>
    </div>
  );
}
