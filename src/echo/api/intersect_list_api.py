"""交集API"""

from fastapi import APIRouter

from echo.research.intersect_list import get_intersect_list


router = APIRouter(prefix="/api/intersect", tags=["intersect"])


@router.post("/items")
async def intersect_items(list1: list, list2: list):
    """计算交集"""
    tool = get_intersect_list()
    return {"items": tool.intersection(list1, list2)}


@router.post("/by")
async def intersect_by(list1: list, list2: list, key: str):
    """按键计算交集"""
    tool = get_intersect_list()
    key_func = eval(key)
    return {"items": tool.intersection_by(list1, list2, key_func)}
