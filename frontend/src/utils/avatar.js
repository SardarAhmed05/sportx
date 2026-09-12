/**
 * Team crest fallback generator and helpers
 * Generates high quality clean SVG avatars when remote images fail to load.
 * Strictly no emojis.
 */

export function generateTeamAvatar(teamName) {
  const clean = (teamName || 'Team').trim();
  const parts = clean.split(/\s+/);
  const initials = parts.length >= 2 
    ? (parts[0][0] + parts[1][0]).toUpperCase()
    : clean.slice(0, 2).toUpperCase();

  // Pick deterministic accent color based on name hash
  let hash = 0;
  for (let i = 0; i < clean.length; i++) {
    hash = clean.charCodeAt(i) + ((hash << 5) - hash);
  }
  const hues = ['#059669', '#2563eb', '#d97706', '#7c3aed', '#dc2626', '#0891b2', '#4f46e5'];
  const color = hues[Math.abs(hash) % hues.length];

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
    <defs>
      <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1e293b" />
        <stop offset="100%" stop-color="#0f172a" />
      </linearGradient>
    </defs>
    <rect width="96" height="96" rx="20" fill="url(#g)" stroke="#334155" stroke-width="2"/>
    <circle cx="48" cy="48" r="32" fill="${color}" fill-opacity="0.18" stroke="${color}" stroke-width="1.5"/>
    <text x="48" y="55" font-family="system-ui, -apple-system, sans-serif" font-weight="800" font-size="28" fill="#f8fafc" text-anchor="middle" dominant-baseline="middle">${initials}</text>
  </svg>`;

  return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
}

export function handleLogoError(e, teamName) {
  if (e && e.currentTarget) {
    e.currentTarget.onerror = null; // prevent infinite loops
    e.currentTarget.src = generateTeamAvatar(teamName);
  }
}
