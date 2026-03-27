"""Zip最长API"""

from fastapi import APIRouter

from echo.research.zip_longest_list import get_zip_longest


router = APIRouter(prefix="/api/zip-extend", tags=["zip-extend"])


@router.post("/lists")
async def zip_longest_lists(lists: list, fillvalue: str = None):
    """合并多个列表"""
    tool = get_zip_longest()
    return {"result": tool.zip_longest(*lists, fillvalue=fillvalue)}


@router.post("/with")
async def zip_longest_with(list1: list, list2: list, func: str, fillvalue: str = None):
    """使用函数合并"""
    tool = get_zip_longest()
    func_obj = eval(func)
    return {"result": tool.zip_longest_with(list1, list2, func_obj, fillvalue)}
