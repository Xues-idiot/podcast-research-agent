"""LRU缓存API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.cache import get_lru_cache


router = APIRouter(prefix="/api/lru-cache", tags=["lru-cache"])


class CacheRequest(BaseModel):
    key: str
    value: Any = None


@router.post("/get")
async def get(request: CacheRequest):
    return {"result": get_lru_cache().get(request.key)}


@router.post("/put")
async def put(request: CacheRequest):
    get_lru_cache().put(request.key, request.value)
    return {"success": True}
