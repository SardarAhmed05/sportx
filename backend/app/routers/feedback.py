"""
Community Feedback and Comments Router
Stores and serves user match requests, feedback, bug reports, and suggestions.
"""

import json
import os
import time
import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

router = APIRouter(prefix="/api/feedback", tags=["Community Feedback"])

FEEDBACK_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "feedback.json")

class FeedbackCreateRequest(BaseModel):
    name: Optional[str] = Field(None, description="User display name")
    user_name: Optional[str] = Field(None, description="User display name alias")
    category: Optional[str] = Field("General Feedback", description="Feedback category")
    message: Optional[str] = Field(None, description="Feedback message")
    comment: Optional[str] = Field(None, description="Feedback comment alias")
    rating: Optional[int] = Field(5, ge=1, le=5, description="Star rating")

def load_feedback_data() -> List[dict]:
    if not os.path.exists(FEEDBACK_FILE):
        return []
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def save_feedback_data(data: List[dict]) -> bool:
    try:
        os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False

@router.get("")
async def get_all_feedback():
    """Returns all community feedback comments, sorted newest first."""
    data = load_feedback_data()
    # Normalize fields for client compatibility
    for item in data:
        if "user_name" not in item:
            item["user_name"] = item.get("name", "Sports Fan")
        if "comment" not in item:
            item["comment"] = item.get("message", "")
        if "created_at" not in item:
            item["created_at"] = item.get("created_at_formatted", "Recently")
    data.sort(key=lambda x: x.get("timestamp", x.get("created_at_num", 0)), reverse=True)
    return data

@router.post("")
async def submit_feedback(payload: FeedbackCreateRequest):
    """Submits a new user feedback comment or stream request."""
    data = load_feedback_data()
    
    clean_name = (payload.user_name or payload.name or "Sports Fan").strip()[:50]
    clean_category = (payload.category or "General Feedback").strip()
    clean_comment = (payload.comment or payload.message or "").strip()

    if not clean_comment:
        clean_comment = "Great experience watching live sports."

    now = time.time()
    dt = datetime.datetime.fromtimestamp(now, datetime.timezone.utc)
    formatted_date = dt.strftime("%b %d, %Y")

    new_entry = {
        "id": f"fb-{int(now * 1000)}",
        "name": clean_name if clean_name else "Sports Fan",
        "user_name": clean_name if clean_name else "Sports Fan",
        "category": clean_category,
        "message": clean_comment,
        "comment": clean_comment,
        "rating": payload.rating or 5,
        "likes": 0,
        "created_at": formatted_date,
        "timestamp": now,
        "created_at_num": now
    }

    # Prepend new comment
    data.insert(0, new_entry)
    # Keep up to 250 recent comments
    data = data[:250]
    save_feedback_data(data)

    return new_entry

@router.post("/{comment_id}/like")
async def like_feedback(comment_id: str):
    """Increments the upvote/like count for a feedback comment."""
    data = load_feedback_data()
    found = False
    new_likes = 0
    for item in data:
        if item.get("id") == comment_id:
            item["likes"] = item.get("likes", 0) + 1
            new_likes = item["likes"]
            found = True
            break
    
    if not found:
        raise HTTPException(status_code=404, detail="Comment not found")
        
    save_feedback_data(data)
    return {"status": "success", "id": comment_id, "likes": new_likes}
