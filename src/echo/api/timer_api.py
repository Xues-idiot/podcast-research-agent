"""计时器API"""

from fastapi import APIRouter

from echo.research.timer_tool import get_timer_tool


router = APIRouter(prefix="/api/timer", tags=["timer"])


@router.post("/start")
async def start():
    get_timer_tool().start()
    return {"success": True}


@router.post("/stop")
async def stop():
    return {"result": get_timer_tool().stop()}


@router.get("/elapsed")
async def elapsed():
    return {"result": get_timer_tool().elapsed()}