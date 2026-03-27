"""滑动窗口API"""

from fastapi import APIRouter

from echo.research.window_by_size_tool import get_window_by_size_tool


router = APIRouter(prefix="/api/window-by-size", tags=["window-by-size"])


@router.post("/window")
async def window_by_size(items: list, size: int):
    return {"result": get_window_by_size_tool().window_by_size(items, size)}