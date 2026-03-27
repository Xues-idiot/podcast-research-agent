"""线程池API"""

from fastapi import APIRouter

from echo.research.thread_tool import get_thread_pool_tool


router = APIRouter(prefix="/api/thread", tags=["thread"])


@router.post("/map")
async def thread_map(func: str, items: list, max_workers: int = 4):
    """线程池映射"""
    tool = get_thread_pool_tool()
    func_obj = eval(func)
    return {"results": tool.map(func_obj, items, max_workers)}
