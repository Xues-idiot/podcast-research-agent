"""缓存API"""

from fastapi import APIRouter

from echo.research.cache_manager import get_cache_manager


router = APIRouter(prefix="/api/cache", tags=["cache"])


@router.post("/set")
async def set_cache(key: str, value: str, ttl: int = 300):
    get_cache_manager().set(key, value, ttl)
    return {"success": True}


@router.get("/get")
async def get_cache(key: str, default: str = None):
    return {"value": get_cache_manager().get(key, default)}


@router.post("/delete")
async def delete_cache(key: str):
    get_cache_manager().delete(key)
    return {"success": True}


@router.post("/clear")
async def clear_cache():
    get_cache_manager().clear()
    return {"success": True}