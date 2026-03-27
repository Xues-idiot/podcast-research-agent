"""范围API"""

from fastapi import APIRouter

from echo.research.range_tool import get_range_tool


router = APIRouter(prefix="/api/range", tags=["range"])


@router.post("/range")
async def range(start: int, stop: int, step: int = 1):
    return {"result": get_range_tool().range(start, stop, step)}