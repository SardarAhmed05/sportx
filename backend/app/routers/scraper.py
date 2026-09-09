"""
Scraper Router
Provides endpoints to trigger live stream scraping, check stream connectivity,
and retrieve scraper statistics.
"""

from fastapi import APIRouter, Query, BackgroundTasks
from app.services.stream_scraper import scraper_service
from app.services.stream_checker import check_stream_health

router = APIRouter(prefix="/api/scraper", tags=["Stream Scraper"])

@router.post("/trigger")
async def trigger_scrape(background_tasks: BackgroundTasks):
    """Triggers real-time scraping of global sports stream feeds in background."""
    background_tasks.add_task(scraper_service.trigger_live_scrape)
    return {
        "status": "scraping_started",
        "message": "Background live stream scrape initiated",
        "cached_count": len(scraper_service.cached_scraped_channels)
    }

@router.get("/status")
async def scraper_status():
    """Returns current status of scraper cache."""
    return {
        "is_scraping": scraper_service.is_scraping,
        "scraped_channels_count": len(scraper_service.cached_scraped_channels),
        "last_scraped_at": scraper_service.last_scraped_at
    }

@router.get("/check-stream")
async def check_stream(url: str = Query(..., description="Stream URL to check")):
    """Tests latency, HTTP status, and online health of a stream."""
    return await check_stream_health(url)
