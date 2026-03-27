"""按键最小最大API"""

from fastapi import APIRouter

from echo.research.min_by import get_min_by


router = APIRouter(prefix="/api/min-max", tags=["min-max"])


@router.post("/min-by")
async def min_by(items: list, key: str):
    """获取最小元素"""
    tool = get_min_by()
    key_func = eval(key)
    return {"item": tool.min_by(items, key_func)}


@router.post("/max-by")
async def max_by(items: list, key: str):
    """获取最大元素"""
    tool = get_min_by()
    key_func = eval(key)
    return {"item": tool.max_by(items, key_func)}


@router.post("/min-max-by")
async def min_max_by(items: list, key: str):
    """获取最小和最大元素"""
    tool = get_min_by()
    key_func = eval(key)
    min_item, max_item = tool.min_max_by(items, key_func)
    return {"min": min_item, "max": max_item}
