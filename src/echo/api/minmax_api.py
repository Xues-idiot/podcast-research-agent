"""最小最大API"""

from fastapi import APIRouter

from echo.research.minmax_tool import get_minmax_tool


router = APIRouter(prefix="/api/minmax", tags=["minmax"])


@router.post("/min")
async def min_value(items: list):
    return {"result": get_minmax_tool().min_value(items)}


@router.post("/max")
async def max_value(items: list):
    return {"result": get_minmax_tool().max_value(items)}


@router.post("/min-max")
async def min_max(items: list):
    return {"result": get_minmax_tool().min_max(items)}