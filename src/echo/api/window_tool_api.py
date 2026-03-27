"""窗口工具API"""

from fastapi import APIRouter

from echo.research.window_tool import get_window_tool


router = APIRouter(prefix="/api/window", tags=["window"])


@router.post("/sliding")
async def sliding_window(items: list, size: int):
    return {"result": get_window_tool().sliding_window(items, size)}


@router.post("/moving-avg")
async def moving_average(items: list, window: int):
    return {"result": get_window_tool().moving_average(items, window)}