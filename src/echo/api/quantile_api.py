"""分位数API"""

from fastapi import APIRouter

from echo.research.quantile_tool import get_quantile_tool


router = APIRouter(prefix="/api/quantile", tags=["quantile"])


@router.post("/percentile")
async def percentile(items: list, percent: float):
    return {"result": get_quantile_tool().percentile(items, percent)}