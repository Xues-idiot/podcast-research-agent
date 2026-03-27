"""缓存装饰器API"""

from fastapi import APIRouter

from echo.research.cache_decorator import get_cache_decorator_tool


router = APIRouter(prefix="/api/cache-decorator", tags=["cache-decorator"])


@router.post("/memoize")
async def memoize_decorator(func):
    return {"result": get_cache_decorator_tool().memoize(func)}


@router.post("/clear-cache")
async def clear_cache(func):
    get_cache_decorator_tool().clear_cache(func)
    return {"success": True}