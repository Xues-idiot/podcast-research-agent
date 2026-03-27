"""滑动窗口API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.moving_window import get_moving_window


router = APIRouter(prefix="/api/moving-window", tags=["moving-window"])


class WindowRequest(BaseModel):
    items: list
    size: int


@router.post("/windowed")
async def windowed(request: WindowRequest):
    return {"result": get_moving_window().windowed(request.items, request.size)}
