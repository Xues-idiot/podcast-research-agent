"""Zip API"""

from fastapi import APIRouter

from echo.research.zip_with import get_zip_with


router = APIRouter(prefix="/api/zip", tags=["zip"])


@router.post("/with")
async def zip_with(list1: list, list2: list, func: str):
    """使用函数合并两个列表"""
    tool = get_zip_with()
    func_obj = eval(func)
    return {"result": tool.zip_with(list1, list2, func_obj)}


@router.post("/all")
async def zip_all(lists: list):
    """合并所有列表"""
    tool = get_zip_with()
    return {"result": tool.zip_all(*lists)}
