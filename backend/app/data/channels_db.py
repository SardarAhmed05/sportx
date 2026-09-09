"""
Worldwide Multi-Sport Live TV Channels & Streams Database
Dedicated 24/7 Sports Broadcast Networks Worldwide for:
- Football (Soccer)
- Basketball
- American Football (NFL)
- Motorsport (Formula 1)
- Tennis
- Combat Sports (UFC / Boxing)
- Baseball (MLB)
"""

FOOTBALL_CHANNELS = [
    {
        "id": "sky-sports-premier-league",
        "name": "Sky Sports Premier League HD",
        "sport": "Football",
        "sport_id": "football",
        "league": "Premier League",
        "country": "United Kingdom",
        "country_code": "GB",
        "language": "English (UK)",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png",
        "description": "24/7 Live Premier League matches, studio analysis, and matchday live.",
        "stream_url": "https://epiembeds.online/embed/sky-sports-premier-league",
        "is_embed": True,
        "backup_streams": [
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
            "https://bein-xtra-bein.amagi.tv/playlist.m3u8"
        ],
        "is_live": True,
        "viewers": 780000,
        "featured": True
    },
    {
        "id": "tnt-sports-1-hd",
        "name": "TNT Sports 1 HD (UK)",
        "sport": "Football",
        "sport_id": "football",
        "league": "Champions League / EPL",
        "country": "United Kingdom",
        "country_code": "GB",
        "language": "English (UK)",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png",
        "description": "UEFA Champions League, Europa League, and Premier League live broadcast.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": [
            "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
        ],
        "is_live": True,
        "viewers": 640000,
        "featured": True
    },
    {
        "id": "dazn-laliga-hd",
        "name": "DAZN LaLiga EA Sports HD",
        "sport": "Football",
        "sport_id": "football",
        "league": "La Liga",
        "country": "Spain",
        "country_code": "ES",
        "language": "Spanish",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png",
        "description": "Official Spanish La Liga broadcast including El Clásico and Madrid derbies.",
        "stream_url": "https://epiembeds.online/embed/daznlaliga-es",
        "is_embed": True,
        "backup_streams": [
            "https://bein-xtra-bein.amagi.tv/playlist.m3u8"
        ],
        "is_live": True,
        "viewers": 590000,
        "featured": True
    },
    {
        "id": "bein-sports-xtra",
        "name": "beIN SPORTS XTRA HD",
        "sport": "Football",
        "sport_id": "football",
        "league": "Global Football",
        "country": "International / Qatar",
        "country_code": "INT",
        "language": "English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/83.png",
        "description": "Live UEFA Champions League, La Liga, Ligue 1, and international football.",
        "stream_url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
        "is_embed": False,
        "backup_streams": [
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
            "https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor.m3u8"
        ],
        "is_live": True,
        "viewers": 510000,
        "featured": True
    },
    {
        "id": "espn-usa-hd",
        "name": "ESPN HD / ESPN+ Soccer",
        "sport": "Football",
        "sport_id": "football",
        "league": "La Liga / Bundesliga",
        "country": "United States",
        "country_code": "US",
        "language": "English (US)",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png",
        "description": "USA broadcast of La Liga, Bundesliga, FA Cup, and MLS.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": [
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
        ],
        "is_live": True,
        "viewers": 430000,
        "featured": True
    },
    {
        "id": "a-spor-hd",
        "name": "A Spor Football HD 1080p",
        "sport": "Football",
        "sport_id": "football",
        "league": "European Football",
        "country": "Europe",
        "country_code": "EU",
        "language": "English / Turkish",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/132.png",
        "description": "Live European cup ties, international matches, and tactical highlights.",
        "stream_url": "https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/aspor/aspor.m3u8",
        "is_embed": False,
        "backup_streams": [
            "https://bein-xtra-bein.amagi.tv/playlist.m3u8"
        ],
        "is_live": True,
        "viewers": 320000,
        "featured": True
    },
    {
        "id": "stan-sport-1",
        "name": "Stan Sport 1 HD (UCL Live)",
        "sport": "Football",
        "sport_id": "football",
        "league": "UEFA Champions League",
        "country": "Australia",
        "country_code": "AU",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/110.png",
        "description": "UEFA Champions League and Europa League live world feed.",
        "stream_url": "https://epiembeds.online/embed/stan-1",
        "is_embed": True,
        "backup_streams": [
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
        ],
        "is_live": True,
        "viewers": 460000,
        "featured": False
    },
    {
        "id": "canal-plus-sport",
        "name": "CANAL+ Sport HD",
        "sport": "Football",
        "sport_id": "football",
        "league": "Premier League / Ligue 1",
        "country": "France / Poland",
        "country_code": "FR",
        "language": "French / Polish",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/103.png",
        "description": "Live European football leagues and Champions League coverage.",
        "stream_url": "https://epiembeds.online/embed/canalsport-pl",
        "is_embed": True,
        "backup_streams": [
            "https://bein-xtra-bein.amagi.tv/playlist.m3u8"
        ],
        "is_live": True,
        "viewers": 380000,
        "featured": False
    },
    {
        "id": "africa24-sport",
        "name": "Africa 24 Football Live",
        "sport": "Football",
        "sport_id": "football",
        "league": "African & Global",
        "country": "Africa / International",
        "country_code": "INT",
        "language": "English / French",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/363.png",
        "description": "African Champions League, AFCON, and European stars.",
        "stream_url": "https://africa24.vedge.infomaniak.com/livecast/ik:africa24sport/manifest.m3u8",
        "is_embed": False,
        "backup_streams": [
            "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
        ],
        "is_live": True,
        "viewers": 195000,
        "featured": False
    }
]

