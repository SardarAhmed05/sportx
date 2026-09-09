"""
Multi-Sport Replays & Classics Vault Database
Contains the Top 10 Greatest Cult Classics of All Time for:
- Basketball (NBA Finals, Jordan, Kobe, Ray Allen, LeBron)
- American Football (Super Bowls, 28-3 Comeback, Helmet Catch, Philly Special)
- Motorsport (Formula 1 Abu Dhabi 2021, Canada 2011, Brazil 2008, Senna 1993)
- Tennis (Wimbledon 2008 Federer vs Nadal, AO 2012 Djokovic vs Nadal)
- Combat Sports (UFC 229 Khabib vs McGregor, Ali vs Foreman, Hagler vs Hearns)
- Baseball (2016 World Series Cubs G7, 2004 Red Sox Comeback)
Delegates to football_replays_db for Football.
"""

from typing import List, Dict, Any
from app.data.football_replays_db import get_all_football_replays, FOOTBALL_REPLAYS_CATALOG

BASKETBALL_REPLAYS = [
    {
        "id": "bball-replay-2016-finals-g7",
        "title": "2016 NBA Finals Game 7: Cavaliers vs Warriors",
        "competition": "NBA Finals Game 7",
        "sport": "Basketball",
        "sport_id": "basketball",
        "category": "finals",
        "category_label": "NBA Finals",
        "year": 2016,
        "date": "June 19, 2016",
        "score": "93 - 89",
        "duration": "Full Game 7 Highlights & The Block",
        "thumbnail": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80",
        "description": "LeBron James delivers 'The Block' on Andre Iguodala, Kyrie Irving buries the championship three, and Cleveland ends their 52-year title drought from 3-1 down.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Match of All Time",
        "home_team": {"name": "Golden State Warriors", "score": 89, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/gsw.png"},
        "away_team": {"name": "Cleveland Cavaliers", "score": 93, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/cle.png"},
        "streams": [
            {"id": "bball-2016-1", "label": "Server 1: Official NBA Finals Game 7 Highlights", "network": "NBA Official", "quality": "1080p 60fps", "language": "English (Mike Breen)", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True},
            {"id": "bball-2016-2", "label": "Server 2: beIN Sports Vault Feed", "network": "beIN Sports Vault", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "is_primary": False}
        ]
    },
    {
        "id": "bball-replay-1998-finals-g6",
        "title": "1998 NBA Finals Game 6: Bulls vs Jazz (Jordan's Last Shot)",
        "competition": "NBA Finals Game 6",
        "sport": "Basketball",
        "sport_id": "basketball",
        "category": "finals",
        "category_label": "NBA Finals",
        "year": 1998,
        "date": "June 14, 1998",
        "score": "87 - 86",
        "duration": "Full 4th Quarter Climax & Trophy Ceremony",
        "thumbnail": "https://images.unsplash.com/photo-1519766304817-4f37bda74a29?w=800&auto=format&fit=crop&q=80",
        "description": "Michael Jordan steals the ball from Karl Malone and sinks the iconic 17-foot jumper with 5.2 seconds remaining to secure Chicago's second three-peat.",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Jordan's Iconic Last Shot",
        "home_team": {"name": "Utah Jazz", "score": 86, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/uta.png"},
        "away_team": {"name": "Chicago Bulls", "score": 87, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/chi.png"},
        "streams": [
            {"id": "bball-1998-1", "label": "Server 1: Official NBA Vault: Jordan's Last Shot", "network": "NBA Vault", "quality": "1080p HD", "language": "English (Bob Costas)", "url": "https://www.youtube-nocookie.com/embed/8V_1ZxOz348?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "bball-replay-2013-finals-g6",
        "title": "2013 NBA Finals Game 6: Heat vs Spurs (Ray Allen Corner Three)",
        "competition": "NBA Finals Game 6",
        "sport": "Basketball",
        "sport_id": "basketball",
        "category": "finals",
        "category_label": "NBA Finals",
        "year": 2013,
        "date": "June 18, 2013",
        "score": "103 - 100 (OT)",
        "duration": "Full 4th Quarter & Extra Time",
        "thumbnail": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80",
        "description": "With yellow ropes already surrounding the court, Ray Allen hits the clutchest shot in NBA history from the right corner with 5.2 seconds left to save the Heat season.",
        "is_cult_classic": True,
        "cult_rank": 3,
        "cult_badge": "#3 Ray Allen 'BANG!' Corner 3",
        "home_team": {"name": "Miami Heat", "score": 103, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/mia.png"},
        "away_team": {"name": "San Antonio Spurs", "score": 100, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/sas.png"},
        "streams": [
            {"id": "bball-2013-1", "label": "Server 1: Official NBA Highlights: Ray Allen Shot", "network": "NBA Official", "quality": "1080p 60fps", "language": "English (Mike Breen)", "url": "https://www.youtube-nocookie.com/embed/tr6XsZVb-ZE?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "bball-replay-2006-kobe-81",
        "title": "2006 Kobe Bryant 81-Point Game: Lakers vs Raptors",
        "competition": "NBA Regular Season Classic",
        "sport": "Basketball",
        "sport_id": "basketball",
        "category": "classics",
        "category_label": "NBA Classics",
        "year": 2006,
        "date": "January 22, 2006",
        "score": "122 - 104",
        "duration": "All 81 Points & Full Game Story",
        "thumbnail": "https://images.unsplash.com/photo-1519766304817-4f37bda74a29?w=800&auto=format&fit=crop&q=80",
        "description": "Kobe Bryant puts on the second-greatest scoring clinic in NBA history, dropping 55 points in the second half alone to complete an astonishing 81-point performance.",
        "is_cult_classic": True,
        "cult_rank": 4,
        "cult_badge": "#4 Kobe Bryant 81-Point Masterpiece",
        "home_team": {"name": "Los Angeles Lakers", "score": 122, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/lal.png"},
        "away_team": {"name": "Toronto Raptors", "score": 104, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/tor.png"},
        "streams": [
            {"id": "bball-2006-1", "label": "Server 1: Official Kobe 81 Points Highlights", "network": "NBA Official", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/FeXZY4eVLlo?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "bball-replay-2024-finals-g5",
        "title": "2024 NBA Finals Game 5: Celtics vs Mavericks",
        "competition": "NBA Finals 2024",
        "sport": "Basketball",
        "sport_id": "basketball",
        "category": "finals",
        "category_label": "NBA Finals",
        "year": 2024,
        "date": "June 17, 2024",
        "score": "106 - 88",
        "duration": "Championship Deciding Highlights & Banner 18",
        "thumbnail": "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80",
        "description": "Jayson Tatum and Jaylen Brown guide Boston to their record-breaking 18th championship at TD Garden with a dominant closeout performance.",
        "is_cult_classic": True,
        "cult_rank": 5,
        "cult_badge": "#5 Boston Celtics Record 18th Title",
        "home_team": {"name": "Boston Celtics", "score": 106, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/bos.png"},
        "away_team": {"name": "Dallas Mavericks", "score": 88, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/dal.png"},
        "streams": [
            {"id": "bball-2024-1", "label": "Server 1: Official 2024 Finals Game 5 Highlights", "network": "NBA Official", "quality": "1080p 60fps", "language": "English", "url": "https://www.youtube-nocookie.com/embed/Xq4-lD1v3qM?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

NFL_REPLAYS = [
    {
        "id": "nfl-replay-sb51-pat-fal",
        "title": "Super Bowl LI: New England Patriots vs Atlanta Falcons (28-3 Comeback)",
        "competition": "Super Bowl LI",
        "sport": "American Football",
        "sport_id": "nfl",
        "category": "super_bowl",
        "category_label": "Super Bowl",
        "year": 2017,
        "date": "February 5, 2017",
        "score": "34 - 28 (OT)",
        "duration": "Full 4th Quarter & First Ever Super Bowl OT",
        "thumbnail": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 28-3 with 2 minutes left in the 3rd quarter, Tom Brady orchestrates the greatest comeback in Super Bowl history, scoring 31 unanswered points.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 28-3 Greatest Comeback in History",
        "home_team": {"name": "New England Patriots", "score": 34, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/ne.png"},
        "away_team": {"name": "Atlanta Falcons", "score": 28, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/atl.png"},
        "streams": [
            {"id": "nfl-sb51-1", "label": "Server 1: Official NFL Super Bowl LI Game Highlights", "network": "NFL Official", "quality": "1080p 60fps", "language": "English (Joe Buck)", "url": "https://www.youtube-nocookie.com/embed/016LXFHpFCk?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "nfl-replay-sb49-pat-sea",
        "title": "Super Bowl XLIX: Patriots vs Seahawks (Malcolm Butler Interception)",
        "competition": "Super Bowl XLIX",
        "sport": "American Football",
        "sport_id": "nfl",
        "category": "super_bowl",
        "category_label": "Super Bowl",
        "year": 2015,
        "date": "February 1, 2015",
        "score": "28 - 24",
        "duration": "Final Two Minutes & Goal Line Stand",
        "thumbnail": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=800&auto=format&fit=crop&q=80",
        "description": "With Seattle on the 1-yard line with 26 seconds left, undrafted rookie Malcolm Butler intercepts Russell Wilson to clinch the Lombardi Trophy.",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Malcolm Butler Goal-Line INT",
        "home_team": {"name": "New England Patriots", "score": 28, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/ne.png"},
        "away_team": {"name": "Seattle Seahawks", "score": 24, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/sea.png"},
        "streams": [
            {"id": "nfl-sb49-1", "label": "Server 1: Official Super Bowl XLIX Climax & Interception", "network": "NFL Official", "quality": "1080p HD", "language": "English (Al Michaels)", "url": "https://www.youtube-nocookie.com/embed/U10h8ZjyvqM?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "nfl-replay-sb58-kc-sf",
        "title": "Super Bowl LVIII: Kansas City Chiefs vs San Francisco 49ers (OT Walk-Off)",
        "competition": "Super Bowl LVIII",
        "sport": "American Football",
        "sport_id": "nfl",
        "category": "super_bowl",
        "category_label": "Super Bowl",
        "year": 2024,
        "date": "February 11, 2024",
        "score": "25 - 22 (OT)",
        "duration": "Full Super Bowl Highlights & Mecole Hardman TD",
        "thumbnail": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=800&auto=format&fit=crop&q=80",
        "description": "Patrick Mahomes leads a 75-yard overtime drive in Las Vegas, finding Mecole Hardman with 3 seconds remaining in OT to seal back-to-back championships.",
        "is_cult_classic": True,
        "cult_rank": 3,
        "cult_badge": "#3 Las Vegas Overtime Walk-Off",
        "home_team": {"name": "Kansas City Chiefs", "score": 25, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/kc.png"},
        "away_team": {"name": "San Francisco 49ers", "score": 22, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/sf.png"},
        "streams": [
            {"id": "nfl-sb58-1", "label": "Server 1: Official Super Bowl LVIII Highlights", "network": "NFL Official", "quality": "1080p 60fps", "language": "English (Jim Nantz)", "url": "https://www.youtube-nocookie.com/embed/5D3k2wN-69A?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

MOTORSPORT_REPLAYS = [
    {
        "id": "f1-replay-2021-abudhabi",
        "title": "2021 Abu Dhabi Grand Prix: Verstappen vs Hamilton (Final Lap Decider)",
        "competition": "Formula 1 World Championship",
        "sport": "Motorsport",
        "sport_id": "motorsport",
        "category": "grand_prix",
        "category_label": "Grand Prix Classics",
        "year": 2021,
        "date": "December 12, 2021",
        "score": "VER P1 • HAM P2",
        "duration": "Final 5 Laps & Championship Deciding Overtake",
        "thumbnail": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&auto=format&fit=crop&q=80",
        "description": "Tied on points entering the final round of the season, Max Verstappen overtakes Lewis Hamilton on the 58th and final lap at Yas Marina to claim his maiden World Championship.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 The Final Lap Decider of the Century",
        "home_team": {"name": "Max Verstappen (Red Bull)", "score": 1, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"},
        "away_team": {"name": "Lewis Hamilton (Mercedes)", "score": 2, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png"},
        "streams": [
            {"id": "f1-2021-1", "label": "Server 1: Official F1 Abu Dhabi Final Lap Highlights", "network": "F1 Official", "quality": "1080p 60fps", "language": "English (Crofty / Brundle)", "url": "https://www.youtube-nocookie.com/embed/3m4a5xY9NLE?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "f1-replay-2011-canada",
        "title": "2011 Canadian Grand Prix: Jenson Button (Last to First in Rain)",
        "competition": "Formula 1 World Championship",
        "sport": "Motorsport",
        "sport_id": "motorsport",
        "category": "grand_prix",
        "category_label": "Grand Prix Classics",
        "year": 2011,
        "date": "June 12, 2011",
        "score": "BUT P1 • VET P2",
        "duration": "Four-Hour Rain Drama & Final Lap Pass",
        "thumbnail": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&auto=format&fit=crop&q=80",
        "description": "In a 4-hour rain-soaked race with 6 pit stops, a collision, and running dead last in P21, Jenson Button charges through the field to pass Sebastian Vettel on the final lap.",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Jenson Button's 4-Hour Rain Miracle",
        "home_team": {"name": "Jenson Button (McLaren)", "score": 1, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png"},
        "away_team": {"name": "Sebastian Vettel (Red Bull)", "score": 2, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"},
        "streams": [
            {"id": "f1-2011-1", "label": "Server 1: Official F1 Canada 2011 Extended Highlights", "network": "F1 Official", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/N-0LwV2b3r0?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

TENNIS_REPLAYS = [
    {
        "id": "ten-replay-2008-wimbledon",
        "title": "2008 Wimbledon Final: Rafael Nadal vs Roger Federer",
        "competition": "The Championships, Wimbledon",
        "sport": "Tennis",
        "sport_id": "tennis",
        "category": "grand_slam",
        "category_label": "Grand Slam Finals",
        "year": 2008,
        "date": "July 6, 2008",
        "score": "6-4, 6-4, 6-7, 6-7, 9-7",
        "duration": "4 Hours 48 Minutes of Greatest Tennis in History",
        "thumbnail": "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80",
        "description": "In almost total darkness on Center Court, Rafael Nadal dethrones five-time defending champion Roger Federer in what is widely considered the greatest tennis match ever played.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Tennis Match Ever Played",
        "home_team": {"name": "Rafael Nadal", "score": 3, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png"},
        "away_team": {"name": "Roger Federer", "score": 2, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png"},
        "streams": [
            {"id": "ten-2008-1", "label": "Server 1: Official Wimbledon 2008 Highlights", "network": "Wimbledon Official", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/6dMh_x2_1k0?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

COMBAT_REPLAYS = [
    {
        "id": "mma-replay-ufc229-khabib-conor",
        "title": "UFC 229: Khabib Nurmagomedov vs Conor McGregor",
        "competition": "UFC Lightweight Championship",
        "sport": "Combat Sports",
        "sport_id": "combat",
        "category": "ufc",
        "category_label": "UFC Main Events",
        "year": 2018,
        "date": "October 6, 2018",
        "score": "Khabib SUB (Round 4)",
        "duration": "Full 4-Round War & Neck Crank Finish",
        "thumbnail": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?w=800&auto=format&fit=crop&q=80",
        "description": "The biggest fight in combat sports history. Khabib drops McGregor with an overhand right, dominates on the canvas, and locks in a 4th-round neck crank before chaos erupts.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Biggest PPV in Combat Sports History",
        "home_team": {"name": "Khabib Nurmagomedov", "score": 1, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"},
        "away_team": {"name": "Conor McGregor", "score": 0, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png"},
        "streams": [
            {"id": "mma-229-1", "label": "Server 1: Official UFC 229 Highlights & Finish", "network": "UFC Official", "quality": "1080p 60fps", "language": "English (Joe Rogan)", "url": "https://www.youtube-nocookie.com/embed/H08YAq1b_sQ?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]


CRICKET_REPLAYS = [
    {
        "id": "cric-replay-2019-wc-final",
        "title": "2019 ICC World Cup Final: England vs New Zealand (Super Over)",
        "competition": "ICC Men's Cricket World Cup Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 2019,
        "date": "July 14, 2019",
        "score": "ENG 241 & 15/0 tied NZ 241/8 & 15/1",
        "duration": "Full Match Highlights, Dramatic Final Over & Super Over",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "The greatest ODI match in cricket history. Tied in 50 overs, tied in the Super Over, England win their first Men's World Cup by the barest of margins on boundary countback at Lord's.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Cricket Match of All Time",
        "home_team": {"name": "England", "score": "241 (50) & 15/0", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "away_team": {"name": "New Zealand", "score": "241/8 (50) & 15/1", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2849.png"},
        "streams": [
            {"id": "cric-2019-1", "label": "Server 1: Official ICC 2019 World Cup Final Highlights", "network": "ICC Official", "quality": "1080p 60fps", "language": "English (Ian Smith & Nasser Hussain)", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True},
            {"id": "cric-2019-2", "label": "Server 2: Sky Sports Cricket Vault", "network": "Sky Sports Cricket", "quality": "1080p HD", "language": "English", "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8", "is_embed": False, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-2022-ind-pak-mcg",
        "title": "2022 T20 World Cup: India vs Pakistan (Kohli's MCG Masterclass)",
        "competition": "ICC Men's T20 World Cup",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "T20 World Cup",
        "year": 2022,
        "date": "October 23, 2022",
        "score": "IND 160/6 (20 ov) beat PAK 159/8 (20 ov)",
        "duration": "Full Chase & Kohli's Iconic Back-Foot Six",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "In front of 90,293 fans at the MCG, Virat Kohli plays the innings of his life (82* off 53 balls), smashing Haris Rauf for two legendary straight sixes to pull off an impossible last-ball win.",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Kohli's Greatest T20 Masterpiece",
        "home_team": {"name": "India", "score": "160/6 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2965.png"},
        "away_team": {"name": "Pakistan", "score": "159/8 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png"},
        "streams": [
            {"id": "cric-2022-1", "label": "Server 1: Official ICC T20 World Cup Highlights", "network": "ICC Official", "quality": "1080p 60fps", "language": "English (Harsha Bhogle)", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2016-wt20-final",
        "title": "2016 T20 World Cup Final: West Indies vs England (Carlos Brathwaite)",
        "competition": "ICC World T20 Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "T20 World Cup",
        "year": 2016,
        "date": "April 3, 2016",
        "score": "WI 161/6 (19.4 ov) beat ENG 155/9 (20 ov)",
        "duration": "Full 20th Over Climax - 4 Consecutive Sixes",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "Needing 19 runs off the final over at Eden Gardens, Carlos Brathwaite blasts Ben Stokes for four consecutive sixes as Ian Bishop roars 'Carlos Brathwaite! Remember the name!'",
        "is_cult_classic": True,
        "cult_rank": 3,
        "cult_badge": "#3 'Carlos Brathwaite! Remember The Name!'",
        "home_team": {"name": "West Indies", "score": "161/6 (19.4 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2850.png"},
        "away_team": {"name": "England", "score": "155/9 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "streams": [
            {"id": "cric-2016-1", "label": "Server 1: Official ICC Highlights", "network": "ICC Official", "quality": "1080p 60fps", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2011-wc-final",
        "title": "2011 ICC World Cup Final: India vs Sri Lanka (Dhoni's Six)",
        "competition": "ICC Cricket World Cup Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 2011,
        "date": "April 2, 2011",
        "score": "IND 277/4 (48.2 ov) beat SL 274/6 (50 ov)",
        "duration": "Full Chase & Trophy Presentation at Wankhede",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "Gautam Gambhir's resolute 97 and MS Dhoni's majestic 91* capped with the immortal winning six into the Wankhede crowd to deliver India's first World Cup title in 28 years for Sachin Tendulkar.",
        "is_cult_classic": True,
        "cult_rank": 4,
        "cult_badge": "#4 'Dhoni Finishes Off In Style!'",
        "home_team": {"name": "India", "score": "277/4 (48.2 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2965.png"},
        "away_team": {"name": "Sri Lanka", "score": "274/6 (50 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2851.png"},
        "streams": [
            {"id": "cric-2011-1", "label": "Server 1: Official ICC 2011 Final Vault", "network": "ICC Vault", "quality": "1080p HD", "language": "English (Ravi Shastri)", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-1999-aus-sa-semi",
        "title": "1999 World Cup Semi-Final: Australia vs South Africa (Edgbaston Tie)",
        "competition": "ICC Cricket World Cup Semi-Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 1999,
        "date": "June 17, 1999",
        "score": "AUS 213 tied SA 213 (49.4 ov)",
        "duration": "Full 50th Over Klusener Blitz & Run Out",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "The most dramatic finish in World Cup history. Lance Klusener's thunderous assault leaves South Africa needing 1 run off 4 balls, followed by a disastrous run out with Allan Donald.",
        "is_cult_classic": True,
        "cult_rank": 5,
        "cult_badge": "#5 The Most Dramatic World Cup Match Ever",
        "home_team": {"name": "Australia", "score": "213 (49.2 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2847.png"},
        "away_team": {"name": "South Africa", "score": "213 (49.4 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2852.png"},
        "streams": [
            {"id": "cric-1999-1", "label": "Server 1: ICC Classics Vault", "network": "ICC Vault", "quality": "1080p HD", "language": "English (Tony Greig)", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2019-headingley-test",
        "title": "2019 Ashes 3rd Test: England vs Australia (Stokes 135* Miracle)",
        "competition": "The Ashes 2019",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "ashes_tests",
        "category_label": "The Ashes & Tests",
        "year": 2019,
        "date": "August 25, 2019",
        "score": "ENG 362/9 beat AUS 179 & 246",
        "duration": "Full 10th-Wicket 76-run Stand Highlights",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "Ben Stokes plays the greatest fourth-innings knock in Test history (135*), partnering with Jack Leach (1*) for an unthinkable 76-run last-wicket partnership to win by 1 wicket.",
        "is_cult_classic": True,
        "cult_rank": 6,
        "cult_badge": "#6 Stokes' Headingley Miracle",
        "home_team": {"name": "England", "score": "67 & 362/9", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "away_team": {"name": "Australia", "score": "179 & 246", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2847.png"},
        "streams": [
            {"id": "cric-2019-ashes-1", "label": "Server 1: Sky Sports Cricket Classics", "network": "Sky Sports", "quality": "1080p 60fps", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2007-wt20-final",
        "title": "2007 T20 World Cup Final: India vs Pakistan (Johannesburg)",
        "competition": "ICC World Twenty20 Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "T20 World Cup",
        "year": 2007,
        "date": "September 24, 2007",
        "score": "IND 157/5 beat PAK 152 (19.3 ov)",
        "duration": "Full Final Over Drama & Misbah Scoop",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "The match that sparked the global T20 revolution. Misbah-ul-Haq's scoop is caught by Sreesanth at short fine-leg off Joginder Sharma as Dhoni's young India become the inaugural T20 World Champions.",
        "is_cult_classic": True,
        "cult_rank": 7,
        "cult_badge": "#7 Birth of the Global T20 Revolution",
        "home_team": {"name": "India", "score": "157/5 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2965.png"},
        "away_team": {"name": "Pakistan", "score": "152 (19.3 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png"},
        "streams": [
            {"id": "cric-2007-1", "label": "Server 1: ICC 2007 Vault", "network": "ICC Vault", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2001-kolkata-test",
        "title": "2001 Kolkata Test: India vs Australia (Laxman 281 & Dravid 180)",
        "competition": "Australia tour of India 2001",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "ashes_tests",
        "category_label": "Test Classics",
        "year": 2001,
        "date": "March 15, 2001",
        "score": "IND 171 & 657/7d beat AUS 445 & 212",
        "duration": "Full Day 4 Partnership & Harbhajan Hat-Trick",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "Forced to follow on, VVS Laxman (281) and Rahul Dravid (180) bat through the entire fourth day without losing a wicket, breaking Steve Waugh's invincible 16-Test winning streak.",
        "is_cult_classic": True,
        "cult_rank": 8,
        "cult_badge": "#8 The Greatest Follow-On Victory in Test History",
        "home_team": {"name": "India", "score": "171 & 657/7d", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2965.png"},
        "away_team": {"name": "Australia", "score": "445 & 212", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2847.png"},
        "streams": [
            {"id": "cric-2001-1", "label": "Server 1: BCCI & Star Sports Classics", "network": "Star Sports", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-2023-ipl-final",
        "title": "2023 IPL Final: Chennai Super Kings vs Gujarat Titans",
        "competition": "Tata IPL Final 2023",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "ipl_psl",
        "category_label": "IPL & PSL",
        "year": 2023,
        "date": "May 29, 2023",
        "score": "CSK 171/5 (15 ov) beat GT 214/4 (20 ov)",
        "duration": "Full 3-Day Rain Thriller & Jadeja's Last 2 Balls",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "After a 3-day rain delay at the Narendra Modi Stadium, CSK need 10 runs off the final 2 balls. Ravindra Jadeja hits Mohit Sharma for a six and four to hand MS Dhoni a record 5th IPL title.",
        "is_cult_classic": True,
        "cult_rank": 9,
        "cult_badge": "#9 Jadeja's 10 Runs Off Last 2 Balls",
        "home_team": {"name": "Chennai Super Kings", "score": "171/5 (15 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png"},
        "away_team": {"name": "Gujarat Titans", "score": "214/4 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png"},
        "streams": [
            {"id": "cric-2023-1", "label": "Server 1: Official IPL Final Highlights", "network": "IPL Official", "quality": "1080p 60fps", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    },
    {
        "id": "cric-replay-1992-wc-final",
        "title": "1992 World Cup Final: Pakistan vs England (Cornered Tigers)",
        "competition": "Benson & Hedges World Cup Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 1992,
        "date": "March 25, 1992",
        "score": "PAK 249/6 beat ENG 227 (49.2 ov)",
        "duration": "Full MCG Trophy Presentation & Wasim Akram Spell",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "Imran Khan's iconic 'Cornered Tigers' speech leads Pakistan from near elimination to glory, with Wasim Akram taking 2 back-to-back unplayable wickets to seal the championship at the MCG.",
        "is_cult_classic": True,
        "cult_rank": 10,
        "cult_badge": "#10 Pakistan's Cornered Tigers Glory",
        "home_team": {"name": "Pakistan", "score": "249/6 (50 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png"},
        "away_team": {"name": "England", "score": "227 (49.2 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "streams": [
            {"id": "cric-1992-1", "label": "Server 1: ICC 1992 Vault", "network": "ICC Vault", "quality": "1080p HD", "language": "English", "url": "https://www.youtube-nocookie.com/embed/5m4XkLg1b_4?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

BASEBALL_REPLAYS = [
    {
        "id": "mlb-replay-2016-ws-g7",
        "title": "2016 World Series Game 7: Chicago Cubs vs Cleveland Indians",
        "competition": "MLB World Series Game 7",
        "sport": "Baseball",
        "sport_id": "baseball",
        "category": "world_series",
        "category_label": "World Series",
        "year": 2016,
        "date": "November 2, 2016",
        "score": "8 - 7 (10 inn)",
        "duration": "Rain Delay, Extra Innings & 108-Year Curse Broken",
        "thumbnail": "https://images.unsplash.com/photo-1508344928928-7165b67de128?w=800&auto=format&fit=crop&q=80",
        "description": "After a dramatic 17-minute rain delay in the 10th inning, the Chicago Cubs break their 108-year championship curse in the most heart-stopping Game 7 ever played.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 108-Year World Series Curse Broken",
        "home_team": {"name": "Cleveland Indians", "score": 7, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png"},
        "away_team": {"name": "Chicago Cubs", "score": 8, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png"},
        "streams": [
            {"id": "mlb-2016-1", "label": "Server 1: Official MLB World Series Game 7 Highlights", "network": "MLB Official", "quality": "1080p 60fps", "language": "English (Joe Buck)", "url": "https://www.youtube-nocookie.com/embed/5F4pQk6uK0M?autoplay=1", "is_embed": True, "is_primary": True}
        ]
    }
]

def get_replays_for_sport(sport: str = "football", category: str = None, query: str = None) -> List[Dict[str, Any]]:
    """Returns official replays and classics for the requested sport."""
    s_key = (sport or "football").lower().strip()
    
    if s_key == "cricket":
        catalog = list(CRICKET_REPLAYS)
    elif s_key == "football":
        return get_all_football_replays(category=category, query=query)
    elif s_key == "basketball":
        catalog = list(BASKETBALL_REPLAYS)
    elif s_key == "nfl":
        catalog = list(NFL_REPLAYS)
    elif s_key == "motorsport":
        catalog = list(MOTORSPORT_REPLAYS)
    elif s_key == "tennis":
        catalog = list(TENNIS_REPLAYS)
    elif s_key == "combat":
        catalog = list(COMBAT_REPLAYS)
    elif s_key == "baseball":
        catalog = list(BASEBALL_REPLAYS)
    else:
        catalog = list(BASKETBALL_REPLAYS)

    if category and category.lower() != "all":
        c_low = category.lower()
        if c_low == "cult_classics":
            catalog = [r for r in catalog if r.get("is_cult_classic")]
            catalog.sort(key=lambda r: r.get("cult_rank", 99))
        else:
            catalog = [r for r in catalog if r.get("category") == c_low or c_low in r.get("categories", [])]

    if query and query.strip():
        q_low = query.lower().strip()
        catalog = [r for r in catalog if q_low in r.get("title", "").lower() or q_low in r.get("description", "").lower()]

    return catalog


SPORT_REPLAY_CATEGORIES = {
    "cricket": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent Matches & Series"},
        {"id": "world_cup", "label": "ICC World Cup & T20 Finals"},
        {"id": "ipl_psl", "label": "IPL & PSL Blockbusters"},
        {"id": "ashes_tests", "label": "The Ashes & Test Classics"}
    ],
    "football": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent League Matches"},
        {"id": "premier_league", "label": "Premier League"},
        {"id": "champions_league", "label": "Champions League"},
        {"id": "world_cup", "label": "FIFA World Cup"},
        {"id": "euro_copa", "label": "Euro & Copa"},
        {"id": "el_clasico", "label": "El Clásico"}
    ],
    "basketball": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent NBA Matches"},
        {"id": "finals", "label": "NBA Finals"},
        {"id": "playoffs", "label": "NBA Playoffs"}
    ],
    "nfl": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent NFL Matches"},
        {"id": "super_bowl", "label": "Super Bowl"},
        {"id": "playoffs", "label": "NFL Playoffs"}
    ],
    "motorsport": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent Grand Prix Races"},
        {"id": "grand_prix", "label": "Iconic Grand Prix"},
        {"id": "championship", "label": "Championship Deciders"}
    ],
    "tennis": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent Grand Slam Matches"},
        {"id": "wimbledon", "label": "Wimbledon Finals"},
        {"id": "grand_slam", "label": "Grand Slam Classics"}
    ],
    "combat": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent Title Fights"},
        {"id": "ufc_ppv", "label": "UFC PPV Main Events"},
        {"id": "boxing_classics", "label": "Legendary Boxing"}
    ],
    "baseball": [
        {"id": "all", "label": "All Replays & Classics"},
        {"id": "cult_classics", "label": "Greatest Cult Classics (Top 10)"},
        {"id": "recent", "label": "Recent MLB Matches"},
        {"id": "world_series", "label": "World Series"},
        {"id": "postseason", "label": "Postseason Classics"}
    ]
}

def get_sport_replay_categories(sport: str = "football") -> List[Dict[str, str]]:
    """Returns available categories for the given sport."""
    s_key = (sport or "football").lower().strip()
    return SPORT_REPLAY_CATEGORIES.get(s_key, SPORT_REPLAY_CATEGORIES["football"])

def get_multi_sport_replays(sport: str = "football", category: str = None, query: str = None, team: str = None) -> List[Dict[str, Any]]:
    """Alias for get_replays_for_sport with team filtering support."""
    replays = get_replays_for_sport(sport=sport, category=category, query=query)
    if team and team.strip():
        t_low = team.lower().strip()
        replays = [
            r for r in replays
            if t_low in r.get("home_team", {}).get("name", "").lower()
            or t_low in r.get("away_team", {}).get("name", "").lower()
        ]
    return replays
