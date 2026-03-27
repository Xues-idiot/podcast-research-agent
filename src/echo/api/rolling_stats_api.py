"""滚动统计API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.rolling_stats import get_rolling_stats


router = APIRouter(prefix="/api/rolling", tags=["rolling"])


class RollingRequest(BaseModel):
    data: list
    window: int


@router.post("/mean")
async def mean(request: RollingRequest):
    return {"result": get_rolling_stats().rolling_mean(request.data, request.window)}