BASKETBALL_CHANNELS = [
    {
        "id": "nba-tv-hd",
        "name": "NBA TV HD Live (24/7)",
        "sport": "Basketball",
        "sport_id": "basketball",
        "league": "NBA",
        "country": "United States",
        "country_code": "US",
        "language": "English (US)",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/tor.png",
        "description": "Official 24/7 NBA network with live games, NBA Gametime, and inside analysis.",
        "stream_url": "https://epiembeds.online/embed/nba-tv",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 820000,
        "featured": True
    },
    {
        "id": "espn-basketball-hd",
        "name": "ESPN Basketball HD",
        "sport": "Basketball",
        "sport_id": "basketball",
        "league": "NBA / NCAA",
        "country": "United States",
        "country_code": "US",
        "language": "English (US)",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/mia.png",
        "description": "Live NBA on ESPN, Wednesday & Friday doubleheaders, and College Hoops.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 690000,
        "featured": True
    },
    {
        "id": "tnt-nba-hd",
        "name": "TNT Sports Basketball HD",
        "sport": "Basketball",
        "sport_id": "basketball",
        "league": "NBA Primetime",
        "country": "United States / UK",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/bos.png",
        "description": "Inside the NBA and Thursday Night Basketball live broadcasts.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 610000,
        "featured": True
    },
    {
        "id": "euroleague-tv-hd",
        "name": "EuroLeague TV Live",
        "sport": "Basketball",
        "sport_id": "basketball",
        "league": "EuroLeague",
        "country": "Europe",
        "country_code": "EU",
        "language": "English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/gsw.png",
        "description": "Top European club basketball: Real Madrid, Panathinaikos, Olympiacos, and Barcelona.",
        "stream_url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
        "is_embed": False,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 340000,
        "featured": False
    }
]

NFL_CHANNELS = [
    {
        "id": "nfl-network-hd",
        "name": "NFL Network 24/7 HD",
        "sport": "American Football",
        "sport_id": "nfl",
        "league": "NFL",
        "country": "United States",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/kc.png",
        "description": "Official 24/7 NFL channel with live game broadcasts, GameDay Live, and NFL Total Access.",
        "stream_url": "https://epiembeds.online/embed/nfl-network",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 950000,
        "featured": True
    },
    {
        "id": "nfl-redzone-hd",
        "name": "NFL RedZone Live HD",
        "sport": "American Football",
        "sport_id": "nfl",
        "league": "NFL Sunday",
        "country": "United States",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/sf.png",
        "description": "Every touchdown from every game, live commercial-free on Sunday afternoons.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 890000,
        "featured": True
    },
    {
        "id": "sky-sports-nfl",
        "name": "Sky Sports NFL HD",
        "sport": "American Football",
        "sport_id": "nfl",
        "league": "NFL International",
        "country": "United Kingdom",
        "country_code": "GB",
        "language": "English (UK)",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/nfl/500/phi.png",
        "description": "Thursday, Sunday, and Monday Night Football live European broadcast.",
        "stream_url": "https://epiembeds.online/embed/sky-sports-premier-league",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 520000,
        "featured": False
    }
]

