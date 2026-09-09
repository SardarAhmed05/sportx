import React from 'react';
import { Calendar, Clock, Activity } from 'lucide-react';

export default function LiveTicker({ matches = [], onSelectMatch }) {
  if (!matches || matches.length === 0) return null;

  return (
    <div className="bg-slate-100 border-b border-slate-200/80 py-1.5 px-4 overflow-hidden text-xs">
      <div className="max-w-7xl mx-auto flex items-center gap-3">
        <div className="flex items-center gap-1.5 text-[10px] font-black uppercase text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded-md border border-emerald-200 shrink-0">
          <span className="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></span>
          <span>SCORE TICKER</span>
        </div>

        <div className="flex items-center gap-2.5 overflow-x-auto scrollbar-none py-0.5 text-slate-700">
          {matches.slice(0, 25).map((m) => {
            const isLive = m.status === 'LIVE';
            const isUpcoming = m.status === 'UPCOMING' || m.status === 'SCHEDULED';
            return (
              <div
                key={m.id}
                onClick={() => onSelectMatch({ type: 'match', sport: 'Football', data: m })}
                className="flex items-center gap-2 px-2.5 py-1 rounded-lg bg-white hover:bg-emerald-50 border border-slate-200/90 shadow-2xs cursor-pointer transition-all shrink-0 group"
              >
                <img 
                  src={m.home_team?.logo} 
                  alt={m.home_team?.name}
                  className="w-4 h-4 object-contain shrink-0"
                />
                <span className="text-[11px] font-bold text-slate-900 group-hover:text-emerald-700 transition-colors">
                  {m.home_team?.short_name || m.home_team?.name}
                </span>

                {isUpcoming ? (
                  <span className="text-[10px] font-black text-sky-700 px-1 py-0.2 bg-sky-50 rounded border border-sky-200 font-mono">
                    VS
                  </span>
                ) : (
                  <span className="text-[11px] font-black text-emerald-700 font-mono">
                    {m.home_team?.score ?? 0} - {m.away_team?.score ?? 0}
                  </span>
                )}

                <span className="text-[11px] font-bold text-slate-900 group-hover:text-emerald-700 transition-colors">
                  {m.away_team?.short_name || m.away_team?.name}
                </span>
                <img 
                  src={m.away_team?.logo} 
                  alt={m.away_team?.name}
                  className="w-4 h-4 object-contain shrink-0"
                />

                <span className={`text-[9px] font-bold px-1.5 py-0.2 rounded-full uppercase ${
                  isLive 
                    ? 'bg-red-100 text-red-700 border border-red-200 font-black' 
                    : isUpcoming
                    ? 'bg-sky-100 text-sky-800'
                    : 'bg-slate-100 text-slate-600'
                }`}>
                  {isLive ? m.minute : (m.short_date || 'SCHED')}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
