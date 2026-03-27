"""最小值查找API"""

from fastapi import APIRouter

from echo.research.min_finder import get_min_finder


router = APIRouter(prefix="/api/min-finder", tags=["min-finder"])


@router.post("/min")
async def min_value(items: list):
    return {"result": get_min_finder().min(items)}