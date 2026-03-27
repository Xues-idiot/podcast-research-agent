"""LRU缓存工具API"""

from fastapi import APIRouter

from echo.research.lru_cache_tool import get_lru_cache_tool


router = APIRouter(prefix="/api/lru-cache", tags=["lru-cache"])


@router.post("/cache")
async def create_cache(func):
    return {"result": get_lru_cache_tool().lru_cache()(func)}