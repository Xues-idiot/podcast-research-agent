"""滑动窗口迭代API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.sliding_window_iter import get_sliding_window_iter


router = APIRouter(prefix="/api/sliding-iter", tags=["sliding-iter"])


class SlideRequest(BaseModel):
    items: list
    size: int
    step: int = 1


@router.post("/slide")
async def slide(request: SlideRequest):
    return {"result": list(get_sliding_window_iter().slide(request.items, request.size, request.step))}
