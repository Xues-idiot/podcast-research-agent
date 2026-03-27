"""比较工具API"""

from fastapi import APIRouter

from echo.research.comparator_tool import get_comparator_tool


router = APIRouter(prefix="/api/comparator", tags=["comparator"])


@router.post("/equal")
async def equal(a, b):
    return {"result": get_comparator_tool().equal(a, b)}


@router.post("/greater")
async def greater(a, b):
    return {"result": get_comparator_tool().greater(a, b)}


@router.post("/less")
async def less(a, b):
    return {"result": get_comparator_tool().less(a, b)}


@router.post("/between")
async def between(value, low, high):
    return {"result": get_comparator_tool().between(value, low, high)}