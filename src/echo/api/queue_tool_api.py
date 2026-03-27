"""异步池API"""

from fastapi import APIRouter

from echo.research.async_pool import get_async_pool


router = APIRouter(prefix="/api/async-pool", tags=["async-pool"])


@router.post("/gather")
async def gather(coros: list):
    """收集协程"""
    tool = get_async_pool()
    return {"result": await tool.gather(*coros)}
