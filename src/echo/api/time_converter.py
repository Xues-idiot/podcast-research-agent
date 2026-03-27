"""时间转换API"""

from fastapi import APIRouter

from echo.research.time_converter import get_time_converter


router = APIRouter(prefix="/api/time", tags=["time"])


@router.post("/seconds_to_readable")
async def seconds_to_readable(seconds: int):
    return {"result": get_time_converter().seconds_to_readable(seconds)}


@router.post("/minutes_to_readable")
async def minutes_to_readable(minutes: int):
    return {"result": get_time_converter().minutes_to_readable(minutes)}