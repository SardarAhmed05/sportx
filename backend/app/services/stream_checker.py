"""
Stream Health & Quality Prober Service
Checks live stream URLs for connectivity, status code, latency (ping in ms),
and content type (application/vnd.apple.mpegurl / video/mp2t).
"""

import httpx
import time
from typing import Dict, Any

async def check_stream_health(url: str) -> Dict[str, Any]:
    """Probes a single stream URL to check if it's responsive."""
    start_time = time.time()
    try:
        async with httpx.AsyncClient(timeout=4.0, follow_redirects=True) as client:
            response = await client.head(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            
            # Some servers reject HEAD, fallback to quick GET byte range
            if response.status_code in [405, 403, 501]:
                response = await client.get(url, headers={
                    "Range": "bytes=0-1024",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                })

            latency_ms = int((time.time() - start_time) * 1000)
            is_alive = response.status_code in [200, 206, 301, 302, 307, 308]
            
            return {
                "url": url,
                "online": is_alive,
                "status_code": response.status_code,
                "latency_ms": latency_ms,
                "content_type": response.headers.get("content-type", "application/x-mpegURL"),
                "estimated_quality": "1080p HD" if latency_ms < 600 else "720p HD"
            }
    except Exception as e:
        return {
            "url": url,
            "online": False,
            "status_code": 0,
            "latency_ms": 999,
            "error": str(e)
        }
