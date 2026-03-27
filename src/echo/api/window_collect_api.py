"""窗口聚合API"""

from fastapi import APIRouter

from echo.research.window_collect import get_window_collect


router = APIRouter(prefix="/api/window", tags=["window"])


@router.post("/collect")
async def window_collect(items: list, size: int, agg: str):
    """窗口聚合"""
    tool = get_window_collect()
    agg_func = eval(agg)
    return {"result": tool.window_collect(items, size, agg_func)}


@router.post("/moving-avg")
async def moving_avg(items: list, size: int):
    """移动平均"""
    tool = get_window_collect()
    return {"result": tool.moving_avg(items, size)}
