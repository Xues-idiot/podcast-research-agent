"""按键去重API"""

from fastapi import APIRouter

from echo.research.unique_by import get_unique_by


router = APIRouter(prefix="/api/unique", tags=["unique"])


@router.post("/by")
async def unique_by(items: list, key: str):
    """按键去重"""
    tool = get_unique_by()
    key_func = eval(key)
    return {"items": tool.unique_by(items, key_func)}


@router.post("/distinct")
async def distinct(items: list):
    """简单去重"""
    tool = get_unique_by()
    return {"items": tool.distinct(items)}
