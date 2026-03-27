"""合并API"""

from fastapi import APIRouter

from echo.research.merge_list import get_merge_list


router = APIRouter(prefix="/api/merge", tags=["merge"])


@router.post("/lists")
async def merge_lists(list1: list, list2: list):
    """合并两个列表"""
    tool = get_merge_list()
    return {"items": tool.merge(list1, list2)}


@router.post("/by")
async def merge_by(list1: list, list2: list, key: str):
    """按键合并"""
    tool = get_merge_list()
    key_func = eval(key)
    return {"items": tool.merge_by(list1, list2, key_func)}
