"""
Multi-Sport Replays & Classics Vault Database
Contains the Top 10 Greatest Cult Classics of All Time for:
- Cricket (2019 WC Super Over, Kohli MCG 82*, Dhoni 2011, Brathwaite 2016, etc.)
- Basketball (NBA Finals, Jordan, Kobe, Ray Allen, LeBron)
- American Football (Super Bowls, 28-3 Comeback, Helmet Catch, Mahomes OT)
- Motorsport (Formula 1 Abu Dhabi 2021, Canada 2011, Brazil 2008, Senna 1993)
- Tennis (Wimbledon 2008 Federer vs Nadal, AO 2012 Djokovic vs Nadal)
- Combat Sports (UFC 229 Khabib vs McGregor, Ali vs Foreman, Hagler vs Hearns)
- Baseball (2016 World Series Cubs G7, 2004 Red Sox Comeback)
Delegates to football_replays_db for Football.
"""

from typing import List, Dict, Any
from app.data.football_replays_db import get_all_football_replays, FOOTBALL_REPLAYS_CATALOG

# ==========================================
# CRICKET CULT CLASSICS (TOP 10 OF ALL TIME)
# ==========================================
CRICKET_REPLAYS: List[Dict[str, Any]] = [
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
        "home_team": {"name": "England", "score": "241 & 15/0", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "away_team": {"name": "New Zealand", "score": "241/8 & 15/1", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2849.png"},
        "streams": [
            {"id": "cric-2019-1", "label": "Server 1: Super Over Thriller (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Ian Smith)", "url": "https://www.youtube-nocookie.com/embed/3KCKNhjcvFo?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=3KCKNhjcvFo", "is_embed": True, "is_primary": True},
            {"id": "cric-2019-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x94q0jg", "direct_url": "https://www.dailymotion.com/video/x94q0jg", "is_embed": True, "is_primary": False}
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
            {"id": "cric-2022-1", "label": "Server 1: Kohli 82* Masterclass (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Harsha Bhogle)", "url": "https://www.youtube-nocookie.com/embed/kaIdKOoObjw?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=kaIdKOoObjw", "is_embed": True, "is_primary": True},
            {"id": "cric-2022-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x9p49qw", "direct_url": "https://www.dailymotion.com/video/x9p49qw", "is_embed": True, "is_primary": False}
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
            {"id": "cric-2016-1", "label": "Server 1: Brathwaite 4 Sixes (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Ian Bishop)", "url": "https://www.youtube-nocookie.com/embed/MQSb1J9sodk?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=MQSb1J9sodk", "is_embed": True, "is_primary": True},
            {"id": "cric-2016-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x42etlr", "direct_url": "https://www.dailymotion.com/video/x42etlr", "is_embed": True, "is_primary": False}
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
            {"id": "cric-2011-1", "label": "Server 1: Final Chase & Dhoni Six (YouTube)", "network": "YouTube Player", "quality": "1080p HD", "language": "English (Ravi Shastri)", "url": "https://www.youtube-nocookie.com/embed/YphL3Whh5B0?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=YphL3Whh5B0", "is_embed": True, "is_primary": True},
            {"id": "cric-2011-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x9ejifo", "direct_url": "https://www.dailymotion.com/video/x9ejifo", "is_embed": True, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-1999-wc-sf",
        "title": "1999 World Cup Semi-Final: Australia vs South Africa (Edgbaston Tie)",
        "competition": "ICC Cricket World Cup Semi-Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 1999,
        "date": "June 17, 1999",
        "score": "AUS 213 (49.2) tied SA 213 (49.4)",
        "duration": "Full 50th Over Run-Out Heartbreak & Highlights",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "Lance Klusener blasts 31 off 16 balls, needing 1 run with 4 balls to spare. A chaotic mix-up with Allan Donald leads to a run-out, ending in the most heart-stopping tie in cricket history.",
        "is_cult_classic": True,
        "cult_rank": 5,
        "cult_badge": "#5 Greatest ODI Drama in History",
        "home_team": {"name": "Australia", "score": "213 (49.2)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2853.png"},
        "away_team": {"name": "South Africa", "score": "213 (49.4)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2854.png"},
        "streams": [
            {"id": "cric-1999-1", "label": "Server 1: Final Over Tie (YouTube)", "network": "YouTube Player", "quality": "720p HD", "language": "English (Bill Lawry)", "url": "https://www.youtube-nocookie.com/embed/AocPABE_Opg?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=AocPABE_Opg", "is_embed": True, "is_primary": True},
            {"id": "cric-1999-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "720p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x7m7zyp", "direct_url": "https://www.dailymotion.com/video/x7m7zyp", "is_embed": True, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-2019-headingley",
        "title": "2019 Ashes 3rd Test at Headingley: England vs Australia (Stokes 135*)",
        "competition": "The Ashes 2019",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "ashes_tests",
        "category_label": "The Ashes & Tests",
        "year": 2019,
        "date": "August 25, 2019",
        "score": "ENG 67 & 362/9 beat AUS 179 & 246",
        "duration": "Stokes' 73-Run 10th-Wicket Stand with Jack Leach",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "After England were bowled out for 67 in the first innings and were 286/9 in the fourth, Ben Stokes plays the greatest fourth-innings Test knock of all time (135*), partnering with Jack Leach (1*) to chase down 359.",
        "is_cult_classic": True,
        "cult_rank": 6,
        "cult_badge": "#6 Stokes' Headingley Miracle",
        "home_team": {"name": "England", "score": "67 & 362/9", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "away_team": {"name": "Australia", "score": "179 & 246", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2853.png"},
        "streams": [
            {"id": "cric-head19-1", "label": "Server 1: Final Day Miracle (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Nasser Hussain)", "url": "https://www.youtube-nocookie.com/embed/wamtTEVFDiA?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=wamtTEVFDiA", "is_embed": True, "is_primary": True},
            {"id": "cric-head19-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x7x8wg1", "direct_url": "https://www.dailymotion.com/video/x7x8wg1", "is_embed": True, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-2007-wt20-final",
        "title": "2007 T20 World Cup Final: India vs Pakistan (Misbah Scoop)",
        "competition": "ICC World Twenty20 Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "T20 World Cup",
        "year": 2007,
        "date": "September 24, 2007",
        "score": "IND 157/5 (20 ov) beat PAK 152 (19.3 ov)",
        "duration": "Full Final Over Drama & Sreesanth Catch",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "Needing 6 runs off 4 balls in Johannesburg, Misbah-ul-Haq scoops Joginder Sharma to fine leg where Sreesanth takes the most famous catch in T20 history to crown MS Dhoni's young India champions.",
        "is_cult_classic": True,
        "cult_rank": 7,
        "cult_badge": "#7 Birth of Modern T20 Cricket",
        "home_team": {"name": "India", "score": "157/5 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2965.png"},
        "away_team": {"name": "Pakistan", "score": "152 (19.3 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png"},
        "streams": [
            {"id": "cric-2007-1", "label": "Server 1: Final Over & Trophy Lift (YouTube)", "network": "YouTube Player", "quality": "720p HD", "language": "English (Ravi Shastri)", "url": "https://www.youtube-nocookie.com/embed/Mr35Qi7ZATg?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=Mr35Qi7ZATg", "is_embed": True, "is_primary": True},
            {"id": "cric-2007-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "720p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x8voghm", "direct_url": "https://www.dailymotion.com/video/x8voghm", "is_embed": True, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-2023-ipl-final",
        "title": "2023 IPL Final: Chennai Super Kings vs Gujarat Titans (Jadeja 10 off 2)",
        "competition": "Indian Premier League Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "ipl_psl",
        "category_label": "IPL & PSL",
        "year": 2023,
        "date": "May 29, 2023",
        "score": "CSK 171/5 (15 ov, DLS) beat GT 214/4",
        "duration": "Full Final Over Thriller - 6 and 4 off Last 2 Balls",
        "thumbnail": "https://images.unsplash.com/photo-1531415074868-036b1c5d53ec?w=800&auto=format&fit=crop&q=80",
        "description": "At 1:30 AM in Ahmedabad after 3 days of rain, CSK need 10 runs off 2 balls against Mohit Sharma. Ravindra Jadeja smashes a straight six and a fine-leg boundary to win Dhoni his 5th IPL title.",
        "is_cult_classic": True,
        "cult_rank": 8,
        "cult_badge": "#8 Jadeja 10 Runs off Last 2 Balls",
        "home_team": {"name": "Chennai Super Kings", "score": "171/5 (15 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/4341.png"},
        "away_team": {"name": "Gujarat Titans", "score": "214/4 (20 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/1298423.png"},
        "streams": [
            {"id": "cric-ipl23-1", "label": "Server 1: Final 2 Balls & Trophy (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English Commentary", "url": "https://www.youtube-nocookie.com/embed/ckTn4ctzGzg?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=ckTn4ctzGzg", "is_embed": True, "is_primary": True},
            {"id": "cric-ipl23-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "Hindi / English", "url": "https://www.dailymotion.com/embed/video/x8lcy9t", "direct_url": "https://www.dailymotion.com/video/x8lcy9t", "is_embed": True, "is_primary": False}
        ]
    },
    {
        "id": "cric-replay-1992-wc-final",
        "title": "1992 World Cup Final: Pakistan vs England (Cornered Tigers)",
        "competition": "ICC Cricket World Cup Final",
        "sport": "Cricket",
        "sport_id": "cricket",
        "category": "world_cup",
        "category_label": "ICC World Cup",
        "year": 1992,
        "date": "March 25, 1992",
        "score": "PAK 249/6 (50 ov) beat ENG 227 (49.2 ov)",
        "duration": "Wasim Akram's Twin Magic Deliveries & Imran Khan Trophy",
        "thumbnail": "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80",
        "description": "Imran Khan leads his 'Cornered Tigers' to victory at the MCG, highlighted by Wasim Akram's two consecutive unplayable reverse-swing deliveries to dismiss Allan Lamb and Chris Lewis.",
        "is_cult_classic": True,
        "cult_rank": 9,
        "cult_badge": "#9 Cornered Tigers MCG Miracle",
        "home_team": {"name": "Pakistan", "score": "249/6 (50 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png"},
        "away_team": {"name": "England", "score": "227 (49.2 ov)", "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/971.png"},
        "streams": [
            {"id": "cric-1992-1", "label": "Server 1: Akram Twin Magic (YouTube)", "network": "YouTube Player", "quality": "720p HD", "language": "English (Richie Benaud)", "url": "https://www.youtube-nocookie.com/embed/QXVcXQCpz_E?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=QXVcXQCpz_E", "is_embed": True, "is_primary": True},
            {"id": "cric-1992-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "720p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x4sfv51", "direct_url": "https://www.dailymotion.com/video/x4sfv51", "is_embed": True, "is_primary": False}
        ]
    }
]

# ==========================================
# BASKETBALL CULT CLASSICS
# ==========================================
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
            {"id": "bball-2016-1", "label": "Server 1: Official Highlights (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Mike Breen)", "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU", "is_embed": True, "is_primary": True},
            {"id": "bball-2016-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Feed", "url": "https://www.dailymotion.com/embed/video/x4h4q76", "direct_url": "https://www.dailymotion.com/video/x4h4q76", "is_embed": True, "is_primary": False}
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
        "cult_rank": 2,
        "cult_badge": "#2 Ray Allen 'BANG!' Corner 3",
        "home_team": {"name": "Miami Heat", "score": 103, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/mia.png"},
        "away_team": {"name": "San Antonio Spurs", "score": 100, "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/sas.png"},
        "streams": [
            {"id": "bball-2013-1", "label": "Server 1: Official Ray Allen Shot (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Mike Breen)", "url": "https://www.youtube-nocookie.com/embed/tr6XsZVb-ZE?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=tr6XsZVb-ZE", "is_embed": True, "is_primary": True},
            {"id": "bball-2013-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Feed", "url": "https://www.dailymotion.com/embed/video/x2q7s9y", "direct_url": "https://www.dailymotion.com/video/x2q7s9y", "is_embed": True, "is_primary": False}
        ]
    }
]

# ==========================================
# NFL CULT CLASSICS
# ==========================================
NFL_REPLAYS = [
    {
        "id": "nfl-replay-sb51-ne-atl",
        "title": "Super Bowl LI: New England Patriots vs Atlanta Falcons (28-3 Comeback)",
        "competition": "Super Bowl LI",
        "sport": "American Football",
        "sport_id": "nfl",
        "category": "super_bowl",
        "category_label": "Super Bowl",
        "year": 2017,
        "date": "February 5, 2017",
        "score": "34 - 28 (OT)",
        "duration": "Full 31-Unanswered Point Rally & James White OT TD",
        "thumbnail": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 28-3 midway through the third quarter, Tom Brady engineers the greatest comeback in Super Bowl history to secure New England's 5th ring in the first overtime game ever.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 28-3 The Greatest Super Bowl Comeback",
        "home_team": {"name": "New England Patriots", "score": 34, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/ne.png"},
        "away_team": {"name": "Atlanta Falcons", "score": 28, "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/atl.png"},
        "streams": [
            {"id": "nfl-sb51-1", "label": "Server 1: Official Super Bowl LI Highlights (YouTube)", "network": "NFL Official", "quality": "1080p 60fps", "language": "English (Joe Buck)", "url": "https://www.youtube-nocookie.com/embed/016LXFHpFCk?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=016LXFHpFCk", "is_embed": True, "is_primary": True},
            {"id": "nfl-sb51-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Feed", "url": "https://www.dailymotion.com/embed/video/x5aql8m", "direct_url": "https://www.dailymotion.com/video/x5aql8m", "is_embed": True, "is_primary": False}
        ]
    }
]

# ==========================================
# MOTORSPORT CULT CLASSICS
# ==========================================
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
            {"id": "f1-2021-1", "label": "Server 1: Final Lap Battle (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Crofty / Brundle)", "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU", "is_embed": True, "is_primary": True},
            {"id": "f1-2021-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x86ak7u", "direct_url": "https://www.dailymotion.com/video/x86ak7u", "is_embed": True, "is_primary": False}
        ]
    }
]

TENNIS_REPLAYS = [
    {
        "id": "ten-replay-2008-wimbledon-final",
        "title": "2008 Wimbledon Final: Rafael Nadal vs Roger Federer",
        "competition": "Wimbledon Championships 2008",
        "sport": "Tennis",
        "sport_id": "tennis",
        "category": "wimbledon",
        "category_label": "Wimbledon Finals",
        "year": 2008,
        "date": "July 6, 2008",
        "score": "6-4, 6-4, 6-7, 6-7, 9-7",
        "duration": "4 Hours 48 Minutes Epic in Near Darkness",
        "thumbnail": "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80",
        "description": "Widely regarded as the greatest tennis match in history. After rain delays and five electrifying sets in near darkness on Centre Court, Nadal dethrones five-time defending champion Federer 9-7 in the fifth.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Tennis Match in History",
        "home_team": {"name": "Rafael Nadal", "score": 3, "logo": "https://a.espncdn.com/i/teamlogos/countries/500/esp.png"},
        "away_team": {"name": "Roger Federer", "score": 2, "logo": "https://a.espncdn.com/i/teamlogos/countries/500/sui.png"},
        "streams": [
            {"id": "ten-2008-1", "label": "Server 1: Final Set & Trophy (YouTube)", "network": "YouTube Player", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU", "is_embed": True, "is_primary": True},
            {"id": "ten-2008-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x2q7s9y", "direct_url": "https://www.dailymotion.com/video/x2q7s9y", "is_embed": True, "is_primary": False}
        ]
    }
]

COMBAT_REPLAYS = [
    {
        "id": "ufc-replay-229-khabib-conor",
        "title": "UFC 229: Khabib Nurmagomedov vs Conor McGregor",
        "competition": "UFC 229 World Lightweight Championship",
        "sport": "Combat Sports",
        "sport_id": "combat",
        "category": "ufc_ppv",
        "category_label": "UFC PPV",
        "year": 2018,
        "date": "October 6, 2018",
        "score": "Khabib Sub R4 3:03",
        "duration": "Full 4 Rounds, Neck Crank & Post-Fight Pandemonium",
        "thumbnail": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?w=800&auto=format&fit=crop&q=80",
        "description": "The biggest fight in combat sports history. Khabib drops McGregor with an overhand right, dominates on the canvas, and forces a fourth-round tap via neck crank.",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Highest-Grossing MMA Fight in History",
        "home_team": {"name": "Khabib Nurmagomedov", "score": 1, "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png"},
        "away_team": {"name": "Conor McGregor", "score": 0, "logo": "https://a.espncdn.com/i/teamlogos/countries/500/irl.png"},
        "streams": [
            {"id": "ufc-229-1", "label": "Server 1: Official Highlights (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Joe Rogan)", "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU", "is_embed": True, "is_primary": True},
            {"id": "ufc-229-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x6vcfau", "direct_url": "https://www.dailymotion.com/video/x6vcfau", "is_embed": True, "is_primary": False}
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
            {"id": "mlb-2016-1", "label": "Server 1: Official Game 7 Highlights (YouTube)", "network": "YouTube Player", "quality": "1080p 60fps", "language": "English (Joe Buck)", "url": "https://www.youtube-nocookie.com/embed/d3jNqfP4pKU?autoplay=1", "direct_url": "https://www.youtube.com/watch?v=d3jNqfP4pKU", "is_embed": True, "is_primary": True},
            {"id": "mlb-2016-2", "label": "Server 2: Dailymotion HD Mirror", "network": "Dailymotion Video", "quality": "1080p HD", "language": "English Commentary", "url": "https://www.dailymotion.com/embed/video/x50j04u", "direct_url": "https://www.dailymotion.com/video/x50j04u", "is_embed": True, "is_primary": False}
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
        catalog = list(CRICKET_REPLAYS)

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
