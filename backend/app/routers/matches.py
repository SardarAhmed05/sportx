"""
Sports Matches Router
Exposes live fixtures, scoreboards, match stats, and official multi-server stream feeds
across Football (Soccer), Basketball (NBA), American Football (NFL), Motorsport (F1),
Tennis, Combat Sports (UFC), and Baseball (MLB).
"""

from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.services.football_service import (
    get_live_football_matches, 
    get_football_match_by_id,
    resolve_match_replay_servers,
    FOOTBALL_LEAGUES_CONFIG
)
from app.services.sports_engine import universal_sports_engine, SPORTS_CONFIGS
from app.data.football_replays_db import get_all_football_replays
from app.data.multi_sports_replays_db import get_multi_sport_replays, get_sport_replay_categories

router = APIRouter(prefix="/api/matches", tags=["Live Sports Matches"])

@router.get("/overview")
async def get_matches_overview(
    sport: Optional[str] = Query("football", description="Sport identifier (football, basketball, nfl, motorsport, tennis, combat, baseball)"),
    league: Optional[str] = Query(None, description="League ID filter (e.g. epl, nba, nfl, f1)"),
    status: Optional[str] = Query(None, description="Status filter (all, live, upcoming, finished)")
):
    """Returns top featured live matches, marquee match, and active leagues for the requested sport."""
    sport_key = (sport or "football").lower().strip()
    
    # 1. Football (Soccer) - uses our optimized dedicated Football Service
    if sport_key in ["football", "soccer"]:
        football_data = await get_live_football_matches(league_filter=league, status_filter=status)
        football_matches = football_data.get("matches", [])
        
        marquee = next((m for m in football_matches if m.get("status") == "LIVE"), football_matches[0] if football_matches else None)
        total_live = football_data.get("total_live", len(football_matches))
        total_upcoming = football_data.get("total_upcoming", 0)
        total_finished = football_data.get("total_finished", 0)
        total_viewers = sum(m.get("viewers_count", 0) for m in football_matches)
        
        return {
            "sport": "Football",
            "sport_id": "football",
            "marquee_match": marquee,
            "football": football_data,
            "matches": football_data,
            "leagues": FOOTBALL_LEAGUES_CONFIG,
            "total_live": total_live,
            "total_upcoming": total_upcoming,
            "total_finished": total_finished,
            "total_viewers": total_viewers
        }
    
    # 2. Other Sports - Universal Sports Engine
    sport_data = await universal_sports_engine.get_live_sports_matches(sport_key, league_filter=league, status_filter=status)
    sport_matches = sport_data.get("matches", [])
    sport_cfg = universal_sports_engine.get_sport_config(sport_key)
    
    marquee = next((m for m in sport_matches if m.get("status") == "LIVE"), sport_matches[0] if sport_matches else None)
    total_live = sport_data.get("total_live", len(sport_matches))
    total_upcoming = sport_data.get("total_upcoming", 0)
    total_finished = sport_data.get("total_finished", 0)
    total_viewers = sum(m.get("viewers_count", 0) for m in sport_matches)
    
    return {
        "sport": sport_cfg.get("name", sport_key.capitalize()),
        "sport_id": sport_key,
        "marquee_match": marquee,
        "football": sport_data,  # Backwards compatibility so frontend .football.matches works transparently
        "matches": sport_data,
        "leagues": sport_cfg.get("leagues", []),
        "total_live": total_live,
        "total_upcoming": total_upcoming,
        "total_finished": total_finished,
        "total_viewers": total_viewers
    }

@router.get("/football")
async def get_football(
    league: Optional[str] = Query(None, description="League ID filter (e.g. epl, ucl, laliga)"),
    status: Optional[str] = Query(None, description="Status filter (all, live, upcoming, finished)")
):
    """Returns live football matches and leagues."""
    return await get_live_football_matches(league_filter=league, status_filter=status)

@router.get("/detail/{match_id}")
async def get_match_detail(match_id: str):
    """Returns detailed match information (stats, events, and streams) across all sports."""
    # Try Football first
    match = get_football_match_by_id(match_id)
    if match:
        return {"sport": "Football", "match": match}
    
    # Try Universal Sports Engine
    sport_match = universal_sports_engine.get_sport_match_by_id(match_id)
    if sport_match:
        return {"sport": sport_match.get("sport", "Sports"), "match": sport_match}
        
    raise HTTPException(status_code=404, detail="Match not found")

@router.get("/live-streams")
async def get_match_live_streams(
    home: str = Query(..., description="Home team name"),
    away: str = Query(..., description="Away team name"),
    sport: Optional[str] = Query("football", description="Sport name")
):
    """Dynamically resolves real-time live broadcast stream servers for any match."""
    from app.services.live_stream_resolver import live_stream_resolver
    servers = await live_stream_resolver.resolve_match_streams(home, away, sport or "football")
    return {
        "home": home,
        "away": away,
        "sport": sport,
        "servers": servers
    }

