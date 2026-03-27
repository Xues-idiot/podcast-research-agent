"""最小最大API"""

from fastapi import APIRouter

from echo.research.min_max_list import get_min_max_list


router = APIRouter(prefix="/api/min-max", tags=["min-max"])


@router.post("/min")
async def min_item(items: list):
    """获取最小值"""
    tool = get_min_max_list()
    return {"min": tool.min(items)}


@router.post("/max")
async def max_item(items: list):
    """获取最大值"""
    tool = get_min_max_list()
    return {"max": tool.max(items)}


@router.post("/both")
async def min_max_items(items: list):
    """获取最小和最大值"""
    tool = get_min_max_list()
    min_val, max_val = tool.min_max(items)
    return {"min": min_val, "max": max_val}


@router.post("/min-by")
async def min_by_item(items: list, key: str):
    """按键获取最小值"""
    tool = get_min_max_list()
    key_func = eval(key)
    return {"min": tool.min_by(items, key_func)}


@router.post("/max-by")
async def max_by_item(items: list, key: str):
    """按键获取最大值"""
    tool = get_min_max_list()
    key_func = eval(key)
    return {"max": tool.max_by(items, key_func)}