MOTORSPORT_CHANNELS = [
    {
        "id": "sky-sports-f1-hd",
        "name": "Sky Sports F1 HD 1080p",
        "sport": "Motorsport",
        "sport_id": "motorsport",
        "league": "Formula 1",
        "country": "United Kingdom",
        "country_code": "GB",
        "language": "English (UK)",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png",
        "description": "24/7 dedicated Formula 1 channel. Live Practice, Qualifying, and Race Day worldwide.",
        "stream_url": "https://epiembeds.online/embed/sky-sports-premier-league",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 910000,
        "featured": True
    },
    {
        "id": "f1tv-live-hd",
        "name": "F1 TV Pro World Feed",
        "sport": "Motorsport",
        "sport_id": "motorsport",
        "league": "Formula 1 World Championship",
        "country": "International",
        "country_code": "INT",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png",
        "description": "Official Formula 1 pitlane view, onboard cameras, and live team telemetry.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 760000,
        "featured": True
    },
    {
        "id": "motogp-live-hd",
        "name": "MotoGP Live HD World Feed",
        "sport": "Motorsport",
        "sport_id": "motorsport",
        "league": "MotoGP",
        "country": "Europe / Spain",
        "country_code": "ES",
        "language": "English / Spanish",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png",
        "description": "Live premier motorcycle racing: MotoGP, Moto2, and Moto3 Grand Prix weekends.",
        "stream_url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
        "is_embed": False,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 430000,
        "featured": False
    }
]

TENNIS_CHANNELS = [
    {
        "id": "tennis-channel-hd",
        "name": "Tennis Channel HD Live",
        "sport": "Tennis",
        "sport_id": "tennis",
        "league": "ATP / WTA Tour",
        "country": "United States",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/364.png",
        "description": "24/7 dedicated Tennis channel with live ATP Masters 1000, WTA 1000, and Grand Slams.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 570000,
        "featured": True
    },
    {
        "id": "eurosport-1-tennis",
        "name": "Eurosport 1 Tennis Live",
        "sport": "Tennis",
        "sport_id": "tennis",
        "league": "Grand Slam Center Court",
        "country": "Europe",
        "country_code": "EU",
        "language": "English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/103.png",
        "description": "Live coverage of the Australian Open, Roland-Garros, and Wimbledon.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 490000,
        "featured": True
    }
]

COMBAT_CHANNELS = [
    {
        "id": "ufc-fight-pass-hd",
        "name": "UFC Fight Pass HD",
        "sport": "Combat Sports",
        "sport_id": "combat",
        "league": "UFC",
        "country": "United States",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/382.png",
        "description": "24/7 live Octagon feed, UFC Fight Nights, early prelims, and historic fight archives.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 880000,
        "featured": True
    },
    {
        "id": "dazn-boxing-hd",
        "name": "DAZN Boxing & Combat HD",
        "sport": "Combat Sports",
        "sport_id": "combat",
        "league": "World Championship Boxing",
        "country": "International",
        "country_code": "INT",
        "language": "English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/86.png",
        "description": "World Title Boxing, Matchroom Boxing, and Golden Boy championship main events.",
        "stream_url": "https://epiembeds.online/embed/daznlaliga-es",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 630000,
        "featured": True
    }
]

BASEBALL_CHANNELS = [
    {
        "id": "mlb-network-hd",
        "name": "MLB Network HD (24/7)",
        "sport": "Baseball",
        "sport_id": "baseball",
        "league": "MLB",
        "country": "United States",
        "country_code": "US",
        "language": "English",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png",
        "description": "Official 24/7 Major League Baseball channel with live games, MLB Tonight, and highlights.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 610000,
        "featured": True
    }
]

