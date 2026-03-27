"""滑动窗口速率限制API"""

from fastapi import APIRouter

from echo.research.sliding_window import get_sliding_window_rate_limiter


router = APIRouter(prefix="/api/sliding-window", tags=["sliding-window"])


@router.post("/allow")
async def allow():
    return {"result": get_sliding_window_rate_limiter().allow()}
