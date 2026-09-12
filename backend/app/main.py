"""
Main FastAPI Application Entrypoint
Sports Stream Scraper & Live Broadcast Hub
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import asyncio

from app.routers import matches, channels, proxy, scraper, feedback
from app.services.stream_scraper import scraper_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: pre-warm football matches cache & trigger background stream scraper
    from app.services.football_service import football_engine
    asyncio.create_task(football_engine.fetch_all_real_matches())
    asyncio.create_task(scraper_service.trigger_live_scrape())
    yield
    # Shutdown logic if any

app = FastAPI(
    title="TimStreams / SportX Football Live Stream Engine API",
    description="Worldwide Football (Soccer) Live Match & TV Channel Aggregator.",
    version="2.0.0",
    lifespan=lifespan
)

# Enable CORS for all origins and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(matches.router)
app.include_router(channels.router)
app.include_router(proxy.router)
app.include_router(scraper.router)
app.include_router(feedback.router)

@app.get("/")
async def root():
    return {
        "message": "Football Live Stream Hub API is online",
        "sport": "Football (Soccer)",
        "endpoints": [
            "/api/matches/overview",
            "/api/matches/football",
            "/api/channels",
            "/api/channels/categories",
            "/api/proxy/stream",
            "/api/scraper/trigger"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "sport": "Football"}
