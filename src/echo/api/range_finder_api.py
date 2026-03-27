"""范围API"""

from fastapi import APIRouter

from echo.research.range_finder import get_range_finder


router = APIRouter(prefix="/api/range-finder", tags=["range-finder"])


@router.post("/range")
async def range_val(items: list):
    return {"result": get_range_finder().range(items)}
