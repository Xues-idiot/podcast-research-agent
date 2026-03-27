"""对象池API"""

from fastapi import APIRouter

from echo.research.object_pool_tool import get_object_pool


router = APIRouter(prefix="/api/object-pool", tags=["object-pool"])


@router.post("/acquire")
async def acquire():
    return {"result": get_object_pool().acquire()}


@router.post("/release")
async def release(obj):
    get_object_pool().release(obj)
    return {"success": True}