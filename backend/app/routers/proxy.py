"""
Bulletproof CORS Stream Proxy Router
Handles HLS (.m3u8) playlists and media segment streaming (.ts, .m4s, .mp4, .aac, .key)
Bypasses browser CORS restrictions, rewrites playlist URLs recursively, and forwards Range requests.
"""

from fastapi import APIRouter, Query, Request, Response, HTTPException
from fastapi.responses import StreamingResponse
import httpx
from urllib.parse import urljoin, quote, unquote
import re

router = APIRouter(prefix="/api/proxy", tags=["Stream Proxy"])

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.google.com",
    "Referer": "https://www.google.com/"
}

@router.get("/stream")
async def proxy_stream(request: Request, url: str = Query(..., description="Stream target URL")):
    """
    Proxies stream playlists and chunks with full CORS headers.
    """
    clean_url = unquote(url).strip()
    if not clean_url or not clean_url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="Invalid stream URL format")

    try:
        # Check if client requested a specific Byte Range (for video seeking)
        forward_headers = dict(DEFAULT_HEADERS)
        range_header = request.headers.get("range")
        if range_header:
            forward_headers["range"] = range_header

        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True, verify=False) as client:
            resp = await client.get(clean_url, headers=forward_headers)
            
            content_type = resp.headers.get("content-type", "").lower()
            status_code = resp.status_code

            if status_code >= 400:
                # Return empty fallback or 502 with detail
                raise HTTPException(status_code=502, detail=f"Upstream server returned HTTP {status_code}")

            # Check if this is a binary media segment (.ts, .mp4, .m4s, .aac, video/*, octet-stream)
            raw_bytes = resp.content
            is_m3u8 = (
                "mpegurl" in content_type or 
                "m3u8" in clean_url.split("?")[0].lower() or 
                raw_bytes.startswith(b"#EXTM3U") or 
                raw_bytes.startswith(b"#EXT-X-")
            )

            if not is_m3u8:
                response_headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
                    "Access-Control-Allow-Headers": "*",
                    "Cache-Control": "public, max-age=120",
                    "Content-Type": content_type or "video/MP2T"
                }
                if "content-range" in resp.headers:
                    response_headers["Content-Range"] = resp.headers["content-range"]
                if "content-length" in resp.headers:
                    response_headers["Content-Length"] = resp.headers["content-length"]

                return Response(
                    content=raw_bytes,
                    status_code=status_code,
                    headers=response_headers,
                    media_type=content_type or "video/MP2T"
                )

            # Otherwise, parse and rewrite the HLS .m3u8 playlist
            text = resp.text
            base_url = str(resp.url)
            lines = text.splitlines()
            rewritten_lines = []
            
            # Proxy base prefix for nested requests
            proxy_prefix = f"{request.base_url}api/proxy/stream?url="

            for line in lines:
                raw_line = line.strip()
                if not raw_line:
                    rewritten_lines.append(raw_line)
                    continue

                if raw_line.startswith("#"):
                    # Rewrite URI="..." in tags like #EXT-X-STREAM-INF, #EXT-X-MEDIA, #EXT-X-KEY, #EXT-X-MAP
                    if 'URI="' in raw_line:
                        def replace_uri(match):
                            nested = match.group(1)
                            abs_nested = urljoin(base_url, nested)
                            return f'URI="{proxy_prefix}{quote(abs_nested)}"'
                        raw_line = re.sub(r'URI="([^"]+)"', replace_uri, raw_line)
                    rewritten_lines.append(raw_line)
                else:
                    # Segment or sub-playlist URL line
                    abs_url = urljoin(base_url, raw_line)
                    rewritten_lines.append(f"{proxy_prefix}{quote(abs_url)}")

            output_playlist = "\n".join(rewritten_lines)
            
            return Response(
                content=output_playlist,
                status_code=200,
                media_type="application/vnd.apple.mpegurl",
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
                    "Access-Control-Allow-Headers": "*",
                    "Cache-Control": "no-cache, no-store, must-revalidate"
                }
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Proxy error connecting to source: {str(e)}")

@router.options("/stream")
async def proxy_options():
    return Response(
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )
