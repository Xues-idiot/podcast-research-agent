"""统计API"""

from fastapi import APIRouter

from echo.research.stats_tool import get_stats_tool


router = APIRouter(prefix="/api/stats", tags=["stats"])


@router.post("/sum")
async def sum_items(items: list):
    return {"result": get_stats_tool().sum(items)}


@router.post("/product")
async def product(items: list):
    return {"result": get_stats_tool().product(items)}


@router.post("/variance")
async def variance(items: list):
    return {"result": get_stats_tool().variance(items)}


@router.post("/std-dev")
async def std_dev(items: list):
    return {"result": get_stats_tool().std_dev(items)}