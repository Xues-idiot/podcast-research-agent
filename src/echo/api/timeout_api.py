"""超时工具API"""

from fastapi import APIRouter

from echo.research.timeout_tool import get_timeout_tool


router = APIRouter(prefix="/api/timeout", tags=["timeout"])


@router.post("/timeout-after")
async def timeout_after(seconds: float):
    return {"result": get_timeout_tool().timeout_after(seconds, lambda: True)}