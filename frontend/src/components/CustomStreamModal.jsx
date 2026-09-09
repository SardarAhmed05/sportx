import React, { useState } from 'react';
import { PlaySquare, X, Play, ShieldCheck, Sparkles } from 'lucide-react';

export default function CustomStreamModal({ isOpen, onClose, onPlayCustomStream }) {
  const [streamUrl, setStreamUrl] = useState('');
  const [streamName, setStreamName] = useState('');
  const [sport, setSport] = useState('Football');

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!streamUrl.trim()) return;

    onPlayCustomStream({
      type: 'channel',
      sport: sport,
      data: {
        id: 'custom-' + Date.now(),
        name: streamName.trim() || 'Custom Live Feed',
        sport: sport,
        category: sport,
        stream_url: streamUrl.trim(),
        quality: '1080p HD',
        country: 'Global',
        language: 'Multilingual',
        description: 'User provided custom stream feed',
        backup_streams: []
      }
    });
    onClose();
  };

  const sampleStreams = [
    { label: 'Mux Live Test HLS (Big Buck)', url: 'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8', sport: 'Football' },
    { label: 'Akamai Live Test Feed (1080p)', url: 'https://cph-p2p-msl.akamaized.net/hls/live/2000341/test/master.m3u8', sport: 'Football' },
    { label: 'Apple BipBop 16x9 Live Test', url: 'https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8', sport: 'Worldwide Sports' },
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
      <div className="relative w-full max-w-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl shadow-2xl p-6 text-slate-900 dark:text-slate-100">
        <div className="flex items-center justify-between pb-4 border-b border-slate-200 dark:border-slate-800 mb-5">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400">
              <PlaySquare className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-black text-slate-900 dark:text-white">Play Custom Stream Feed</h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">Play any .m3u8, HLS, or direct live stream URL</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 cursor-pointer">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1.5">Stream Title (Optional)</label>
            <input
              type="text"
              placeholder="e.g. Champions League Live Feed"
              value={streamName}
              onChange={(e) => setStreamName(e.target.value)}
              className="w-full px-3.5 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:bg-white dark:focus:bg-slate-900 focus:outline-none focus:border-emerald-500"
            />
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1.5">Stream Category</label>
            <select
              value={sport}
              onChange={(e) => setSport(e.target.value)}
              className="w-full px-3.5 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-900 dark:text-slate-100 focus:bg-white dark:focus:bg-slate-900 focus:outline-none focus:border-emerald-500 cursor-pointer"
            >
              <option value="Football">Football Live Match</option>
              <option value="Cricket">Cricket Live Match</option>
              <option value="Basketball">Basketball Live Match</option>
              <option value="Global Sports">Global Sports Live Feed</option>
              <option value="24/7 TV">24/7 Sports TV Channel</option>
            </select>
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1.5">HLS / M3U8 Stream URL *</label>
            <input
              type="url"
              required
              placeholder="https://example.com/live/stream.m3u8"
              value={streamUrl}
              onChange={(e) => setStreamUrl(e.target.value)}
              className="w-full px-3.5 py-2.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:bg-white dark:focus:bg-slate-900 focus:outline-none focus:border-emerald-500 font-mono"
            />
          </div>

          {/* Quick preset tests */}
          <div className="pt-2">
            <p className="text-[11px] font-bold text-slate-500 dark:text-slate-400 mb-2">Or load verified sample feed:</p>
            <div className="space-y-1.5">
              {sampleStreams.map((s, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => {
                    setStreamUrl(s.url);
                    setStreamName(s.label);
                  }}
                  className="w-full text-left p-2 rounded-xl bg-slate-50 dark:bg-slate-800 hover:bg-emerald-50 dark:hover:bg-slate-750 border border-slate-200 dark:border-slate-700 hover:border-emerald-300 text-xs text-slate-700 dark:text-slate-300 flex items-center justify-between transition-colors cursor-pointer"
                >
                  <span className="truncate">{s.label}</span>
                  <span className="text-[10px] text-emerald-700 dark:text-emerald-400 font-bold ml-2">LOAD</span>
                </button>
              ))}
            </div>
          </div>

          <div className="pt-4 flex items-center justify-end gap-2 border-t border-slate-200 dark:border-slate-800">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold transition-colors cursor-pointer"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="flex items-center gap-1.5 px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-black shadow-md shadow-emerald-600/20 transition-all cursor-pointer"
            >
              <Play className="w-3.5 h-3.5 fill-white" />
              <span>Launch Feed</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
