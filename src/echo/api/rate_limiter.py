"""速率限制API"""

from fastapi import APIRouter

from echo.research.rate_limiter import get_rate_limiter


router = APIRouter(prefix="/api/rate_limit", tags=["rate_limit"])


@router.post("/check")
async def check_rate_limit(key: str, max_requests: int = 60, window_seconds: int = 60):
    allowed = get_rate_limiter().is_allowed(key, max_requests, window_seconds)
    return {"allowed": allowed, "max_requests": max_requests, "window_seconds": window_seconds}


@router.post("/reset")
async def reset_rate_limit(key: str):
    get_rate_limiter().reset(key)
    return {"success": True}