import httpx
import asyncio
import time
import logging
import re
from typing import List, Dict, Any, Optional

logger = logging.getLogger("live_stream_resolver")

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
        await self._ensure_cache()
        if not self._matches_cache:
            return []

        best_match = None
        best_score = 0
        for m in self._matches_cache:
            title = m.get("title", "")
            sc = self._match_score(home_name, away_name, title)
            if sc > best_score:
                best_score = sc
                best_match = m

        if not best_match or best_score < 6:
            return []

        match_id = best_match.get("id")
        match_title = best_match.get("title")
        sources = best_match.get("sources", [])
        watch_url = f"https://streamed.pk/watch/{match_id}"

        servers = []
        # Query up to 3 sources concurrently
        async with httpx.AsyncClient(timeout=3.5, verify=False, headers={"User-Agent": "Mozilla/5.0"}) as client:
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

                        servers.append({
                            "id": f"srv-{src}-{s_no}-{len(servers)+1}",
                            "label": f"Server {len(servers)+1}: {lang} ({src.upper()})",
                            "network": f"{src.upper()} Live Sports Network",
                            "quality": "1080p 60fps" if is_hd else "720p HD",
                            "language": lang,
                            "url": embed_url,
                            "watch_url": watch_url,
                            "is_embed": True,
                            "is_primary": len(servers) == 0,
                            "is_replay": False,
                            "viewers": viewers,
                            "coverage": f"Official Live Broadcast: {match_title}"
                        })

        # Add Full Standalone Player server as a backup option
        servers.append({
            "id": f"srv-matchroom-{match_id[:12]}",
            "label": f"Server {len(servers)+1}: Ultra HD Matchroom Player",
            "network": "Global Streamed Network",
            "quality": "1080p Ultra HD",
            "language": "English / Multi-Audio",
            "url": watch_url,
            "watch_url": watch_url,
            "is_embed": True,
            "is_primary": len(servers) == 0,
            "is_replay": False,
            "coverage": f"Full Live Matchroom Hub: {match_title}"
        })

        return servers

# Global singleton instance
live_stream_resolver = LiveStreamResolver()
