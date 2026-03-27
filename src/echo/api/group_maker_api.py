"""分组工具API"""

from fastapi import APIRouter

from echo.research.group_maker import get_group_maker


router = APIRouter(prefix="/api/group-maker", tags=["group-maker"])


@router.post("/by-size")
async def group_by_size(items: list, size: int):
    return {"result": get_group_maker().group_by_size(items, size)}


@router.post("/by-key")
async def group_by_key(items: list, key: str):
    return {"result": get_group_maker().group_by_key(items, key)}