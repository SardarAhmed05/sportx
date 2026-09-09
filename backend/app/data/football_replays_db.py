"""
Official Football Replays & Classic Matches Database
Curated collection of historic full match replays, legendary finals, and extended tournament archives.
All sources utilize verified multi-source embeds (YouTube + Dailymotion Mirrors).
Ordered reverse-chronologically (most recent year first).
"""

from typing import List, Dict, Any

FOOTBALL_REPLAYS_CATALOG: List[Dict[str, Any]] = [
    # --- 1. Euro & Copa America 2024 ---
    {
        "id": "replay-euro-2024-esp-eng",
        "title": "UEFA Euro 2024 Final: Spain vs England",
        "competition": "UEFA European Championship 2024",
        "category": "euro_copa",
        "category_label": "Euro & Copa",
        "year": 2024,
        "date": "July 14, 2024",
        "venue": "Olympiastadion, Berlin",
        "score": "2 - 1",
        "duration": "Full Euro Final Highlights & Trophy Lift",
        "thumbnail": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop&q=80",
        "description": "Mikel Oyarzabal pounces in the 86th minute to fire Spain to a record fourth European Championship title over England in Berlin.",
        "is_cult_classic": True,
        "cult_rank": 4,
        "cult_badge": "#4 Euro 2024 Championship Decider",
        "home_team": {
            "name": "Spain",
            "score": 2,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/esp.png"
        },
        "away_team": {
            "name": "England",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/eng.png"
        },
        "streams": [
            {
                "id": "euro24-srv-1",
                "label": "Server 1: Full Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/1vR_M2y3K6w?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=1vR_M2y3K6w",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "euro24-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x924w0u",
                "direct_url": "https://www.dailymotion.com/video/x924w0u",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },
    {
        "id": "replay-copa-2024-arg-col",
        "title": "Copa América 2024 Final: Argentina vs Colombia",
        "competition": "CONMEBOL Copa América 2024",
        "category": "euro_copa",
        "category_label": "Euro & Copa",
        "year": 2024,
        "date": "July 14, 2024",
        "venue": "Hard Rock Stadium, Miami",
        "score": "1 - 0 (AET)",
        "duration": "Full Extra Time Highlights & Celebrations",
        "thumbnail": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80",
        "description": "After an emotional injury to Lionel Messi, Lautaro Martínez enters and nets a sensational 112th-minute extra-time winner to clinch back-to-back Copa crowns.",
        "is_cult_classic": True,
        "cult_rank": 7,
        "cult_badge": "#7 Back-to-Back Copa Champions",
        "home_team": {
            "name": "Argentina",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/arg.png"
        },
        "away_team": {
            "name": "Colombia",
            "score": 0,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/col.png"
        },
        "streams": [
            {
                "id": "copa24-srv-1",
                "label": "Server 1: Official Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "Spanish / English",
                "url": "https://www.youtube-nocookie.com/embed/P_9nUzsB7jU?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=P_9nUzsB7jU",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "copa24-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x924vyu",
                "direct_url": "https://www.dailymotion.com/video/x924vyu",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 2. UEFA Champions League Finals & Classics ---
    {
        "id": "replay-ucl-2023-mci-int",
        "title": "2023 Champions League Final: Manchester City vs Inter Milan",
        "competition": "UEFA Champions League 2022/23",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2023,
        "date": "June 10, 2023",
        "venue": "Atatürk Olympic Stadium, Istanbul",
        "score": "1 - 0",
        "duration": "Full Match Recap & Treble Celebrations",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Rodri's unerring 68th-minute sidefoot finish hands Pep Guardiola's Manchester City their first European Cup and an immortal historic Treble.",
        "is_cult_classic": True,
        "cult_rank": 8,
        "cult_badge": "#8 Man City Treble Complete",
        "home_team": {
            "name": "Manchester City",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"
        },
        "away_team": {
            "name": "Inter Milan",
            "score": 0,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/110.png"
        },
        "streams": [
            {
                "id": "ucl23-srv-1",
                "label": "Server 1: Official UCL Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/AXEG_lagq9E?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=AXEG_lagq9E",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "ucl23-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "English Feed",
                "url": "https://www.dailymotion.com/embed/video/x8lo756",
                "direct_url": "https://www.dailymotion.com/video/x8lo756",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 3. FIFA World Cup 2022 (#1 Greatest Football Match of All Time) ---
    {
        "id": "replay-wc-2022-arg-fra",
        "title": "2022 World Cup Final: Argentina vs France",
        "competition": "FIFA World Cup Qatar 2022",
        "category": "world_cup",
        "category_label": "FIFA World Cup",
        "year": 2022,
        "date": "December 18, 2022",
        "venue": "Lusail Iconic Stadium, Qatar",
        "score": "3 - 3 (4 - 2 pens)",
        "duration": "Full 120 Minutes, All 6 Goals & Penalty Shootout",
        "thumbnail": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80",
        "description": "Widely crowned the greatest football match ever played. Messi's brace and Mbappé's hat-trick in a 3-3 rollercoaster before Argentina triumph on penalties to hand Messi his crowning glory.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Match of All Time",
        "home_team": {
            "name": "Argentina",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/arg.png"
        },
        "away_team": {
            "name": "France",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/fra.png"
        },
        "streams": [
            {
                "id": "wc22-srv-1",
                "label": "Server 1: Full Match Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "English Commentary (Peter Drury)",
                "url": "https://www.youtube-nocookie.com/embed/DDWYR9Oi_wI?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=DDWYR9Oi_wI",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "wc22-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x8gaa1k",
                "direct_url": "https://www.dailymotion.com/video/x8gaa1k",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 4. The Miracle of Istanbul 2005 ---
    {
        "id": "replay-ucl-2005-liv-mil",
        "title": "2005 Champions League Final: Liverpool vs AC Milan (Miracle of Istanbul)",
        "competition": "UEFA Champions League 2004/05",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2005,
        "date": "May 25, 2005",
        "venue": "Atatürk Olympic Stadium, Istanbul",
        "score": "3 - 3 (3 - 2 pens)",
        "duration": "Full 2nd Half Comeback & Dudek Shootout",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 3-0 at half-time against Carlo Ancelotti's star-studded AC Milan, Steven Gerrard inspires Liverpool to score three goals in six minutes before winning on penalties.",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Miracle of Istanbul (3-0 to 3-3)",
        "home_team": {
            "name": "AC Milan",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/103.png"
        },
        "away_team": {
            "name": "Liverpool",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png"
        },
        "streams": [
            {
                "id": "ist05-srv-1",
                "label": "Server 1: Official Istanbul Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p HD",
                "language": "English Commentary (Clive Tyldesley)",
                "url": "https://www.youtube-nocookie.com/embed/3ojXHf293M8?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=3ojXHf293M8",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "ist05-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "English Commentary",
                "url": "https://www.dailymotion.com/embed/video/x19oev1",
                "direct_url": "https://www.dailymotion.com/video/x19oev1",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 5. Corner Taken Quickly 2019 ---
    {
        "id": "replay-ucl-2019-liv-bar",
        "title": "2019 Champions League Semi-Final: Liverpool 4-0 Barcelona",
        "competition": "UEFA Champions League 2018/19",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2019,
        "date": "May 7, 2019",
        "venue": "Anfield, Liverpool",
        "score": "4 - 0 (agg 4 - 3)",
        "duration": "Full Match Recap & 'Corner Taken Quickly, ORIGI!'",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 3-0 from the Camp Nou and without Salah or Firmino, Liverpool produce an Anfield miracle capped by Trent Alexander-Arnold's genius quick corner for Divock Origi.",
        "is_cult_classic": True,
        "cult_rank": 3,
        "cult_badge": "#3 'Corner Taken Quickly... ORIGI!'",
        "home_team": {
            "name": "Liverpool",
            "score": 4,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png"
        },
        "away_team": {
            "name": "Barcelona",
            "score": 0,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/83.png"
        },
        "streams": [
            {
                "id": "liv19-srv-1",
                "label": "Server 1: Full Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/pkEpLtePJm0?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=pkEpLtePJm0",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "liv19-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x77s96a",
                "direct_url": "https://www.dailymotion.com/video/x77s96a",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 6. FIFA World Cup 2018 Final ---
    {
        "id": "replay-wc-2018-fra-cro",
        "title": "2018 World Cup Final: France vs Croatia",
        "competition": "FIFA World Cup Russia 2018",
        "category": "world_cup",
        "category_label": "FIFA World Cup",
        "year": 2018,
        "date": "July 15, 2018",
        "venue": "Luzhniki Stadium, Moscow",
        "score": "4 - 2",
        "duration": "Full 6-Goal Final Highlights & Trophy Lift",
        "thumbnail": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80",
        "description": "Kylian Mbappé becomes the first teenager since Pelé to score in a World Cup final as France overcome a spirited Croatia 4-2 in Moscow.",
        "is_cult_classic": True,
        "cult_rank": 9,
        "cult_badge": "#9 France 2nd World Crown",
        "home_team": {
            "name": "France",
            "score": 4,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/fra.png"
        },
        "away_team": {
            "name": "Croatia",
            "score": 2,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/cro.png"
        },
        "streams": [
            {
                "id": "wc18-srv-1",
                "label": "Server 1: Official Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p HD",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/GrsEAvRerTg?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=GrsEAvRerTg",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "wc18-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x6p43u8",
                "direct_url": "https://www.dailymotion.com/video/x6p43u8",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 7. El Clásico 2017 (Messi 500th Goal Shirt Celebration) ---
    {
        "id": "replay-clasico-2017-rm-fcb",
        "title": "2017 El Clásico: Real Madrid 2-3 Barcelona (Messi 500th Goal)",
        "competition": "La Liga 2016/17",
        "category": "el_clasico",
        "category_label": "El Clásico",
        "year": 2017,
        "date": "April 23, 2017",
        "venue": "Santiago Bernabéu, Madrid",
        "score": "2 - 3",
        "duration": "Full 5-Goal Thriller & 92nd Minute Winner",
        "thumbnail": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800&auto=format&fit=crop&q=80",
        "description": "With the final kick of the match in the 92nd minute, Lionel Messi slots home his 500th Barcelona goal and holds his jersey aloft in front of a stunned Santiago Bernabéu.",
        "is_cult_classic": True,
        "cult_rank": 5,
        "cult_badge": "#5 Messi's Immortal 500th Goal",
        "home_team": {
            "name": "Real Madrid",
            "score": 2,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png"
        },
        "away_team": {
            "name": "Barcelona",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/83.png"
        },
        "streams": [
            {
                "id": "clas17-srv-1",
                "label": "Server 1: Official Highlights (YouTube)",
                "network": "LaLiga Player",
                "quality": "1080p 60fps",
                "language": "Spanish / English",
                "url": "https://www.youtube-nocookie.com/embed/fVufY4SCoOk?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=fVufY4SCoOk",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "clas17-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "International Feed",
                "url": "https://www.dailymotion.com/embed/video/x5j9vzk",
                "direct_url": "https://www.dailymotion.com/video/x5j9vzk",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 8. La Remontada 2017 ---
    {
        "id": "replay-ucl-2017-fcb-psg",
        "title": "2017 Champions League: Barcelona 6-1 PSG ('La Remontada')",
        "competition": "UEFA Champions League 2016/17",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2017,
        "date": "March 8, 2017",
        "venue": "Camp Nou, Barcelona",
        "score": "6 - 1 (agg 6 - 5)",
        "duration": "Three Goals After 88th Minute & Sergi Roberto Winner",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Overturning a 4-0 first-leg deficit, Barcelona score three goals in the final seven minutes, culminating in Sergi Roberto's 95th-minute volley to complete the greatest comeback in UCL history.",
        "is_cult_classic": True,
        "cult_rank": 6,
        "cult_badge": "#6 Greatest Comeback in UCL History",
        "home_team": {
            "name": "Barcelona",
            "score": 6,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/83.png"
        },
        "away_team": {
            "name": "Paris Saint-Germain",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/160.png"
        },
        "streams": [
            {
                "id": "rem17-srv-1",
                "label": "Server 1: Official Match Highlights (YouTube)",
                "network": "YouTube Player",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/h4m68r8kWAc?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=h4m68r8kWAc",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "rem17-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "French / English",
                "url": "https://www.dailymotion.com/embed/video/x5ecq3q",
                "direct_url": "https://www.dailymotion.com/video/x5ecq3q",
                "is_embed": True,
                "is_primary": False
            }
        ]
    },

    # --- 9. AGÜEROOOO 2012 ---
    {
        "id": "replay-pl-2012-mci-qpr",
        "title": "2012 Premier League: Manchester City 3-2 QPR ('93:20 Aguerooo!')",
        "competition": "Premier League 2011/12",
        "category": "premier_league",
        "category_label": "Premier League",
        "year": 2012,
        "date": "May 13, 2012",
        "venue": "Etihad Stadium, Manchester",
        "score": "3 - 2",
        "duration": "Stoppage Time Drama - Dzeko 91' & Aguero 93:20",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 2-1 in the 91st minute with the title slipping to rivals Man United, City score twice in stoppage time as Sergio Agüero blasts home the title-winning goal at 93:20.",
        "is_cult_classic": True,
        "cult_rank": 10,
        "cult_badge": "#10 'I Swear You\'ll Never See Anything Like This!'",
        "home_team": {
            "name": "Manchester City",
            "score": 3,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"
        },
        "away_team": {
            "name": "Queens Park Rangers",
            "score": 2,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/334.png"
        },
        "streams": [
            {
                "id": "agu12-srv-1",
                "label": "Server 1: Official Premier League Highlights (YouTube)",
                "network": "Premier League Player",
                "quality": "1080p 60fps",
                "language": "English (Martin Tyler)",
                "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1",
                "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU",
                "is_embed": True,
                "is_primary": True
            },
            {
                "id": "agu12-srv-2",
                "label": "Server 2: Dailymotion HD Mirror",
                "network": "Dailymotion Video",
                "quality": "1080p HD",
                "language": "English Commentary",
                "url": "https://www.dailymotion.com/embed/video/xqtd5c",
                "direct_url": "https://www.dailymotion.com/video/xqtd5c",
                "is_embed": True,
                "is_primary": False
            }
        ]
    }
]

def get_all_football_replays(category: str = None, query: str = None, team: str = None) -> List[Dict[str, Any]]:
    """Returns curated football replays with optional category, search, and team filters."""
    catalog = list(FOOTBALL_REPLAYS_CATALOG)
    
    if category and category.lower() != "all":
        cat_lower = category.lower().strip()
        if cat_lower == "cult_classics":
            catalog = [r for r in catalog if r.get("is_cult_classic")]
            catalog.sort(key=lambda r: r.get("cult_rank", 99))
        else:
            catalog = [r for r in catalog if r.get("category") == cat_lower or cat_lower in r.get("categories", [])]
        
    if query and query.strip():
        q = query.lower().strip()
        catalog = [
            r for r in catalog 
            if q in r.get("title", "").lower() 
            or q in r.get("competition", "").lower()
            or q in r.get("description", "").lower()
            or q in r.get("home_team", {}).get("name", "").lower()
            or q in r.get("away_team", {}).get("name", "").lower()
            or q in str(r.get("year", ""))
        ]
        
    if team and team.strip():
        t = team.lower().strip()
        catalog = [
            r for r in catalog
            if t in r.get("home_team", {}).get("name", "").lower()
            or t in r.get("away_team", {}).get("name", "").lower()
        ]
        
    return catalog

def find_replays_for_match(home_team: str, away_team: str) -> List[Dict[str, Any]]:
    """Matches a live or upcoming fixture against historical classic replays database."""
    h = home_team.lower().strip()
    a = away_team.lower().strip()
    
    matches = []
    for r in FOOTBALL_REPLAYS_CATALOG:
        rh = r["home_team"]["name"].lower()
        ra = r["away_team"]["name"].lower()
        
        if (h in rh and a in ra) or (a in rh and h in ra):
            matches.append(r)
            continue
            
        h_tokens = set(h.split())
        a_tokens = set(a.split())
        rh_tokens = set(rh.split())
        ra_tokens = set(ra.split())
        
        if (h_tokens & rh_tokens and a_tokens & ra_tokens) or (a_tokens & rh_tokens and h_tokens & ra_tokens):
            matches.append(r)
            
    return matches
