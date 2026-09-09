import React, { useState } from 'react';
import VideoPlayer from './VideoPlayer';
import { Layers, Plus, X, Tv, Radio } from 'lucide-react';

export default function MultiViewPlayer({ 
  stream1, 
  stream2, 
  allAvailableStreams = [], 
  onUpdateStream1, 
  onUpdateStream2, 
  onClose 
}) {
  const [showSelector1, setShowSelector1] = useState(false);
  const [showSelector2, setShowSelector2] = useState(false);

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 shadow-sm transition-colors">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-2xl bg-indigo-50 dark:bg-indigo-950/50 text-indigo-700 dark:text-indigo-400 border border-indigo-200 dark:border-indigo-800">
            <Layers className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-base sm:text-lg font-black text-slate-900 dark:text-slate-100 flex items-center gap-2">
              Dual-Stream Multi-View Studio
              <span className="text-xs px-2.5 py-0.5 rounded-full bg-indigo-100 dark:bg-indigo-950/60 text-indigo-800 dark:text-indigo-300 font-bold border border-indigo-200 dark:border-indigo-800">
                2 Screen Cinema
              </span>
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400">Watch two live football matches or TV channels side-by-side simultaneously</p>
          </div>
        </div>

        <button
          onClick={onClose}
          className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold transition-all cursor-pointer border border-slate-200 dark:border-slate-700"
        >
          Exit Multi-View
        </button>
      </div>

      {/* 2-Column Split Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Screen 1 */}
        <div className="space-y-3">
          <div className="flex items-center justify-between bg-white dark:bg-slate-900 px-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-2xs">
            <span className="text-xs font-bold text-slate-900 dark:text-slate-100 flex items-center gap-1.5">
              <Tv className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
              <span className="text-emerald-600 dark:text-emerald-400 font-black">Screen 1:</span>
              <span className="truncate max-w-[200px]">{stream1?.data?.name || stream1?.data?.home_team?.name || 'Select Match'}</span>
            </span>
            <button
              onClick={() => setShowSelector1(!showSelector1)}
              className="text-xs text-emerald-600 dark:text-emerald-400 hover:underline font-bold cursor-pointer"
            >
              {showSelector1 ? 'Cancel' : 'Change Feed'}
            </button>
          </div>

          {showSelector1 ? (
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 max-h-80 overflow-y-auto space-y-2 shadow-md">
              <p className="text-xs text-slate-500 dark:text-slate-400 font-bold mb-2">Select Live Feed for Screen 1:</p>
              {allAvailableStreams.map((item, idx) => (
                <button
                  key={idx}
                  onClick={() => {
                    onUpdateStream1(item);
                    setShowSelector1(false);
                  }}
                  className="w-full text-left p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 hover:bg-emerald-50 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:border-emerald-500/50 text-xs font-medium text-slate-800 dark:text-slate-200 flex items-center justify-between transition-all cursor-pointer"
                >
                  <span className="truncate flex items-center gap-1.5">
                    {item.type === 'match' ? (
                      <Tv className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                    ) : (
                      <Radio className="w-3.5 h-3.5 text-sky-600 dark:text-sky-400 shrink-0" />
                    )}
                    <span>{item.data?.name || `${item.data?.home_team?.name} vs ${item.data?.away_team?.name}`}</span>
                  </span>
                  <span className="text-[10px] text-emerald-600 dark:text-emerald-400 font-bold ml-2">SELECT</span>
                </button>
              ))}
            </div>
          ) : stream1 ? (
            <VideoPlayer streamItem={stream1} onClose={() => onUpdateStream1(null)} />
          ) : (
            <div className="aspect-video rounded-3xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center p-6 text-center bg-white dark:bg-slate-900 shadow-xs">
              <Plus className="w-8 h-8 text-slate-400 dark:text-slate-500 mb-2" />
              <p className="text-xs font-bold text-slate-600 dark:text-slate-400 mb-3">No stream selected for Screen 1</p>
              <button
                onClick={() => setShowSelector1(true)}
                className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all cursor-pointer shadow-sm shadow-emerald-600/20"
              >
                Choose Football Stream
              </button>
            </div>
          )}
        </div>

        {/* Screen 2 */}
        <div className="space-y-3">
          <div className="flex items-center justify-between bg-white dark:bg-slate-900 px-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-2xs">
            <span className="text-xs font-bold text-slate-900 dark:text-slate-100 flex items-center gap-1.5">
              <Tv className="w-3.5 h-3.5 text-sky-600 dark:text-sky-400" />
              <span className="text-sky-600 dark:text-sky-400 font-black">Screen 2:</span>
              <span className="truncate max-w-[200px]">{stream2?.data?.name || stream2?.data?.home_team?.name || 'Select Match'}</span>
            </span>
            <button
              onClick={() => setShowSelector2(!showSelector2)}
              className="text-xs text-sky-600 dark:text-sky-400 hover:underline font-bold cursor-pointer"
            >
              {showSelector2 ? 'Cancel' : 'Change Feed'}
            </button>
          </div>

          {showSelector2 ? (
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 max-h-80 overflow-y-auto space-y-2 shadow-md">
              <p className="text-xs text-slate-500 dark:text-slate-400 font-bold mb-2">Select Live Feed for Screen 2:</p>
              {allAvailableStreams.map((item, idx) => (
                <button
                  key={idx}
                  onClick={() => {
                    onUpdateStream2(item);
                    setShowSelector2(false);
                  }}
                  className="w-full text-left p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 hover:bg-sky-50 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:border-sky-500/50 text-xs font-medium text-slate-800 dark:text-slate-200 flex items-center justify-between transition-all cursor-pointer"
                >
                  <span className="truncate flex items-center gap-1.5">
                    {item.type === 'match' ? (
                      <Tv className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                    ) : (
                      <Radio className="w-3.5 h-3.5 text-sky-600 dark:text-sky-400 shrink-0" />
                    )}
                    <span>{item.data?.name || `${item.data?.home_team?.name} vs ${item.data?.away_team?.name}`}</span>
                  </span>
                  <span className="text-[10px] text-sky-600 dark:text-sky-400 font-bold ml-2">SELECT</span>
                </button>
              ))}
            </div>
          ) : stream2 ? (
            <VideoPlayer streamItem={stream2} onClose={() => onUpdateStream2(null)} />
          ) : (
            <div className="aspect-video rounded-3xl border-2 border-dashed border-slate-300 dark:border-slate-700 flex flex-col items-center justify-center p-6 text-center bg-white dark:bg-slate-900 shadow-xs">
              <Plus className="w-8 h-8 text-slate-400 dark:text-slate-500 mb-2" />
              <p className="text-xs font-bold text-slate-600 dark:text-slate-400 mb-3">No stream selected for Screen 2</p>
              <button
                onClick={() => setShowSelector2(true)}
                className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold transition-all cursor-pointer shadow-sm shadow-sky-600/20"
              >
                Choose Football Stream
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
