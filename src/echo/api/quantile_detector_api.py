"""分位数检测API"""

from fastapi import APIRouter

from echo.research.quantile_detector import get_quantile_detector


router = APIRouter(prefix="/api/quantile", tags=["quantile"])


@router.post("/quartiles")
async def quartiles(data: list):
    return {"result": get_quantile_detector().quartiles(data)}
