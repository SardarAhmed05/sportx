"""
Live Sports Stream Scraper & IPTV Aggregator Service
Fetches, scrapes, and parses sports streams, HLS feeds (.m3u8), and live event links
from public sports directories, IPTV playlists, and Free-to-Air streams worldwide.
"""

import httpx
import re
import asyncio
from typing import List, Dict, Any
from app.data.channels_db import ALL_CHANNELS, SPORTS_CHANNELS, SPORTS_CATEGORIES

# Public IPTV sports m3u sources for real-time aggregation
IPTV_SOURCES = [
    "https://iptv-org.github.io/iptv/categories/sports.m3u",
]

class StreamScraperService:
    def __init__(self):
        self.cached_scraped_channels: List[Dict[str, Any]] = []
        self.last_scraped_at = None
        self.is_scraping = False

    async def scrape_m3u_playlist(self, url: str) -> List[Dict[str, Any]]:
        """Scrapes and parses an external M3U sports playlist."""
        channels = []
        try:
            async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
                response = await client.get(url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                })
                if response.status_code == 200:
                    text = response.text
                    lines = text.splitlines()
                    current_item = {}
                    
                    for line in lines:
                        line = line.strip()
                        if line.startswith("#EXTINF:"):
                            # Parse metadata
                            name_match = re.search(r',([^,]+)$', line)
                            name = name_match.group(1).strip() if name_match else "Sports Stream"
                            
                            logo_match = re.search(r'tvg-logo="([^"]*)"', line)
                            logo = logo_match.group(1) if logo_match else ""
                            
                            group_match = re.search(r'group-title="([^"]*)"', line)
                            group = group_match.group(1) if group_match else "Sports"
                            
                            country_match = re.search(r'tvg-country="([^"]*)"', line)
                            country_code = country_match.group(1).upper() if country_match else "INT"
                            
                            current_item = {
                                "name": name,
                                "logo": logo or "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=150&auto=format&fit=crop&q=80",
                                "group": group,
                                "country_code": country_code,
                            }
                        elif line and not line.startswith("#") and (line.startswith("http://") or line.startswith("https://")):
                            if current_item:
                                stream_url = line
                                name_lower = current_item.get("name", "").lower()
                                
                                # Classify sport priority
                                if any(k in name_lower for k in ["football", "soccer", "laliga", "premier", "serie a", "bundesliga", "uefa", "fifa", "fc ", "united", "chelsea", "arsenal", "real madrid", "barca", "milan", "bayern"]):
                                    sport = "Football"
                                    priority = 1
                                    category = "Football"
                                elif any(k in name_lower for k in ["cricket", "willow", "ipl", "psl", "bbl", "star sports", "sky cricket", "ptv sports", "sony ten"]):
                                    sport = "Cricket"
                                    priority = 2
                                    category = "Cricket"
                                else:
                                    sport = "Worldwide Sports"
                                    priority = 3
                                    category = "Multi-sport"
                                
                                channel_id = f"scraped-{re.sub(r'[^a-zA-Z0-9]', '-', name_lower)[:30]}-{len(channels)}"
                                
                                channels.append({
                                    "id": channel_id,
                                    "name": current_item.get("name", "Live Sports Channel"),
                                    "sport": sport,
                                    "priority": priority,
                                    "category": category,
                                    "country": current_item.get("country_code", "International"),
                                    "country_code": current_item.get("country_code", "INT"),
                                    "language": "International",
                                    "quality": "HD",
                                    "logo": current_item.get("logo"),
                                    "description": f"Live sports broadcast from {current_item.get('name')}",
                                    "stream_url": stream_url,
                                    "backup_streams": ["https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"],
                                    "is_live": True,
                                    "viewers": 50000 + (len(channels) * 1200) % 250000,
                                    "scraped": True
                                })
                                current_item = {}
        except Exception as e:
            print(f"Error scraping M3U playlist: {e}")
        return channels

    async def get_all_channels(self, sport_filter: str = None, country_filter: str = None, query: str = None) -> List[Dict[str, Any]]:
        """
        Combines curated high-reliability channels with dynamically scraped channels.
        Always orders by Priority: Football (1) > Cricket (2) > Other Sports (3).
        """
        all_channels = list(ALL_CHANNELS)
        
        # Add cached scraped channels if available
        if self.cached_scraped_channels:
            all_channels.extend(self.cached_scraped_channels)
            
        # Apply filters
        filtered = all_channels
        if sport_filter and sport_filter.lower() != "all":
            sf = sport_filter.lower().strip()
            if sf in ["football", "soccer"]:
                filtered = [c for c in filtered if (c.get("sport_id") == "football" or c.get("sport") == "Football")]
            elif sf in ["nfl", "american football"]:
                filtered = [c for c in filtered if (c.get("sport_id") == "nfl" or c.get("sport") == "American Football")]
            else:
                filtered = [
                    c for c in filtered 
                    if c.get("sport", "").lower() == sf 
                    or c.get("sport_id", "").lower() == sf 
                    or c.get("category", "").lower() == sf 
                    or (sf in c.get("sport", "").lower())
                    or (c.get("sport_id", "").lower() in sf)
                ]
            
        if country_filter and country_filter.upper() != "ALL":
            filtered = [c for c in filtered if c.get("country_code", "").upper() == country_filter.upper()]
            
        if query:
            q = query.lower()
            filtered = [c for c in filtered if q in c.get("name", "").lower() or q in c.get("sport", "").lower() or q in c.get("description", "").lower()]
            
        # Sort by priority ascending (1 = Football, 2 = Cricket, 3 = Others) then by viewers descending
        filtered.sort(key=lambda c: (c.get("priority", 99), -c.get("viewers", 0)))
        return filtered

    async def trigger_live_scrape(self):
        """Asynchronously refreshes external sports streams."""
        if self.is_scraping:
            return {"status": "scraping_in_progress", "count": len(self.cached_scraped_channels)}
            
        self.is_scraping = True
        try:
            tasks = [self.scrape_m3u_playlist(src) for src in IPTV_SOURCES]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            scraped = []
            for res in results:
                if isinstance(res, list):
                    scraped.extend(res)
            
            # Keep top scraped channels
            self.cached_scraped_channels = scraped[:60]
            return {
                "status": "success",
                "scraped_count": len(self.cached_scraped_channels),
                "total_channels": len(SPORTS_CHANNELS) + len(self.cached_scraped_channels)
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            self.is_scraping = False

scraper_service = StreamScraperService()