CRICKET_CHANNELS = [
    {
        "id": "sky-sports-cricket-hd",
        "name": "Sky Sports Cricket HD (24/7)",
        "sport": "Cricket",
        "sport_id": "cricket",
        "league": "ICC & International Cricket",
        "country": "United Kingdom",
        "country_code": "GB",
        "language": "English (UK)",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png",
        "description": "The home of live international cricket, The Ashes, ICC World Cups, and County Cricket.",
        "stream_url": "https://epiembeds.online/embed/sky-sports-premier-league",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 1250000,
        "featured": True
    },
    {
        "id": "willow-cricket-hd",
        "name": "Willow Cricket HD USA",
        "sport": "Cricket",
        "sport_id": "cricket",
        "league": "IPL & Global T20",
        "country": "United States",
        "country_code": "US",
        "language": "English (US)",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png",
        "description": "Official 24/7 cricket channel in USA & Canada with live IPL, PSL, and ICC tournaments.",
        "stream_url": "https://epiembeds.online/embed/espn-usa",
        "is_embed": True,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 890000,
        "featured": True
    },
    {
        "id": "star-sports-1-hd",
        "name": "Star Sports 1 HD (Live)",
        "sport": "Cricket",
        "sport_id": "cricket",
        "league": "ICC / IPL / BCCI",
        "country": "India",
        "country_code": "IN",
        "language": "English / Hindi",
        "quality": "1080p 60fps",
        "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png",
        "description": "Prime broadcaster for Indian cricket, ICC World Cups, and Tata IPL.",
        "stream_url": "https://epiembeds.online/embed/tntsports1-uk",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 1400000,
        "featured": True
    },
    {
        "id": "ptv-sports-hd",
        "name": "PTV Sports HD Live",
        "sport": "Cricket",
        "sport_id": "cricket",
        "league": "Pakistan Cricket / PSL",
        "country": "Pakistan",
        "country_code": "PK",
        "language": "Urdu / English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/2964.png",
        "description": "National sports broadcaster of Pakistan featuring live PCB matches and HBL PSL.",
        "stream_url": "https://bein-xtra-bein.amagi.tv/playlist.m3u8",
        "is_embed": False,
        "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
        "is_live": True,
        "viewers": 950000,
        "featured": True
    },
    {
        "id": "sony-ten-cricket-hd",
        "name": "Sony Sports Ten 1 HD",
        "sport": "Cricket",
        "sport_id": "cricket",
        "league": "International Bilaterals",
        "country": "International",
        "country_code": "INT",
        "language": "English",
        "quality": "1080p HD",
        "logo": "https://a.espncdn.com/i/teamlogos/cricket/500/default.png",
        "description": "Live coverage of overseas cricket tours: England, Australia, South Africa, and Sri Lanka.",
        "stream_url": "https://epiembeds.online/embed/canalsport-pl",
        "is_embed": True,
        "backup_streams": ["https://bein-xtra-bein.amagi.tv/playlist.m3u8"],
        "is_live": True,
        "viewers": 720000,
        "featured": False
    }
]

ALL_CHANNELS = (
    CRICKET_CHANNELS +
    FOOTBALL_CHANNELS +
    BASKETBALL_CHANNELS +
    NFL_CHANNELS +
    MOTORSPORT_CHANNELS +
    TENNIS_CHANNELS +
    COMBAT_CHANNELS +
    BASEBALL_CHANNELS
)

SPORTS_CHANNELS = FOOTBALL_CHANNELS

def get_channels_for_sport(sport: str = "football"):
    s_key = (sport or "football").lower().strip()
    if s_key == "cricket":
        return CRICKET_CHANNELS
    elif s_key == "football":
        return FOOTBALL_CHANNELS
    elif s_key == "basketball":
        return BASKETBALL_CHANNELS
    elif s_key == "nfl":
        return NFL_CHANNELS
    elif s_key == "motorsport":
        return MOTORSPORT_CHANNELS
    elif s_key == "tennis":
        return TENNIS_CHANNELS
    elif s_key == "combat":
        return COMBAT_CHANNELS
    elif s_key == "baseball":
        return BASEBALL_CHANNELS
    return ALL_CHANNELS

FOOTBALL_LEAGUES = [
    {"id": "all", "name": "All Competitions", "emblem": ""},
    {"id": "epl", "name": "Premier League", "emblem": ""},
    {"id": "ucl", "name": "Champions League", "emblem": ""},
    {"id": "laliga", "name": "La Liga", "emblem": ""},
    {"id": "seriea", "name": "Serie A", "emblem": ""},
    {"id": "bundesliga", "name": "Bundesliga", "emblem": ""},
    {"id": "fra1", "name": "Ligue 1", "emblem": ""},
    {"id": "spl", "name": "Saudi Pro League", "emblem": ""},
]

SPORTS_CATEGORIES = [
    {"id": "all", "name": "All Channels", "icon": "Tv", "count": len(FOOTBALL_CHANNELS)},
    {"id": "epl", "name": "Premier League TV", "icon": "Tv", "count": 2},
    {"id": "ucl", "name": "Champions League TV", "icon": "Star", "count": 2},
    {"id": "laliga", "name": "La Liga TV", "icon": "Flame", "count": 2},
    {"id": "global", "name": "Global 24/7 Feeds", "icon": "Globe", "count": 3},
]

COUNTRIES = [
    {"code": "ALL", "name": "All Countries"},
    {"code": "GB", "name": "United Kingdom"},
    {"code": "ES", "name": "Spain"},
    {"code": "US", "name": "United States"},
    {"code": "INT", "name": "International"},
    {"code": "EU", "name": "Europe"},
]
