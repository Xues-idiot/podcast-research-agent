"""工作者API"""

from fastapi import APIRouter

from echo.research.worker_tool import get_worker_tool


router = APIRouter(prefix="/api/worker", tags=["worker"])


@router.post("/map-reduce")
async def map_reduce(map_func: str, reduce_func: str, items: list):
    """MapReduce"""
    tool = get_worker_tool()
    map_obj = eval(map_func)
    reduce_obj = eval(reduce_func)
    return {"result": tool.map_reduce(map_obj, reduce_obj, items)}
