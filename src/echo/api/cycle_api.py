"""循环API"""

from fastapi import APIRouter

from echo.research.cycle_tool import get_cycle_tool


router = APIRouter(prefix="/api/cycle", tags=["cycle"])


@router.post("/cycle")
async def cycle(items: list, times: int):
    return {"result": get_cycle_tool().cycle(items, times)}