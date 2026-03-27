"""并集API"""

from fastapi import APIRouter

from echo.research.union_list import get_union_list


router = APIRouter(prefix="/api/union", tags=["union"])


@router.post("/items")
async def union_items(lists: list):
    """计算并集"""
    tool = get_union_list()
    return {"items": tool.union(*lists)}


@router.post("/by")
async def union_by(lists: list, key: str):
    """按键计算并集"""
    tool = get_union_list()
    key_func = eval(key)
    return {"items": tool.union_by(*lists, key=key_func)}
