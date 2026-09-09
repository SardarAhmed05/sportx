/**
 * API Service for communicating with the FastAPI Backend
 */

const API_BASE = (import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL.replace(/\/$/, '') : '') + '/api';

export async function fetchOverview(sport = 'football') {
  const params = new URLSearchParams();
  if (sport && sport !== 'football') params.append('sport', sport);
  const url = `${API_BASE}/matches/overview${params.toString() ? `?${params.toString()}` : ''}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to fetch overview');
  return res.json();
}

export async function fetchFootballMatches(league = null, sport = 'football') {
  const params = new URLSearchParams();
  if (league) params.append('league', league);
  if (sport && sport !== 'football') params.append('sport', sport);
  const url = `${API_BASE}/matches/overview${params.toString() ? `?${params.toString()}` : ''}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to fetch matches');
  return res.json();
}

export async function fetchFootballReplays(category = null, query = null, team = null, sport = 'football') {
  const params = new URLSearchParams();
  if (sport && sport !== 'football') params.append('sport', sport);
  if (category && category !== 'all') params.append('category', category);
  if (query) params.append('q', query);
  if (team) params.append('team', team);

  const url = `${API_BASE}/matches/replays${params.toString() ? `?${params.toString()}` : ''}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to fetch replays');
  return res.json();
}

export async function fetchReplayStreams(home, away, competition = '') {
  const params = new URLSearchParams();
  if (home) params.append('home', home);
  if (away) params.append('away', away);
  if (competition) params.append('competition', competition);

  const res = await fetch(`${API_BASE}/matches/replay-streams?${params.toString()}`);
  if (!res.ok) throw new Error('Failed to resolve match replay servers');
  return res.json();
}


export async function fetchChannels(sport = null, country = null, query = null) {
  const params = new URLSearchParams();
  if (sport && sport !== 'all') params.append('sport', sport);
  if (country && country !== 'ALL') params.append('country', country);
  if (query) params.append('q', query);

  const res = await fetch(`${API_BASE}/channels?${params.toString()}`);
  if (!res.ok) throw new Error('Failed to fetch channels');
  return res.json();
}

export async function fetchCategories() {
  const res = await fetch(`${API_BASE}/channels/categories`);
  if (!res.ok) throw new Error('Failed to fetch categories');
  return res.json();
}

export async function triggerScraper() {
  const res = await fetch(`${API_BASE}/scraper/trigger`, { method: 'POST' });
  if (!res.ok) throw new Error('Failed to trigger scraper');
  return res.json();
}

export async function checkStreamHealth(url) {
  const res = await fetch(`${API_BASE}/scraper/check-stream?url=${encodeURIComponent(url)}`);
  if (!res.ok) throw new Error('Failed to check stream health');
  return res.json();
}

export function getProxiedStreamUrl(originalUrl) {
  if (!originalUrl) return '';
  return `${API_BASE}/proxy/stream?url=${encodeURIComponent(originalUrl)}`;
}
