"""节流API"""

from fastapi import APIRouter

from echo.research.throttle_tool import get_throttle_tool


router = APIRouter(prefix="/api/throttle", tags=["throttle"])


@router.post("/throttle")
async def throttle(func, interval: float = 1.0):
    return {"result": get_throttle_tool(interval).throttle(func)}