@router.get("/replay-streams")
async def get_match_replay_streams(
    home: str = Query(..., description="Home team name"),
    away: str = Query(..., description="Away team name"),
    competition: Optional[str] = Query(None, description="Competition/League name")
):
    """Dynamically resolves real multi-source replay servers (YouTube, Dailymotion, beIN Vault) for this exact match."""
    servers = await resolve_match_replay_servers(home, away, competition or "")
    return {
        "home": home,
        "away": away,
        "competition": competition,
        "servers": servers
    }

@router.get("/replays")
async def get_sports_replays(
    sport: Optional[str] = Query("football", description="Sport identifier (football, basketball, nfl, motorsport, tennis, combat, baseball)"),
    category: Optional[str] = Query(None, description="Category filter"),
    q: Optional[str] = Query(None, description="Search keyword"),
    team: Optional[str] = Query(None, description="Team name filter")
):
    """Returns curated collection of official full match replays, Top 10 Cult Classics, and recent fixtures for any sport."""
    sport_key = (sport or "football").lower().strip()
    
    # 1. FOOTBALL REPLAYS
    if sport_key in ["football", "soccer"]:
        classic_replays = get_all_football_replays(category=category, query=q, team=team)
        
        recent_replays = []
        try:
            fb_data = await get_live_football_matches(status_filter="finished")
            finished_matches = fb_data.get("matches", [])
            finished_matches.sort(key=lambda m: m.get("raw_date", ""), reverse=True)
            
            top_leagues = ["epl", "ucl", "uel", "laliga", "seriea", "bundesliga"]
            top_finished = [m for m in finished_matches if (m.get("league_id") or "").lower() in top_leagues]
            other_finished = [m for m in finished_matches if (m.get("league_id") or "").lower() not in top_leagues]
            curated_finished = (top_finished + other_finished)[:18]
            
            for m in curated_finished:
                lid = (m.get("league_id") or "").lower()
                lname = (m.get("league") or "").lower()
                hname = m.get("home_team", {}).get("name", "").lower()
                aname = m.get("away_team", {}).get("name", "").lower()
                
                categories_list = ["recent"]
                main_category = "recent"
                if lid == "epl" or "premier league" in lname:
                    main_category = "premier_league"
                    categories_list.append("premier_league")
                elif lid in ["ucl", "uel"] or "champions" in lname or "europa" in lname:
                    main_category = "champions_league"
                    categories_list.append("champions_league")
                elif ("madrid" in hname and "barcelona" in aname) or ("barcelona" in hname and "madrid" in aname):
                    main_category = "el_clasico"
                    categories_list.append("el_clasico")

                recent_replays.append({
                    "id": f"recent-{m['id']}",
                    "title": f"{m['home_team']['name']} vs {m['away_team']['name']}",
                    "competition": m.get("league") or "Official Match",
                    "category": main_category,
                    "categories": categories_list,
                    "category_label": m.get("league") or "Recent League Match",
                    "year": 2026,
                    "date": m.get("kickoff_date") or m.get("short_date") or "Recently Completed",
                    "raw_date": m.get("raw_date", ""),
                    "score": f"{m['home_team'].get('score', 0)} - {m['away_team'].get('score', 0)}",
                    "duration": "Official Match Highlights",
                    "thumbnail": m.get("home_team", {}).get("logo") or m.get("away_team", {}).get("logo"),
                    "description": f"Full time result: {m['home_team']['name']} {m['home_team'].get('score', 0)} - {m['away_team'].get('score', 0)} {m['away_team']['name']} in {m.get('league')}. Official verified highlights and key match moments.",
                    "home_team": m.get("home_team"),
                    "away_team": m.get("away_team"),
                    "streams": m.get("streams", []),
                    "is_recent": True
                })
        except Exception:
            pass

        if team and isinstance(team, str) and team.strip():
            t_low = team.lower().strip()
            recent_replays = [
                r for r in recent_replays 
                if t_low in r.get("home_team", {}).get("name", "").lower()
                or t_low in r.get("away_team", {}).get("name", "").lower()
            ]

        if q and isinstance(q, str) and q.strip():
            q_low = q.lower().strip()
            recent_replays = [
                r for r in recent_replays
                if q_low in r.get("title", "").lower()
                or q_low in r.get("competition", "").lower()
                or q_low in r.get("home_team", {}).get("name", "").lower()
                or q_low in r.get("away_team", {}).get("name", "").lower()
            ]

        if category == "cult_classics":
            final_list = [r for r in classic_replays if r.get("is_cult_classic")]
            final_list.sort(key=lambda r: r.get("cult_rank", 99))
        elif category == "recent":
            final_list = recent_replays
        elif category in ["premier_league", "champions_league", "el_clasico"]:
            cat_recent = [r for r in recent_replays if category in r.get("categories", []) or r.get("category") == category]
            cat_classic = [r for r in classic_replays if category in r.get("categories", []) or r.get("category") == category]
            final_list = cat_recent + cat_classic
        elif category in ["world_cup", "euro_copa"]:
            final_list = [r for r in classic_replays if category in r.get("categories", []) or r.get("category") == category]
        else:
            cult = [r for r in classic_replays if r.get("is_cult_classic")]
            cult.sort(key=lambda r: r.get("cult_rank", 99))
            other_classics = [r for r in classic_replays if not r.get("is_cult_classic")]
            final_list = cult + recent_replays + other_classics

        return {
            "sport": "Football",
            "sport_id": "football",
            "total": len(final_list),
            "category": category or "all",
            "replays": final_list,
            "categories": [
                {"id": "all", "label": "All Replays & Classics"},
                {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
                {"id": "recent", "label": "Recent League Matches"},
                {"id": "premier_league", "label": "Premier League"},
                {"id": "champions_league", "label": "Champions League"},
                {"id": "world_cup", "label": "FIFA World Cup"},
                {"id": "euro_copa", "label": "Euro & Copa"},
                {"id": "el_clasico", "label": "El Clásico"}
            ]
        }

    # 2. MULTI-SPORT REPLAYS (Basketball, NFL, Motorsport, Tennis, Combat, Baseball)
    classic_replays = get_multi_sport_replays(sport=sport_key, category=category, query=q, team=team)
    recent_replays = []
    
    try:
        sp_data = await universal_sports_engine.get_live_sports_matches(sport_key, status_filter="finished")
        finished_matches = sp_data.get("matches", [])
        finished_matches.sort(key=lambda m: m.get("raw_date", ""), reverse=True)
        curated_finished = finished_matches[:18]
        
        for m in curated_finished:
            recent_replays.append({
                "id": f"recent-{m['id']}",
                "title": f"{m['home_team']['name']} vs {m['away_team']['name']}",
                "competition": m.get("league") or "Official Match",
                "category": "recent",
                "categories": ["recent"],
                "category_label": m.get("league") or "Recent Match",
                "year": 2026,
                "date": m.get("kickoff_date") or m.get("short_date") or "Recently Completed",
                "raw_date": m.get("raw_date", ""),
                "score": f"{m['home_team'].get('score', 0)} - {m['away_team'].get('score', 0)}",
                "duration": "Official Highlights",
                "thumbnail": m.get("home_team", {}).get("logo") or m.get("away_team", {}).get("logo"),
                "description": f"Official full match recap: {m['home_team']['name']} {m['home_team'].get('score', 0)} - {m['away_team'].get('score', 0)} {m['away_team']['name']} in {m.get('league')}. Verified highlights and key plays.",
                "home_team": m.get("home_team"),
                "away_team": m.get("away_team"),
                "streams": m.get("streams", []),
                "is_recent": True
            })
    except Exception:
        pass

    if team and isinstance(team, str) and team.strip():
        t_low = team.lower().strip()
        recent_replays = [
            r for r in recent_replays 
            if t_low in r.get("home_team", {}).get("name", "").lower()
            or t_low in r.get("away_team", {}).get("name", "").lower()
        ]

    if q and isinstance(q, str) and q.strip():
        q_low = q.lower().strip()
        recent_replays = [
            r for r in recent_replays
            if q_low in r.get("title", "").lower()
            or q_low in r.get("competition", "").lower()
            or q_low in r.get("home_team", {}).get("name", "").lower()
            or q_low in r.get("away_team", {}).get("name", "").lower()
        ]

    if category == "cult_classics":
        final_list = [r for r in classic_replays if r.get("is_cult_classic")]
        final_list.sort(key=lambda r: r.get("cult_rank", 99))
    elif category == "recent":
        final_list = recent_replays
    elif category:
        cat_recent = [r for r in recent_replays if category in r.get("categories", []) or r.get("category") == category]
        cat_classic = [r for r in classic_replays if category in r.get("categories", []) or r.get("category") == category]
        final_list = cat_recent + cat_classic
    else:
        cult = [r for r in classic_replays if r.get("is_cult_classic")]
        cult.sort(key=lambda r: r.get("cult_rank", 99))
        other_classics = [r for r in classic_replays if not r.get("is_cult_classic")]
        final_list = cult + recent_replays + other_classics

    sport_cfg = universal_sports_engine.get_sport_config(sport_key)
    return {
        "sport": sport_cfg.get("name", sport_key.capitalize()),
        "sport_id": sport_key,
        "total": len(final_list),
        "category": category or "all",
        "replays": final_list,
        "categories": get_sport_replay_categories(sport_key)
    }
