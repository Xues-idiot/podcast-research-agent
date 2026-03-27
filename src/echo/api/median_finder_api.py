"""中位数API"""

from fastapi import APIRouter

from echo.research.median_finder import get_median_finder


router = APIRouter(prefix="/api/median-finder", tags=["median-finder"])


@router.post("/median")
async def median(items: list):
    return {"result": get_median_finder().median(items)}
