"""累积计算API"""

from fastapi import APIRouter

from echo.research.cumulative_tool import get_cumulative_tool


router = APIRouter(prefix="/api/cumulative", tags=["cumulative"])


@router.post("/cumsum")
async def cumsum(data: list):
    return {"result": get_cumulative_tool().cumsum(data)}
