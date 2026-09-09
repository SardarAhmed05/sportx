"""
Channels Router
Exposes 24/7 Worldwide sports channels, priority filtering, country filtering,
and stream sources.
"""

from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.services.stream_scraper import scraper_service
from app.data.channels_db import SPORTS_CATEGORIES, COUNTRIES, SPORTS_CHANNELS

router = APIRouter(prefix="/api/channels", tags=["Worldwide Channels"])

@router.get("")
async def get_channels(
    sport: Optional[str] = Query(None, description="Sport filter (e.g. football, cricket, basketball)"),
    country: Optional[str] = Query(None, description="Country code (e.g. GB, IN, US)"),
    q: Optional[str] = Query(None, description="Search query")
):
    """Retrieve worldwide sports channels sorted by priority (Football > Cricket > Others)."""
    channels = await scraper_service.get_all_channels(
        sport_filter=sport,
        country_filter=country,
        query=q
    )
    return {
        "total": len(channels),
        "channels": channels
    }

@router.get("/categories")
async def get_categories():
    """Retrieve sports categories with icons and counts."""
    return {
        "categories": SPORTS_CATEGORIES,
        "countries": COUNTRIES
    }

@router.get("/{channel_id}")
async def get_channel_detail(channel_id: str):
    """Retrieve single channel info and backup streams."""
    channels = await scraper_service.get_all_channels()
    for c in channels:
        if c["id"] == channel_id:
            return c
    raise HTTPException(status_code=404, detail="Channel not found")
