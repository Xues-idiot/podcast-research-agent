"""窗口制造API"""

from fastapi import APIRouter

from echo.research.window_maker_tool import get_window_maker_tool


router = APIRouter(prefix="/api/window-maker", tags=["window-maker"])


@router.post("/make")
async def make_window(items: list, size: int):
    return {"result": get_window_maker_tool().make_window(items, size)}