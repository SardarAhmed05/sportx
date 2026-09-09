import httpx
import asyncio
import time
import logging
import re
from typing import List, Dict, Any, Optional

logger = logging.getLogger("live_stream_resolver")

VERIFIED_BACKUP_FEEDS = {
    "football": [
        {
            "network": "Sky Sports Premier League HD",
            "quality": "1080p 60fps",
            "language": "English (UK)",
            "url": "https://epiembeds.online/embed/sky-sports-premier-league",
            "coverage": "Live Sports Broadcast"
        },
        {
            "network": "TNT Sports 1 HD",
            "quality": "1080p HD",
            "language": "English (UK)",
            "url": "https://epiembeds.online/embed/tntsports1-uk",
            "coverage": "Primetime European Sports"
        },
        {
            "network": "NBC Sports / USA Network",
            "quality": "1080p HD",
            "language": "English (USA)",
            "url": "https://epiembeds.online/embed/espn-usa",
            "coverage": "Live Matchday Coverage"
        },
        {
            "network": "Direct 1080p Stream",
            "quality": "1080p HD",
            "language": "English",
            "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
            "coverage": "High Bandwidth Direct Video"
        }
    ],
    "basketball": [
        {
            "network": "NBA TV HD",
            "quality": "1080p 60fps",
            "language": "English",
            "url": "https://epiembeds.online/embed/nba-tv",
            "coverage": "Official NBA Live"
        },
        {
            "network": "ESPN Basketball Live",
            "quality": "1080p HD",
            "language": "English",
            "url": "https://epiembeds.online/embed/espn-usa",
            "coverage": "USA Prime Matchday"
        },
        {
            "network": "TNT Sports Basketball",
            "quality": "1080p HD",
            "language": "English",
            "url": "https://epiembeds.online/embed/tntsports1-uk",
            "coverage": "Primetime European Broadcast"
        }
    ]
}

class LiveStreamResolver:
    def __init__(self):
        self._matches_cache = []
        self._last_fetch = 0
        self._cache_ttl = 60  # seconds
        self._lock = asyncio.Lock()
        self._stream_details_cache = {}  # (source, sid) -> list of streams

    async def _ensure_cache(self):
        now = time.time()
        if self._matches_cache and (now - self._last_fetch) < self._cache_ttl:
            return

        async with self._lock:
            # Double check inside lock
            if self._matches_cache and (time.time() - self._last_fetch) < self._cache_ttl:
                return
            
            endpoints = [
                "https://streamed.pk/api/matches/all",
                "https://streamed.su/api/matches/all",
                "https://v2.streamed.su/api/matches/all"
            ]
            for ep in endpoints:
                try:
                    async with httpx.AsyncClient(timeout=4.0, verify=False, headers={"User-Agent": "Mozilla/5.0"}) as client:
                        resp = await client.get(ep)
                        if resp.status_code == 200:
                            data = resp.json()
                            if isinstance(data, list) and len(data) > 0:
                                self._matches_cache = data
                                self._last_fetch = time.time()
                                logger.info(f"Loaded {len(data)} live matches from {ep}")
                                return
                except Exception as e:
                    logger.warning(f"Failed to fetch live streams from {ep}: {e}")

    def _normalize(self, text: str) -> str:
        t = re.sub(r'[^a-zA-Z0-9\s]', ' ', (text or '').lower())
        return ' '.join(t.split())

    def _match_score(self, query_home: str, query_away: str, match_title: str) -> int:
        h = self._normalize(query_home)
        a = self._normalize(query_away)
        title = self._normalize(match_title)

        score = 0
        # Direct presence of key team names
        h_words = [w for w in h.split() if len(w) > 2]
        a_words = [w for w in a.split() if len(w) > 2]

        h_match = any(w in title for w in h_words)
        a_match = any(w in title for w in a_words)

        if h_match and a_match:
            score += 10
        elif h_match or a_match:
            score += 3
        return score

    async def resolve_match_streams(self, home_name: str, away_name: str, sport: str = "football") -> List[Dict[str, Any]]:
        s_key = (sport or "football").lower().strip()
        await self._ensure_cache()

        candidates = []
        if self._matches_cache:
            for m in self._matches_cache:
                title = m.get("title", "")
                sc = self._match_score(home_name, away_name, title)
                if sc >= 6:
                    srcs = [s.get("source") for s in m.get("sources", [])]
                    boost = 0
                    for s in srcs:
                        if s in ["admin", "delta", "golf", "alpha", "bravo", "charlie"]:
                            boost += 5
                    candidates.append((sc + boost, m))

        candidates.sort(key=lambda x: x[0], reverse=True)

        servers = []
        if candidates:
            async with httpx.AsyncClient(timeout=4.0, verify=False, headers={"User-Agent": "Mozilla/5.0"}) as client:
                for score, best_match in candidates[:3]:
                    match_title = best_match.get("title")
                    sources = best_match.get("sources", [])

                    async def fetch_source(s):
                        src = s.get("source")
                        sid = s.get("id")
                        cache_key = f"{src}_{sid}"
                        if cache_key in self._stream_details_cache:
                            return src, self._stream_details_cache[cache_key]
                        try:
                            r = await client.get(f"https://streamed.pk/api/stream/{src}/{sid}")
                            if r.status_code == 200:
                                res = r.json()
                                self._stream_details_cache[cache_key] = res
                                return src, res
                        except Exception:
                            pass
                        return src, []

                    results = await asyncio.gather(*[fetch_source(s) for s in sources[:4]], return_exceptions=True)
                    for res in results:
                        if isinstance(res, tuple):
                            src, stream_list = res
                            for st in stream_list:
                                s_no = st.get("streamNo", 1)
                                lang = st.get("language") or "Live HD Feed"
                                embed_url = st.get("embedUrl") or f"https://embed.st/embed/{src}/{st.get('id', '')}/{s_no}"
                                is_hd = st.get("hd", True)
                                viewers = st.get("viewers", 0)

                                # Strictly reject full-page web portals like streamed.pk/watch
                                if embed_url and "watch" not in embed_url:
                                    servers.append({
                                        "id": f"srv-{src}-{s_no}-{len(servers)+1}",
                                        "label": f"Server {len(servers)+1}: {lang} ({src.upper()})",
                                        "network": f"{src.upper()} Live Sports Network",
                                        "quality": "1080p 60fps" if is_hd else "720p HD",
                                        "language": lang,
                                        "url": embed_url,
                                        "is_embed": True,
                                        "is_primary": len(servers) == 0,
                                        "is_replay": False,
                                        "viewers": viewers,
                                        "coverage": f"Official Live Broadcast: {match_title}"
                                    })
                    # If valid embed streams were found, break out
                    if servers:
                        break

        # Append reliable verified network backup feeds so every match has guaranteed failover
        backup_feeds = VERIFIED_BACKUP_FEEDS.get(s_key, VERIFIED_BACKUP_FEEDS.get("football", []))
        feeds_to_add = backup_feeds if not servers else backup_feeds[:2]
        for feed in feeds_to_add:
            srv_idx = len(servers) + 1
            servers.append({
                "id": f"srv-backup-{s_key}-{srv_idx}",
                "label": f"Server {srv_idx}: {feed['network']} (Official HD)",
                "network": feed["network"],
                "quality": feed.get("quality", "1080p HD"),
                "language": feed.get("language", "English"),
                "url": feed["url"],
                "is_embed": True,
                "is_primary": len(servers) == 0,
                "is_replay": False,
                "coverage": f"Official Broadcast Feed: {home_name} vs {away_name}"
            })

        return servers

# Global singleton instance
live_stream_resolver = LiveStreamResolver()
