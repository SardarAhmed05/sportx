# SPORTX
### Global Multi-Sport Live Streaming, Match Center & Replays Vault

A high-performance, modern multi-sport broadcasting web application featuring real-time scores, multi-server auto-failover, 24/7 live television channels, a curated Cult Classics Vault, dual Multi-View split-screen playback, and a clean, responsive mobile architecture.

---

## Supported Sports Matrix

Every sport features full feature parity: live fixtures, scoreboard parsing, broadcast feeds, 24/7 television networks, and an archival replays vault:

| Position | Sport | Featured Competitions | 24/7 Live TV Channels | Replays & Cult Classics |
| :--- | :--- | :--- | :--- | :--- |
| **#1** | **Cricket** | ICC World Cup, IPL, PSL, County Championship, Tests | Star Sports 1 HD, Sky Sports Cricket, PTV Sports, Willow HD, Sony Ten 1 | Top 10 Cult Classics (2019 WC Final, Kohli MCG, Dhoni 2011) |
| **#2** | **Football** | Premier League, Champions League, La Liga, Serie A, Bundesliga | Sky Sports PL, TNT Sports, beIN Sports, Canal+ Sport | Top 10 Cult Classics (2022 WC Final, Istanbul 2005) + Recent Matches |
| **#3** | **Basketball** | NBA, WNBA, NCAA Men's Basketball | NBA TV HD (24/7), ESPN Basketball, TNT Sports | Top 10 Cult Classics (2016 Game 7, Jordan 1998, Ray Allen 2013) |
| **#4** | **American Football** | NFL, College Football (CFB) | NFL Network 24/7 HD, NFL RedZone, ESPN Sunday Night | Top 10 Cult Classics (28-3 Patriots Comeback, Helmet Catch) |
| **#5** | **Motorsport** | Formula 1 Grand Prix | Sky Sports F1 HD 1080p, F1 TV Pro, Canal+ F1 | Top 10 Cult Classics (2021 Abu Dhabi, 2011 Canada Button) |
| **#6** | **Tennis** | ATP Tour, WTA Tour, Grand Slams | Tennis Channel HD Live, Eurosport 1 Tennis | Top 10 Cult Classics (2008 Wimbledon Nadal vs Federer) |
| **#7** | **Combat Sports** | UFC PPV, Championship Boxing | UFC Fight Pass HD, DAZN Boxing & Combat | Top 10 Cult Classics (UFC 229 Khabib vs McGregor, Ali vs Foreman) |
| **#8** | **Baseball** | MLB World Series & Regular Season | MLB Network HD (24/7) | Top 10 Cult Classics (2016 Cubs Game 7, 2004 ALCS Red Sox) |

---

## Key Features

- **Zero-Emoji Minimal Classic Design**: Engineered to a strict aesthetic standard utilizing clean typography and Lucide vector graphics.
- **Centered Sport Switcher with 0ms Cache Hydration**: Instant sport switching powered by local cache pre-warming (`localStorage`), with the desktop dropdown mathematically centered in the top header.
- **Multi-Server Failover with Auto-Switching**: Every match and replay provides multiple verified broadcast feeds (YouTube, Dailymotion, Official TV Vault) with auto-detection if a stream becomes unavailable.
- **Cult Classics Vault**: Archival collections containing full match replays and extended highlights for the greatest moments in athletic history.
- **24/7 Television Networks**: Curated live broadcast networks with a **Popularity First vs Alphabetical (A-Z)** sorting toggle.
- **Dual Multi-View Studio**: Synchronized split-screen player to stream any two matches or TV feeds concurrently.
- **Mobile-First De-Cluttered UX**: Streamlined mobile header, expandable search bar, native slide-up bottom sheets for sport selection, and compact mobile match cards.
- **Bespoke Minimal Classic SVG Logo & Favicon**: Custom luxury geometric athletic monogram (Obsidian squircle, emerald chamfer border, platinum S-ribbon, and velocity cross-blade forming the 'X').

---

## Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Lucide Icons, Hls.js
- **Backend**: Python 3.11+, FastAPI, Uvicorn, HTTPX, BeautifulSoup4, Pydantic
- **Deployment Targets**: Vercel (Edge CDN & Serverless), Render, Railway

---

## Local Development Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.10+

### Option A: Windows 1-Click Launchers
- **Start All Services**: Double-click `run_project.bat` in the root folder.
- **Stop All Services**: Double-click `stop_project.bat` in the root folder.

### Option B: Manual Setup

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd sports
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate

   pip install -r requirements.txt
   python run.py
   ```
   *Backend runs at `http://127.0.0.1:8000` (API Docs: `http://127.0.0.1:8000/docs`)*

3. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   *Frontend runs at `http://localhost:5173`*

---

## Production Deployment

### Option 1: 100% All-in-One on Vercel
The repository is pre-configured with `vercel.json` and `api/index.py` for full-stack Vercel hosting:
1. Push your repository to GitHub.
2. In Vercel, click **Add New...** → **Project** and select your repository.
3. Keep the Root Directory as `./` and click **Deploy**.
4. Vercel builds the React frontend into `frontend/dist` and mounts the FastAPI backend as Serverless Functions at `/api/*`.

### Option 2: Vercel (Frontend) + Render (Backend) — *Recommended for Streaming*
For 24/7 continuous stream scrapers and long-lived proxy connections without serverless execution timeouts:
1. **Deploy Backend to [Render.com](https://render.com)**:
   - Create a **New Web Service** connected to your repo.
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Render assigns a URL like `https://sportx-api.onrender.com`.
2. **Deploy Frontend to [Vercel.com](https://vercel.com)**:
   - Import the repository and set Root Directory to `frontend`.
   - Add an Environment Variable:
     - `VITE_API_URL` = `https://sportx-api.onrender.com`
   - Click **Deploy**.

---

## API Reference

| Method | Endpoint | Description | Query Parameters |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/matches/overview` | Active fixtures, live scores, leagues, and marquee showcase | `sport` (e.g. `cricket`, `football`, `basketball`, `nfl`, `motorsport`, `tennis`, `combat`, `baseball`) |
| `GET` | `/api/matches/replays` | Full match replays, classic archives, and category metadata | `sport`, `category`, `q` |
| `GET` | `/api/matches/replay-streams` | Multi-server stream resolution for selected replay | `home`, `away`, `competition` |
| `GET` | `/api/channels` | 24/7 live television channels | `sport`, `country`, `q` |
| `GET` | `/api/channels/categories` | Available channel sport categories and countries | None |
| `GET` | `/api/proxy/stream` | HLS stream proxy with dynamic CORS headers | `url` |
| `POST` | `/api/scraper/trigger` | Trigger real-time background scraper refresh | None |
| `GET` | `/health` | Service health status check | None |

---

## License
MIT License. Built for sports fans and developers worldwide.
