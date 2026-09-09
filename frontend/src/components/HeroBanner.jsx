import React from 'react';
import { Play, Flame, Users, Sparkles, Shield, Trophy } from 'lucide-react';

export default function HeroBanner({ marqueeMatch, onWatchMatch, onOpenStats }) {
  if (!marqueeMatch) return null;

  const isFootball = marqueeMatch.id?.startsWith('fb-') || marqueeMatch.home_team !== undefined;
  const isCricket = marqueeMatch.id?.startsWith('cric-') || marqueeMatch.team_1 !== undefined;

  return (
    <div className="relative overflow-hidden rounded-2xl border border-slate-700/60 bg-gradient-to-r from-slate-900 via-slate-900/90 to-emerald-950/40 p-6 md:p-8 shadow-2xl glow-football">
      {/* Background visual accents */}
      <div className="absolute -right-16 -top-16 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -left-16 -bottom-16 w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 flex flex-col lg:flex-row items-center justify-between gap-8">
        {/* Left match info & headline */}
        <div className="flex-1 space-y-4 text-center lg:text-left">
          <div className="flex flex-wrap items-center justify-center lg:justify-start gap-2.5">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-500/20 text-red-400 text-xs font-black uppercase tracking-wider border border-red-500/30">
              <span className="w-2 h-2 rounded-full bg-red-500 animate-live-dot"></span>
              MARQUEE MATCH &bull; {marqueeMatch.minute || 'LIVE NOW'}
            </span>
            <span className="px-3 py-1 rounded-full bg-emerald-500/15 text-emerald-300 text-xs font-bold border border-emerald-500/30">
              ⚽ {marqueeMatch.league || 'Premier League'}
            </span>
            <span className="px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 text-xs font-medium flex items-center gap-1.5">
              <Users className="w-3.5 h-3.5 text-emerald-400" />
              {(marqueeMatch.viewers_count || 480000).toLocaleString()} Watching
            </span>
          </div>

          <h1 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white tracking-tight leading-tight">
            {isFootball ? (
              <>
                <span className="text-emerald-400">{marqueeMatch.home_team?.name}</span> vs{' '}
                <span className="text-cyan-400">{marqueeMatch.away_team?.name}</span>
              </>
            ) : (
              <>
                <span className="text-amber-400">{marqueeMatch.team_1?.name}</span> vs{' '}
                <span className="text-cyan-400">{marqueeMatch.team_2?.name}</span>
              </>
            )}
          </h1>

          <p className="text-slate-300 text-sm max-w-xl">
            {marqueeMatch.stadium || marqueeMatch.venue} &bull; Streamed in Full HD 1080p 60fps with Multi-Language Audio & Real-time Ball Tracker.
          </p>

          {/* Action buttons */}
          <div className="flex flex-wrap items-center justify-center lg:justify-start gap-3 pt-2">
            <button
              onClick={() => onWatchMatch({ type: 'match', sport: 'Football', data: marqueeMatch })}
              className="flex items-center gap-2.5 px-6 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm shadow-lg shadow-emerald-500/30 hover:scale-[1.02] active:scale-[0.98] transition-all cursor-pointer"
            >
              <Play className="w-4 h-4 fill-slate-950" />
              <span>WATCH LIVE STREAM (HD)</span>
            </button>

            {onOpenStats && (
              <button
                onClick={() => onOpenStats(marqueeMatch)}
                className="px-5 py-3.5 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 text-white text-sm font-bold border border-slate-600/50 hover:border-emerald-500/50 transition-all cursor-pointer"
              >
                Match Center & Stats
              </button>
            )}
          </div>
        </div>

        {/* Right side live scoreboard preview card */}
        <div className="w-full lg:w-auto shrink-0">
          <div className="glass-card rounded-2xl p-6 border border-emerald-500/30 shadow-2xl bg-slate-900/90 text-center min-w-[280px] sm:min-w-[340px]">
            <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-3">
              {marqueeMatch.round || 'Live Score'}
            </div>

            {isFootball && (
              <div className="flex items-center justify-between gap-6 py-2">
                <div className="flex flex-col items-center flex-1">
                  <div className="w-14 h-14 rounded-full bg-slate-800 border-2 border-emerald-500/40 flex items-center justify-center text-xl font-bold text-white shadow-md overflow-hidden mb-2">
                    {marqueeMatch.home_team?.short_name || 'ARS'}
                  </div>
                  <span className="text-xs font-bold text-white truncate max-w-[100px]">
                    {marqueeMatch.home_team?.name}
                  </span>
                </div>

                <div className="flex flex-col items-center">
                  <div className="text-3xl sm:text-4xl font-black text-emerald-400 tracking-wider">
                    {marqueeMatch.home_team?.score} : {marqueeMatch.away_team?.score}
                  </div>
                  <span className="text-[11px] font-bold text-red-400 bg-red-950/60 px-2 py-0.5 rounded-full mt-1 border border-red-800/50">
                    {marqueeMatch.minute || 'LIVE'}
                  </span>
                </div>

                <div className="flex flex-col items-center flex-1">
                  <div className="w-14 h-14 rounded-full bg-slate-800 border-2 border-cyan-500/40 flex items-center justify-center text-xl font-bold text-white shadow-md overflow-hidden mb-2">
                    {marqueeMatch.away_team?.short_name || 'MCI'}
                  </div>
                  <span className="text-xs font-bold text-white truncate max-w-[100px]">
                    {marqueeMatch.away_team?.name}
                  </span>
                </div>
              </div>
            )}

            <div className="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
              <span className="flex items-center gap-1 text-emerald-400">
                <Sparkles className="w-3.5 h-3.5" /> 3 Live Mirrors
              </span>
              <span className="text-slate-300">Ultra-Low Latency</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
