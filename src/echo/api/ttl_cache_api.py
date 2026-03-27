"""TTL缓存API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.ttl_cache import get_ttl_cache


router = APIRouter(prefix="/api/ttl-cache", tags=["ttl-cache"])


class TTLRequest(BaseModel):
    key: str
    value: Any = None
    ttl: int = 300


@router.post("/get")
async def get(request: TTLRequest):
    return {"result": get_ttl_cache().get(request.key)}


@router.post("/put")
async def put(request: TTLRequest):
    get_ttl_cache().put(request.key, request.value, request.ttl)
    return {"success": True}
