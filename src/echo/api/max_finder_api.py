"""最大值查找API"""

from fastapi import APIRouter

from echo.research.max_finder import get_max_finder


router = APIRouter(prefix="/api/max-finder", tags=["max-finder"])


@router.post("/max")
async def max_value(items: list):
    return {"result": get_max_finder().max(items)}