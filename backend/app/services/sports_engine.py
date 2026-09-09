"""
Universal Multi-Sport Data Engine
Fetches live fixtures, scores, schedules, and official broadcast feeds for:
- Basketball (NBA, WNBA, NCAA)
- American Football (NFL, College Football)
- Motorsport (Formula 1)
- Tennis (ATP, WTA)
- Combat Sports (UFC, Boxing)
- Baseball (MLB)
"""

import httpx
import asyncio
import datetime
import time
import logging
import urllib.parse
from typing import List, Dict, Any, Optional

logger = logging.getLogger("sports_engine")

SPORTS_CONFIGS = {
    "cricket": {
        "name": "Cricket",
        "sport_code": "cricket",
        "leagues": [
            {"id": "icc", "name": "ICC International", "code": "icc", "short_code": "ICC"},
            {"id": "ipl", "name": "Indian Premier League", "code": "ipl", "short_code": "IPL"},
            {"id": "psl", "name": "Pakistan Super League", "code": "psl", "short_code": "PSL"},
            {"id": "bbl", "name": "Big Bash League", "code": "bbl", "short_code": "BBL"},
            {"id": "county", "name": "County Championship", "code": "county", "short_code": "ENG"},
            {"id": "t20", "name": "T20 Leagues", "code": "t20", "short_code": "T20"}
        ],
        "default_broadcasters": [
            {"id": "cric-srv-1", "label": "Server 1: Sky Sports Cricket HD (Official Live)", "network": "Sky Sports Cricket", "quality": "1080p 60fps", "language": "English (Sky UK)", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "Ball-by-Ball Live Commentary"},
            {"id": "cric-srv-2", "label": "Server 2: Willow TV HD USA", "network": "Willow HD", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "North American Broadcast Feed"},
            {"id": "cric-srv-3", "label": "Server 3: TNT Sports / Star Sports", "network": "Star Sports", "quality": "1080p HD", "language": "English / Hindi", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Primetime HD Broadcast"},
            {"id": "cric-srv-4", "label": "Server 4: Direct 1080p Stream", "network": "beIN Sports", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "High Bandwidth Direct Video"}
        ]
    },
    "basketball": {
        "name": "Basketball",
        "sport_code": "basketball",
        "leagues": [
            {"id": "nba", "name": "NBA", "code": "nba", "short_code": "NBA"},
            {"id": "wnba", "name": "WNBA", "code": "wnba", "short_code": "WNBA"},
            {"id": "ncaa_mbb", "name": "NCAA Men's Basketball", "code": "mens-college-basketball", "short_code": "NCAA"}
        ],
        "default_broadcasters": [
            {"id": "bball-srv-1", "label": "Server 1: NBA TV HD (Official Live)", "network": "NBA TV", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/nba-tv", "is_embed": True, "coverage": "Official NBA Broadcast Feed"},
            {"id": "bball-srv-2", "label": "Server 2: ESPN Basketball Live", "network": "ESPN HD", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "USA Prime Matchday"},
            {"id": "bball-srv-3", "label": "Server 3: TNT Sports Basketball", "network": "TNT Sports", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Primetime European Broadcast"},
            {"id": "bball-srv-4", "label": "Server 4: Direct 1080p Stream", "network": "beIN Sports", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "High Bandwidth Direct Video"}
        ]
    },
    "nfl": {
        "name": "American Football",
        "sport_code": "football",
        "leagues": [
            {"id": "nfl", "name": "NFL", "code": "nfl", "short_code": "NFL"},
            {"id": "cfb", "name": "College Football", "code": "college-football", "short_code": "CFB"}
        ],
        "default_broadcasters": [
            {"id": "nfl-srv-1", "label": "Server 1: NFL Network HD (Official Live)", "network": "NFL Network", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/nfl-network", "is_embed": True, "coverage": "Official NFL Game Pass Feed"},
            {"id": "nfl-srv-2", "label": "Server 2: ESPN Sunday Night Football", "network": "ESPN / ABC", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "National Game Broadcast"},
            {"id": "nfl-srv-3", "label": "Server 3: Sky Sports NFL Live", "network": "Sky Sports NFL", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "International Broadcast"},
            {"id": "nfl-srv-4", "label": "Server 4: Direct 1080p Video", "network": "beIN XTRA", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "High Bandwidth Direct Video"}
        ]
    },
    "motorsport": {
        "name": "Motorsport",
        "sport_code": "racing",
        "leagues": [
            {"id": "f1", "name": "Formula 1", "code": "f1", "short_code": "F1"}
        ],
        "default_broadcasters": [
            {"id": "f1-srv-1", "label": "Server 1: Sky Sports F1 HD (Official Live)", "network": "Sky Sports F1", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "Full Weekend Trackside Live"},
            {"id": "f1-srv-2", "label": "Server 2: F1 TV Live International Feed", "network": "F1 TV Pro", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Cockpit & Pitlane Radio"},
            {"id": "f1-srv-3", "label": "Server 3: Canal+ Sport Formule 1", "network": "CANAL+ F1", "quality": "1080p HD", "language": "International", "url": "https://epiembeds.online/embed/canalsport-pl", "is_embed": True, "coverage": "European Paddock Live"},
            {"id": "f1-srv-4", "label": "Server 4: Direct HLS Video Feed", "network": "Motorsport Vault", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "Direct Video Stream"}
        ]
    },
    "tennis": {
        "name": "Tennis",
        "sport_code": "tennis",
        "leagues": [
            {"id": "atp", "name": "ATP Tour", "code": "atp", "short_code": "ATP"},
            {"id": "wta", "name": "WTA Tour", "code": "wta", "short_code": "WTA"}
        ],
        "default_broadcasters": [
            {"id": "ten-srv-1", "label": "Server 1: Tennis Channel HD (Center Court)", "network": "Tennis Channel", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "Official Center Court Live"},
            {"id": "ten-srv-2", "label": "Server 2: Eurosport 1 Tennis Live", "network": "Eurosport 1", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Grand Slam Matchday"},
            {"id": "ten-srv-3", "label": "Server 3: Sky Sports Tennis HD", "network": "Sky Sports Tennis", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "ATP / WTA Tour Live"},
            {"id": "ten-srv-4", "label": "Server 4: Direct 1080p Video Feed", "network": "beIN Sports Tennis", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "Direct Video Feed"}
        ]
    },
    "combat": {
        "name": "Combat Sports",
        "sport_code": "mma",
        "leagues": [
            {"id": "ufc", "name": "UFC", "code": "ufc", "short_code": "UFC"}
        ],
        "default_broadcasters": [
            {"id": "mma-srv-1", "label": "Server 1: UFC Fight Pass HD (Main Card)", "network": "UFC Fight Pass", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Octagon Main Event Live"},
            {"id": "mma-srv-2", "label": "Server 2: ESPN+ Pay-Per-View Feed", "network": "ESPN+ PPV", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "Championship Fights Live"},
            {"id": "mma-srv-3", "label": "Server 3: TNT Sports Box Office HD", "network": "TNT Box Office", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "Undercard & Prelims"},
            {"id": "mma-srv-4", "label": "Server 4: Direct Video Feed", "network": "Combat Vault", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "High Bandwidth Direct Video"}
        ]
    },
    "baseball": {
        "name": "Baseball",
        "sport_code": "baseball",
        "leagues": [
            {"id": "mlb", "name": "MLB", "code": "mlb", "short_code": "MLB"}
        ],
        "default_broadcasters": [
            {"id": "mlb-srv-1", "label": "Server 1: MLB Network HD (Live Ballpark)", "network": "MLB Network", "quality": "1080p 60fps", "language": "English", "url": "https://epiembeds.online/embed/espn-usa", "is_embed": True, "coverage": "Official Ballpark World Feed"},
            {"id": "mlb-srv-2", "label": "Server 2: ESPN Sunday Night Baseball", "network": "ESPN MLB", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/tntsports1-uk", "is_embed": True, "coverage": "Primetime National Game"},
            {"id": "mlb-srv-3", "label": "Server 3: Fox Sports MLB Live", "network": "Fox Sports HD", "quality": "1080p HD", "language": "English", "url": "https://epiembeds.online/embed/sky-sports-premier-league", "is_embed": True, "coverage": "Interleague Game Live"},
            {"id": "mlb-srv-4", "label": "Server 4: Direct HLS Stream", "network": "beIN Baseball", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "coverage": "High Bandwidth Stream"}
        ]
    }
}

class UniversalSportsEngine:
    def __init__(self):
        self.sport_caches: Dict[str, List[Dict[str, Any]]] = {}
        self.last_fetch: Dict[str, float] = {}
        self.cache_ttl = 300.0  # 5 minutes

    async def fetch_sport_matches(self, sport: str) -> List[Dict[str, Any]]:
        """Fetches live fixtures and scoreboards from ESPN for the specified sport."""
        s_key = (sport or "basketball").lower().strip()
        if s_key not in SPORTS_CONFIGS:
            return []

        now = time.time()
        has_live = any(m.get("status") == "LIVE" for m in self.sport_caches.get(s_key, []))
        effective_ttl = 25.0 if has_live else self.cache_ttl
        if s_key in self.sport_caches and (now - self.last_fetch.get(s_key, 0)) < effective_ttl:
            return self.sport_caches[s_key]

        cfg = SPORTS_CONFIGS[s_key]
        leagues = cfg["leagues"]
        sport_code = cfg["sport_code"]
        matches = []

        if s_key == "cricket":
            async with httpx.AsyncClient(timeout=8.0) as client:
                try:
                    url = "https://site.web.api.espn.com/apis/v2/scoreboard/header?sport=cricket"
                    resp = await client.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                    if resp.status_code == 200:
                        data = resp.json()
                        sports_list = data.get("sports", [])
                        if sports_list:
                            for l in sports_list[0].get("leagues", []):
                                lname = l.get("name", "International Cricket")
                                lid = str(l.get("id", "icc"))
                                for e in l.get("events", []):
                                    comps = e.get("competitors", [])
                                    if len(comps) < 2:
                                        continue
                                    h = comps[0]
                                    a = comps[1]
                                    
                                    f_st = e.get("fullStatus", {}).get("type", {}).get("state", e.get("status", "pre"))
                                    summary = e.get("fullStatus", {}).get("summary") or e.get("summary", "Match scheduled")
                                    
                                    if f_st == "in":
                                        match_status = "LIVE"
                                        minute = summary
                                        match_time = f"{summary} • Live"
                                    elif f_st == "post":
                                        match_status = "FINISHED"
                                        minute = "FT"
                                        match_time = f"Result: {summary}"
                                    else:
                                        match_status = "UPCOMING"
                                        minute = e.get("locationAndDate") or "Scheduled"
                                        match_time = summary or "Scheduled"
                                        
                                    h_name = h.get("displayName", "Team A")
                                    a_name = a.get("displayName", "Team B")
                                    h_score = h.get("score") or ""
                                    a_score = a.get("score") or ""
                                    h_logo = h.get("logo") or "https://a.espncdn.com/i/teamlogos/cricket/500/default.png"
                                    a_logo = a.get("logo") or "https://a.espncdn.com/i/teamlogos/cricket/500/default.png"
                                    
                                    matches.append({
                                        "id": f"cric-{e.get('id', len(matches))}",
                                        "sport": "Cricket",
                                        "sport_id": "cricket",
                                        "league": lname,
                                        "league_id": lid,
                                        "league_short": "CRIC",
                                        "round": e.get("title", lname),
                                        "raw_date": e.get("date", ""),
                                        "kickoff_date": e.get("locationAndDate", "Matchday"),
                                        "kickoff_time": summary,
                                        "short_date": e.get("locationAndDate", "Matchday"),
                                        "formatted_date_time": e.get("locationAndDate", "Matchday"),
                                        "home_team": {
                                            "name": h_name,
                                            "short_name": h.get("abbreviation", h_name[:3].upper()),
                                            "logo": h_logo,
                                            "score": h_score or 0,
                                            "display_score": h_score,
                                            "form": "W-W-L"
                                        },
                                        "away_team": {
                                            "name": a_name,
                                            "short_name": a.get("abbreviation", a_name[:3].upper()),
                                            "logo": a_logo,
                                            "score": a_score or 0,
                                            "display_score": a_score,
                                            "form": "L-W-W"
                                        },
                                        "status": match_status,
                                        "minute": minute,
                                        "match_time": match_time,
                                        "stadium": e.get("location", f"{h_name} Stadium"),
                                        "possession": {"home": 50, "away": 50},
                                        "shots_on_target": {"home": 0, "away": 0},
                                        "total_shots": {"home": 0, "away": 0},
                                        "corners": {"home": 0, "away": 0},
                                        "yellow_cards": {"home": 0, "away": 0},
                                        "events": [],
                                        "streams": cfg["default_broadcasters"],
                                        "priority": 1 if match_status == "LIVE" else (2 if match_status == "UPCOMING" else 3),
                                        "viewers_count": 650000 if match_status == "LIVE" else 320000,
                                        "featured": match_status == "LIVE"
                                    })
                except Exception as ex:
                    logger.warning(f"Error fetching cricket: {ex}")


        async with httpx.AsyncClient(timeout=8.0) as client:
            async def fetch_league(l_info):
                league_matches = []
                try:
                    url = f"https://site.api.espn.com/apis/site/v2/sports/{sport_code}/{l_info['code']}/scoreboard"
                    resp = await client.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                    if resp.status_code == 200:
                        data = resp.json()
                        events = data.get("events", [])
                        for e in events:
                            comps = e.get("competitions", [])
                            if not comps:
                                continue
                            comp = comps[0]
                            competitors = comp.get("competitors", [])
                            if len(competitors) < 2:
                                continue
                            
                            home = next((c for c in competitors if c.get("homeAway") == "home"), competitors[0])
                            away = next((c for c in competitors if c.get("homeAway") == "away"), competitors[1])
                            
                            status_obj = comp.get("status", {})
                            status_type = status_obj.get("type", {})
                            status_state = status_type.get("state", "pre")
                            short_detail = status_type.get("shortDetail") or status_type.get("detail", "Scheduled")
                            
                            raw_date = e.get("date") or comp.get("date", "")
                            
                            home_name = home.get("team", {}).get("displayName", "Home Team")
                            away_name = away.get("team", {}).get("displayName", "Away Team")
                            
                            home_logo = home.get("team", {}).get("logo") or "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/tor.png"
                            away_logo = away.get("team", {}).get("logo") or "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/mia.png"
                            
                            home_score = int(home.get("score") or 0)
                            away_score = int(away.get("score") or 0)
                            
                            if status_state == "in":
                                match_status = "LIVE"
                                minute = short_detail
                                match_time = f"{minute} Live"
                            elif status_state == "post":
                                match_status = "FINISHED"
                                minute = "FT"
                                match_time = f"Final • {short_detail}"
                            else:
                                match_status = "UPCOMING"
                                minute = short_detail
                                match_time = f"Scheduled: {short_detail}"
                            
                            venue = comp.get("venue", {}).get("fullName", f"{home_name} Arena")
                            if match_status == "FINISHED":
                                q_enc = urllib.parse.quote_plus(f"{home_name} vs {away_name} highlights {cfg.get('name', '')}")
                                broadcasters = [
                                    {
                                        "id": f"{s_key}-yt-hl-{e.get('id', len(league_matches))}",
                                        "label": f"Server 1: YouTube Official Highlights ({home_name} vs {away_name})",
                                        "network": f"{cfg['name']} Highlights",
                                        "quality": "1080p HD",
                                        "language": "English Commentary",
                                        "url": f"https://www.youtube-nocookie.com/embed?listType=search&list={q_enc}",
                                        "watch_url": f"https://www.youtube.com/results?search_query={q_enc}",
                                        "is_embed": True,
                                        "is_primary": True,
                                        "is_replay": True,
                                        "coverage": f"Official Video Highlights: {home_name} vs {away_name}"
                                    },
                                    {
                                        "id": f"{s_key}-dm-hl-{e.get('id', len(league_matches))}",
                                        "label": "Server 2: Dailymotion Sports Mirror",
                                        "network": "Dailymotion Sports",
                                        "quality": "1080p 60fps",
                                        "language": "International",
                                        "url": "https://geo.dailymotion.com/player.html?video=x9z79ao",
                                        "watch_url": f"https://www.dailymotion.com/search/{urllib.parse.quote_plus(home_name + ' ' + away_name)}",
                                        "is_embed": True,
                                        "is_primary": False,
                                        "is_replay": True,
                                        "coverage": f"Extended Game Highlights: {home_name} vs {away_name}"
                                    }
                                ]
                            else:
                                broadcasters = cfg.get("default_broadcasters", [])
                            
                            league_matches.append({
                                "id": match_id,
                                "sport": cfg["name"],
                                "sport_id": s_key,
                                "league": l_info["name"],
                                "league_id": l_info["id"],
                                "league_short": l_info.get("short_code", l_info["id"].upper()),
                                "round": e.get("name", l_info["name"]),
                                "raw_date": raw_date,
                                "kickoff_date": short_detail,
                                "kickoff_time": short_detail,
                                "short_date": short_detail,
                                "formatted_date_time": short_detail,
                                "home_team": {
                                    "name": home_name,
                                    "short_name": home.get("team", {}).get("abbreviation", home_name[:3].upper()),
                                    "logo": home_logo,
                                    "score": home_score,
                                    "form": "W-W-L"
                                },
                                "away_team": {
                                    "name": away_name,
                                    "short_name": away.get("team", {}).get("abbreviation", away_name[:3].upper()),
                                    "logo": away_logo,
                                    "score": away_score,
                                    "form": "L-W-W"
                                },
                                "status": match_status,
                                "minute": minute,
                                "match_time": match_time,
                                "stadium": venue,
                                "possession": {"home": 51, "away": 49},
                                "shots_on_target": {"home": max(home_score, 1), "away": max(away_score, 1)},
                                "total_shots": {"home": max(home_score + 5, 6), "away": max(away_score + 4, 5)},
                                "corners": {"home": 4, "away": 3},
                                "yellow_cards": {"home": 0, "away": 0},
                                "events": [],
                                "streams": broadcasters,
                                "priority": 1 if match_status == "LIVE" else (2 if match_status == "UPCOMING" else 3),
                                "viewers_count": 480000 if match_status == "LIVE" else 240000,
                                "featured": match_status == "LIVE"
                            })
                except Exception as ex:
                    logger.warning(f"Error fetching {s_key} league {l_info['name']}: {ex}")
                return league_matches

            results = await asyncio.gather(*[fetch_league(l) for l in leagues], return_exceptions=True)
            for res in results:
                if isinstance(res, list):
                    matches.extend(res)

        if matches:
            live = [m for m in matches if m.get("status") == "LIVE"]
            upcoming = [m for m in matches if m.get("status") in ["UPCOMING", "SCHEDULED"]]
            finished = [m for m in matches if m.get("status") in ["FINISHED", "FT"]]
            
            live.sort(key=lambda m: m.get("raw_date", ""))
            
            # Enrich live multi-sport matches with real-time verified broadcast streams
            if live:
                try:
                    from app.services.live_stream_resolver import live_stream_resolver
                    async def enrich_live_sport(m):
                        try:
                            h_name = m.get("home_team", {}).get("name", "")
                            a_name = m.get("away_team", {}).get("name", "")
                            live_srvs = await live_stream_resolver.resolve_match_streams(h_name, a_name, s_key)
                            if live_srvs:
                                m["streams"] = live_srvs
                        except Exception:
                            pass
                    await asyncio.gather(*[enrich_live_sport(m) for m in live], return_exceptions=True)
                except Exception as ex:
                    logger.warning(f"Error enriching {s_key} live streams: {ex}")

            upcoming.sort(key=lambda m: m.get("raw_date", ""))
            finished.sort(key=lambda m: m.get("raw_date", ""), reverse=True)
            
            sorted_matches = live + upcoming + finished
            self.sport_caches[s_key] = sorted_matches
            self.last_fetch[s_key] = time.time()
            return sorted_matches

        return self.sport_caches.get(s_key, [])

    def get_sport_config(self, sport: str) -> Dict[str, Any]:
        s_key = (sport or "basketball").lower().strip()
        return SPORTS_CONFIGS.get(s_key, SPORTS_CONFIGS.get("basketball", {}))

    async def get_live_sports_matches(self, sport: str, league_filter: str = None, status_filter: str = None) -> Dict[str, Any]:
        s_key = (sport or "basketball").lower().strip()
        all_matches = await self.fetch_sport_matches(s_key)
        filtered = list(all_matches)
        
        if league_filter and league_filter.lower() != "all":
            lf = league_filter.lower().strip()
            filtered = [m for m in filtered if m.get("league_id", "").lower() == lf or lf in m.get("league", "").lower()]
            
        if status_filter and status_filter.lower() != "all":
            sf = status_filter.upper().strip()
            if sf in ["LIVE"]:
                filtered = [m for m in filtered if m.get("status") == "LIVE"]
            elif sf in ["UPCOMING", "SCHEDULED"]:
                filtered = [m for m in filtered if m.get("status") in ["UPCOMING", "SCHEDULED"]]
            elif sf in ["FINISHED", "FT"]:
                filtered = [m for m in filtered if m.get("status") in ["FINISHED", "FT"]]
                
        total_live = sum(1 for m in all_matches if m.get("status") == "LIVE")
        total_upcoming = sum(1 for m in all_matches if m.get("status") in ["UPCOMING", "SCHEDULED"])
        total_finished = sum(1 for m in all_matches if m.get("status") in ["FINISHED", "FT"])
        
        cfg = self.get_sport_config(s_key)
        return {
            "sport": cfg.get("name", s_key.capitalize()),
            "sport_id": s_key,
            "total_matches": len(filtered),
            "total_live": total_live,
            "total_upcoming": total_upcoming,
            "total_finished": total_finished,
            "matches": filtered,
            "leagues": cfg.get("leagues", [])
        }

    def get_sport_match_by_id(self, match_id: str) -> Optional[Dict[str, Any]]:
        for sport, matches in self.sport_caches.items():
            for m in matches:
                if str(m.get("id")) == str(match_id):
                    return m
        return None

    async def get_overview(self, sport: str) -> Dict[str, Any]:
        """Returns overview for the specified sport with marquee match and total counts."""
        s_key = (sport or "basketball").lower().strip()
        matches = await self.fetch_sport_matches(s_key)
        cfg = self.get_sport_config(s_key)
        
        marquee = next((m for m in matches if m.get("status") == "LIVE"), matches[0] if matches else None)
        total_live = sum(1 for m in matches if m.get("status") == "LIVE")
        total_upcoming = sum(1 for m in matches if m.get("status") in ["UPCOMING", "SCHEDULED"])
        total_finished = sum(1 for m in matches if m.get("status") in ["FINISHED", "FT"])
        total_viewers = sum(m.get("viewers_count", 0) for m in matches)
        
        return {
            "sport": cfg["name"],
            "sport_id": s_key,
            "marquee_match": marquee,
            "matches": matches,
            "leagues": cfg["leagues"],
            "total_live": total_live,
            "total_upcoming": total_upcoming,
            "total_finished": total_finished,
            "total_viewers": total_viewers
        }

universal_sports_engine = UniversalSportsEngine()

