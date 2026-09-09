# SPORTCAST LIVE ⚽🏏📺
### Global Sports Live Stream Aggregator & Scraper Platform

A high-performance live sports streaming web platform with real-time stream scrapers, built-in CORS HLS stream proxy, multi-server mirror switching, and dual Multi-View split-screen broadcasting.

---

## 🏆 Priority Architecture

1. **⚽ TOP PRIORITY #1 — Football Arena**:
   - Premier League (EPL), UEFA Champions League (UCL), La Liga, Serie A, Bundesliga, Saudi Pro League.
   - Live Match Center: Real-time score, minute indicator (`68'`), possession ratio, goal timelines, shots on target, yellow/red cards.
   - Dedicated 24/7 Football TV Networks: Sky Sports Football, TNT Sports 1, beIN Sports Global, DAZN Football, SuperSport Premier League, FIFA+ TV.

2. **🏏 TOP PRIORITY #2 — Cricket Pavilion**:
   - Indian Premier League (IPL), ICC Champions Trophy & World Cups, Pakistan Super League (PSL), Big Bash League (BBL), Test Series.
   - Real-time Ball-by-Ball Scorecard: Team scores, overs, current run rate (CRR), required run rate (RRR), active batsmen on crease (runs, balls, 4s, 6s, strike rate), active bowler figures, recent balls timeline (`4 1 W 0 6 1`).
   - Dedicated 24/7 Cricket TV Networks: Sky Sports Cricket, Willow TV HD, Star Sports 1 HD, Sony Sports Ten 5, PTV Sports HD, Astro Cricket.

3. **📺 24/7 Worldwide Sports Channels & Multi-Sport Hub**:
   - Category filter: Basketball (NBA), Motorsport (Formula 1, MotoGP), Combat Sports (UFC, Boxing), Tennis (Grand Slams).
   - Country filter: UK, USA, India, Pakistan, Germany, Qatar, South Africa, France, Malaysia, and Global feeds.

---

## ⚡ Key Technical Features

- **HLS Adaptive Video Player**: High-definition `.m3u8` video player built on `Hls.js` with auto bitrate adjustment (1080p 60fps / 720p / SD).
- **Built-in CORS & Referrer Stream Proxy (`/api/proxy/stream`)**: Automatically rewrites playlist segments and proxies streams to bypass browser CORS headers or origin locks.
- **Multi-Server Mirror Switcher**: 1-click fallback across multiple redundant stream servers (Server 1 HD, Server 2 FHD, Server 3 Low Latency).
- **Dual-Stream Multi-View Studio**: Watch a Football match and a Cricket match side-by-side on a split screen with independent controls.
- **Live Stream Health & Ping Diagnostics**: Probes stream latency in real-time (`45ms`, `1080p HD`).
- **Live Fan Chat Simulation**: Interactive real-time crowd reactions, goal alerts, sixes, and user chat.
- **Custom Stream URL Player**: Play any external `.m3u8` or live stream URL.
- **Local Favorites**: Bookmark favorite teams, matches, and channels.

---

## 🚀 Quick Start Guide

### 1. One-Click Launch (Windows)
Double-click `run_project.bat` in the root folder, or run in terminal:
```bash
.\run_project.bat
```

### 2. Manual Launch

**Backend (FastAPI)**:
```bash
cd backend
.\venv\Scripts\activate
python run.py
```
*API will run at `http://127.0.0.1:8000` (Swagger Docs: `http://127.0.0.1:8000/docs`)*

**Frontend (React + Vite + Tailwind CSS)**:
```bash
cd frontend
npm run dev
```
*Frontend will run at `http://localhost:5173`*

---

## 📡 API Endpoints

- `GET /api/matches/overview` — Top spotlight marquee clash + Football & Cricket live overview
- `GET /api/matches/football` — Live football matches & league standings
- `GET /api/matches/cricket` — Live cricket matches & ball-by-ball scorecards
- `GET /api/matches/detail/{id}` — In-depth match statistics and lineups
- `GET /api/channels` — Worldwide 24/7 sports channels with sport/country/search filters
- `GET /api/channels/categories` — Sports categories & country lists
- `GET /api/proxy/stream?url=...` — HLS stream proxy with CORS rewrite
- `POST /api/scraper/trigger` — Scrape and update live sports feeds
- `GET /api/scraper/check-stream?url=...` — Stream latency & health tester
