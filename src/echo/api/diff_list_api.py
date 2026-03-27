"""差集API"""

from fastapi import APIRouter

from echo.research.diff_list import get_diff_list


router = APIRouter(prefix="/api/diff", tags=["diff"])


@router.post("/difference")
async def difference(list1: list, list2: list):
    """计算差集"""
    tool = get_diff_list()
    return {"items": tool.difference(list1, list2)}


@router.post("/symmetric")
async def symmetric_difference(list1: list, list2: list):
    """计算对称差集"""
    tool = get_diff_list()
    return {"items": tool.symmetric_difference(list1, list2)}


@router.post("/by")
async def diff_by(list1: list, list2: list, key: str):
    """按键计算差集"""
    tool = get_diff_list()
    key_func = eval(key)
    return {"items": tool.diff_by(list1, list2, key_func)}
