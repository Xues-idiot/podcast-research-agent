"""比较API"""

from fastapi import APIRouter

from echo.research.compare_tool import get_compare_tool


router = APIRouter(prefix="/api/compare", tags=["compare"])


@router.post("/greater-than")
async def greater_than(a, b):
    return {"result": get_compare_tool().greater_than(a, b)}


@router.post("/less-than")
async def less_than(a, b):
    return {"result": get_compare_tool().less_than(a, b)}


@router.post("/equal")
async def equal(a, b):
    return {"result": get_compare_tool().equal(a, b)}