"""延迟API"""

from fastapi import APIRouter

from echo.research.delay_tool import get_delay_tool


router = APIRouter(prefix="/api/delay", tags=["delay"])


@router.post("/delay")
async def delay(seconds: float):
    get_delay_tool().delay(seconds)
    return {"success": True}


@router.post("/delay-ms")
async def delay_ms(milliseconds: int):
    get_delay_tool().delay_ms(milliseconds)
    return {"success": True}