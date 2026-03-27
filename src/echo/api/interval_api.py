"""区间API"""

from fastapi import APIRouter

from echo.research.interval_tool import get_interval_tool


router = APIRouter(prefix="/api/interval", tags=["interval"])


@router.post("/in-interval")
async def in_interval(value: float, low: float, high: float):
    return {"result": get_interval_tool().in_interval(value, low, high)}


@router.post("/clamp")
async def clamp(value: float, low: float, high: float):
    return {"result": get_interval_tool().clamp(value, low, high)}


@router.post("/overlap")
async def overlap(a: tuple, b: tuple):
    return {"result": get_interval_tool().overlap(a, b)}