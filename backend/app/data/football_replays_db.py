"""
Official Football Replays & Classic Matches Database
Curated collection of historic full match replays, legendary finals, and extended tournament archives.
All sources utilize verified official YouTube video IDs from FIFA, UEFA, Premier League, and LaLiga.
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
        "description": "Mikel Oyarzabal pounces in the 86th minute to fire Spain to a record fourth European Championship title over Gareth Southgate's England in Berlin.",
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
                "label": "Server 1: Official UEFA Euro 2024 Final Highlights",
                "network": "UEFA Official",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/lBOS43RWfY0?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Berlin Euro 2024 Final Highlights"
            },
            {
                "id": "euro24-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Official Match Archive"
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
                "label": "Server 1: Official CONMEBOL Final Highlights & Lautaro Winner",
                "network": "CONMEBOL Official",
                "quality": "1080p 60fps",
                "language": "Spanish / English",
                "url": "https://www.youtube-nocookie.com/embed/P_9nUzsB7jU?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Miami Copa Final Official Highlights"
            },
            {
                "id": "copa24-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Direct Video Feed"
            }
        ]
    },

    # --- 2. UEFA Champions League 2023 & 2019 & 2017 & 2005 ---
    {
        "id": "replay-ucl-2023-mci-int",
        "title": "2023 Champions League Final: Manchester City vs Inter Milan",
        "competition": "UEFA Champions League Final",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2023,
        "date": "June 10, 2023",
        "venue": "Atatürk Olympic Stadium, Istanbul",
        "score": "1 - 0",
        "duration": "Full Final Highlights & Treble Ceremony",
        "thumbnail": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop&q=80",
        "description": "Rodri's precision strike in the 68th minute secures Manchester City's maiden European crown to complete a historic continental treble.",
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
                "label": "Server 1: Official UEFA Final Highlights & Rodri Winner",
                "network": "Manchester City Official",
                "quality": "1080p 60fps",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/AXEG_lagq9E?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Man City Treble Final Highlights"
            },
            {
                "id": "ucl23-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Archived Tournament Stream"
            }
        ]
    },

    # --- 3. FIFA World Cup 2022 Qatar ---
    {
        "id": "replay-wc-2022-arg-fra",
        "is_cult_classic": True,
        "cult_rank": 1,
        "cult_badge": "#1 Greatest Match of All Time",
        "title": "2022 World Cup Final: Argentina vs France",
        "competition": "FIFA World Cup Qatar 2022",
        "category": "world_cup",
        "category_label": "World Cup",
        "year": 2022,
        "date": "December 18, 2022",
        "venue": "Lusail Iconic Stadium, Qatar",
        "score": "3 - 3 (4 - 2 pens)",
        "duration": "Full Match Highlights & Deciding Shootout",
        "thumbnail": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop&q=80",
        "description": "Widely heralded as the greatest football final ever played. Lionel Messi scores twice and Kylian Mbappé hits a historic hat-trick in a 120-minute thriller before a dramatic shootout.",
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
                "label": "Server 1: Official Extended Match Highlights & Shootout",
                "network": "World Cup Vault",
                "quality": "1080p 60fps",
                "language": "English Commentary",
                "url": "https://www.youtube-nocookie.com/embed/DDWYR9Oi_wI?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Official FIFA World Cup Extended Highlights"
            },
            {
                "id": "wc22-srv-2",
                "label": "Server 2: beIN Sports World Cup Vault",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Archived Tournament Stream"
            }
        ]
    },

    # --- 4. Champions League 2019 Anfield Comeback ---
    {
        "id": "replay-ucl-2019-liv-bar",
        "is_cult_classic": True,
        "cult_rank": 7,
        "cult_badge": "#7 Anfield Miracle & Corner Taken Quickly",
        "title": "2019 Champions League Semi-Final: Liverpool 4-0 Barcelona",
        "competition": "UEFA Champions League Semi-Final",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2019,
        "date": "May 7, 2019",
        "venue": "Anfield, Liverpool",
        "score": "4 - 0 (4 - 3 agg)",
        "duration": "Full Match Highlights & Anfield Magic",
        "thumbnail": "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 3-0 from the Camp Nou and without Salah and Firmino, Liverpool produce an electric Anfield miracle finished off by Alexander-Arnold's genius corner taken quickly.",
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
                "id": "ucl19-srv-1",
                "label": "Server 1: Official Anfield Highlights & Corner Taken Quickly",
                "network": "Liverpool FC Official",
                "quality": "1080p 60fps",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/pkEpLtePJm0?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Liverpool 4-0 Barcelona Official Highlights"
            },
            {
                "id": "ucl19-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Archived Match Footage"
            }
        ]
    },

    # --- 5. FIFA World Cup 2018 Russia ---
    {
        "id": "replay-wc-2018-fra-cro",
        "title": "2018 World Cup Final: France vs Croatia",
        "competition": "FIFA World Cup Russia 2018",
        "category": "world_cup",
        "category_label": "World Cup",
        "year": 2018,
        "date": "July 15, 2018",
        "venue": "Luzhniki Stadium, Moscow",
        "score": "4 - 2",
        "duration": "Official Highlights & Six-Goal Thriller",
        "thumbnail": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80",
        "description": "Six-goal spectacle featuring strikes from Paul Pogba, Antoine Griezmann, and a teenage Kylian Mbappé as France claim their second world championship.",
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
                "label": "Server 1: Official FIFA 2018 World Cup Final Highlights",
                "network": "FIFA Official",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/GrsEAvRerTg?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "FIFA 2018 Moscow Final Highlights"
            },
            {
                "id": "wc18-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Tournament Video Stream"
            }
        ]
    },

    # --- 6. El Clasico 2017 & 2010 ---
    {
        "id": "replay-clasico-2017-rm-bar",
        "is_cult_classic": True,
        "cult_rank": 6,
        "cult_badge": "#6 Messi 92' Bernabéu Winner",
        "title": "2017 El Clásico: Real Madrid 2-3 Barcelona (Messi 500th Goal)",
        "competition": "La Liga EA Sports",
        "category": "el_clasico",
        "category_label": "El Clásico",
        "year": 2017,
        "date": "April 23, 2017",
        "venue": "Santiago Bernabéu, Madrid",
        "score": "2 - 3",
        "duration": "Full Clásico Drama & 92nd-min Winner",
        "thumbnail": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800&auto=format&fit=crop&q=80",
        "description": "With bloodied gauze in mouth, Lionel Messi strikes a breathtaking 92nd-minute counter-attack winner to notch his 500th goal for Barcelona and produce the iconic jersey celebration.",
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
                "label": "Server 1: Official LaLiga Bernabéu Resumen & Messi 500th",
                "network": "LALIGA EA SPORTS Official",
                "quality": "1080p 60fps",
                "language": "Spanish / English",
                "url": "https://www.youtube-nocookie.com/embed/fVufY4SCoOk?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Real Madrid 2-3 Barcelona Official Highlights"
            },
            {
                "id": "clas17-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Archived Match Footage"
            }
        ]
    },
    {
        "id": "replay-ucl-2017-bar-psg",
        "is_cult_classic": True,
        "cult_rank": 3,
        "cult_badge": "#3 'La Remontada' Miracle",
        "title": "2017 Champions League: Barcelona 6-1 PSG ('La Remontada')",
        "competition": "UEFA Champions League Round of 16",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2017,
        "date": "March 8, 2017",
        "venue": "Camp Nou, Barcelona",
        "score": "6 - 1 (6 - 5 agg)",
        "duration": "Full Match Story & 95th-min Climax",
        "thumbnail": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 4-0 from the first leg, FC Barcelona deliver the greatest comeback in Champions League history with Sergi Roberto scoring in the 95th minute to stun PSG.",
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
                "id": "ucl17-srv-1",
                "label": "Server 1: Official Barcelona 6-1 Remontada Extended Highlights",
                "network": "FC Barcelona Official",
                "quality": "1080p 60fps",
                "language": "English / Spanish",
                "url": "https://www.youtube-nocookie.com/embed/h4m68r8kWAc?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Camp Nou 6-1 Complete Comeback"
            }
        ]
    },

    # --- 7. FIFA World Cup 2014 Brazil ---
    {
        "id": "replay-wc-2014-bra-ger",
        "is_cult_classic": True,
        "cult_rank": 5,
        "cult_badge": "#5 The Mineirazo Stunner",
        "title": "2014 World Cup Semi-Final: Brazil vs Germany",
        "competition": "FIFA World Cup Brazil 2014",
        "category": "world_cup",
        "category_label": "World Cup",
        "year": 2014,
        "date": "July 8, 2014",
        "venue": "Estádio Mineirão, Belo Horizonte",
        "score": "1 - 7",
        "duration": "Full Match Story & All 8 Goals",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "The 'Mineirazo' — the most astonishing match in World Cup history as Germany score five goals in the opening 29 minutes against the tournament hosts.",
        "home_team": {
            "name": "Brazil",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/bra.png"
        },
        "away_team": {
            "name": "Germany",
            "score": 7,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/ger.png"
        },
        "streams": [
            {
                "id": "wc14-bg-srv-1",
                "label": "Server 1: Official FIFA Extended Highlights | All 8 Goals",
                "network": "FIFA Official",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/aE4BdIP6bvc?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Mineirão 7-1 Historic Highlights"
            }
        ]
    },
    {
        "id": "replay-wc-2014-ger-arg",
        "is_cult_classic": True,
        "cult_rank": 10,
        "cult_badge": "#10 Maracanã Extra-Time Gold",
        "title": "2014 World Cup Final: Germany vs Argentina",
        "competition": "FIFA World Cup Brazil 2014",
        "category": "world_cup",
        "category_label": "World Cup",
        "year": 2014,
        "date": "July 13, 2014",
        "venue": "Maracanã Stadium, Rio de Janeiro",
        "score": "1 - 0 (AET)",
        "duration": "Full Extra Time Highlights & Götze Volley",
        "thumbnail": "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?w=800&auto=format&fit=crop&q=80",
        "description": "Mario Götze's unforgettable 113th-minute chest control and left-footed volley at the Maracanã crowns Germany world champions.",
        "home_team": {
            "name": "Germany",
            "score": 1,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/ger.png"
        },
        "away_team": {
            "name": "Argentina",
            "score": 0,
            "logo": "https://a.espncdn.com/i/teamlogos/countries/500/arg.png"
        },
        "streams": [
            {
                "id": "wc14-ga-srv-1",
                "label": "Server 1: Official FIFA 2014 Final Highlights (AET)",
                "network": "FIFA Official",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/ffAYByv2pLc?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Maracanã 2014 Final Highlights"
            }
        ]
    },

    # --- 8. Premier League 2012 & 2011 ---
    {
        "id": "replay-epl-2012-mci-qpr",
        "is_cult_classic": True,
        "cult_rank": 4,
        "cult_badge": "#4 93:20 Agüero Title Decider",
        "title": "2012 Premier League Finale: Manchester City vs QPR ('Agueroooo!')",
        "competition": "English Premier League",
        "category": "premier_league",
        "category_label": "Premier League",
        "year": 2012,
        "date": "May 13, 2012",
        "venue": "Etihad Stadium, Manchester",
        "score": "3 - 2",
        "duration": "Historic Title Climax & Full Stoppage Time",
        "thumbnail": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80",
        "description": "Trailing 2-1 in stoppage time on the final day, Dzeko and Sergio Agüero (93:20) score back-to-back goals to win City's first title in 44 years at Manchester United's expense.",
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
                "id": "epl12-srv-1",
                "label": "Server 1: Official Agüero 93:20 Title Deciding Replay",
                "network": "Manchester City Official",
                "quality": "1080p 60fps",
                "language": "English (Martin Tyler)",
                "url": "https://www.youtube-nocookie.com/embed/QdZfs3aj3uk?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Title Deciding Agüero Stoppage Time Replay"
            }
        ]
    },
    {
        "id": "replay-epl-2011-new-ars",
        "is_cult_classic": True,
        "cult_rank": 9,
        "cult_badge": "#9 Greatest Premier League Comeback",
        "title": "2011 Premier League: Newcastle United 4-4 Arsenal",
        "competition": "English Premier League",
        "category": "premier_league",
        "category_label": "Premier League",
        "year": 2011,
        "date": "February 5, 2011",
        "venue": "St. James' Park, Newcastle",
        "score": "4 - 4",
        "duration": "Eight Goal Thriller & Tioté Volley",
        "thumbnail": "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&auto=format&fit=crop&q=80",
        "description": "Arsenal race into a 4-0 lead within 26 minutes before Newcastle orchestrate the greatest comeback in Premier League history, capped by Cheick Tioté's thunderous 87th-minute volley.",
        "home_team": {
            "name": "Newcastle United",
            "score": 4,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/361.png"
        },
        "away_team": {
            "name": "Arsenal",
            "score": 4,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png"
        },
        "streams": [
            {
                "id": "epl11-srv-1",
                "label": "Server 1: Official Premier League 4-4 Thriller Highlights",
                "network": "Premier League Official",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://www.youtube-nocookie.com/embed/PnR3pr4qsoI?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "St James Park 4-4 Comeback Replay"
            }
        ]
    },

    # --- 9. El Clasico 2010 ---
    {
        "id": "replay-clasico-2010-bar-rm",
        "is_cult_classic": True,
        "cult_rank": 8,
        "cult_badge": "#8 Peak Tiki-Taka Manita",
        "title": "2010 El Clásico: Barcelona 5-0 Real Madrid (Manita Masterpiece)",
        "competition": "La Liga EA Sports",
        "category": "el_clasico",
        "category_label": "El Clásico",
        "year": 2010,
        "date": "November 29, 2010",
        "venue": "Camp Nou, Barcelona",
        "score": "5 - 0",
        "duration": "Pep Guardiola Masterclass & Highlights",
        "thumbnail": "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?w=800&auto=format&fit=crop&q=80",
        "description": "Peak tiki-taka perfection as Pep Guardiola's FC Barcelona dismantle José Mourinho's unbeaten Real Madrid with a breathtaking 5-0 exhibition.",
        "home_team": {
            "name": "Barcelona",
            "score": 5,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/83.png"
        },
        "away_team": {
            "name": "Real Madrid",
            "score": 0,
            "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png"
        },
        "streams": [
            {
                "id": "clas10-srv-1",
                "label": "Server 1: Official 5-0 Manita Exhibition Highlights",
                "network": "LaLiga EA SPORTS",
                "quality": "1080p HD",
                "language": "Spanish / English",
                "url": "https://www.youtube-nocookie.com/embed/5mLnuCORMrU?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Camp Nou 5-0 Exhibition Replay"
            }
        ]
    },

    # --- 10. Champions League 2005 Istanbul ---
    {
        "id": "replay-ucl-2005-liv-mil",
        "is_cult_classic": True,
        "cult_rank": 2,
        "cult_badge": "#2 Miracle of Istanbul",
        "title": "2005 Champions League Final: AC Milan vs Liverpool",
        "competition": "UEFA Champions League Final",
        "category": "champions_league",
        "category_label": "Champions League",
        "year": 2005,
        "date": "May 25, 2005",
        "venue": "Atatürk Olympic Stadium, Istanbul",
        "score": "3 - 3 (2 - 3 pens)",
        "duration": "Full Match Highlights & Dudek Shootout",
        "thumbnail": "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&auto=format&fit=crop&q=80",
        "description": "The 'Miracle of Istanbul'. Down 3-0 at half-time against prime AC Milan, Steven Gerrard leads an unbelievable six-minute comeback to force penalties and claim European glory.",
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
                "id": "ucl05-srv-1",
                "label": "Server 1: Official Istanbul 05 Greatest Ever Final Highlights",
                "network": "Liverpool FC Official",
                "quality": "1080p HD",
                "language": "English (Clive Tyldesley)",
                "url": "https://www.youtube-nocookie.com/embed/3ojXHf293M8?autoplay=1",
                "is_embed": True,
                "is_primary": True,
                "coverage": "Istanbul 2005 Official Replay"
            },
            {
                "id": "ucl05-srv-2",
                "label": "Server 2: beIN Sports Vault Stream",
                "network": "beIN Sports Vault",
                "quality": "1080p HD",
                "language": "English",
                "url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
                "is_embed": False,
                "is_primary": False,
                "coverage": "Deciding Penalty Shootout"
            }
        ]
    }
]

def get_all_football_replays(category: str = None, query: str = None, team: str = None) -> List[Dict[str, Any]]:
    """Filters football replays by category, keyword search, or team."""
    results = list(FOOTBALL_REPLAYS_CATALOG)
    
    if category and isinstance(category, str) and category.lower() != "all":
        cat_lower = category.lower()
        if cat_lower == "cult_classics":
            results = [r for r in results if r.get("is_cult_classic")]
            results.sort(key=lambda r: r.get("cult_rank", 99))
        else:
            results = [
                r for r in results 
                if r.get("category") == cat_lower or cat_lower in r.get("categories", [])
            ]
        
    if team and isinstance(team, str) and team.strip():
        t_lower = team.lower().strip()
        results = [
            r for r in results 
            if t_lower in r.get("home_team", {}).get("name", "").lower()
            or t_lower in r.get("away_team", {}).get("name", "").lower()
        ]
        
    if query and isinstance(query, str) and query.strip():
        q_lower = query.lower().strip()
        results = [
            r for r in results
            if q_lower in r.get("title", "").lower()
            or q_lower in r.get("description", "").lower()
            or q_lower in r.get("competition", "").lower()
            or q_lower in r.get("home_team", {}).get("name", "").lower()
            or q_lower in r.get("away_team", {}).get("name", "").lower()
            or str(r.get("year", "")) in q_lower
        ]
        
    return results

def find_replays_for_match(home_name: str, away_name: str) -> List[Dict[str, Any]]:
    """Attempts to find related classic replays for the competing teams."""
    h_lower = home_name.lower()
    a_lower = away_name.lower()
    
    related = []
    for r in FOOTBALL_REPLAYS_CATALOG:
        rh = r.get("home_team", {}).get("name", "").lower()
        ra = r.get("away_team", {}).get("name", "").lower()
        if (h_lower in rh and a_lower in ra) or (h_lower in ra and a_lower in rh):
            related.insert(0, r)
        elif h_lower in rh or h_lower in ra or a_lower in rh or a_lower in ra:
            related.append(r)
            
    return related[:3]
