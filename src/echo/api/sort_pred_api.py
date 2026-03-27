"""条件排序API"""

from fastapi import APIRouter

from echo.research.sort_pred import get_sort_pred


router = APIRouter(prefix="/api/sort", tags=["sort"])


@router.post("/by")
async def sort_by(items: list, key: str, reverse: bool = False):
    """按键排序"""
    tool = get_sort_pred()
    key_func = eval(key)
    return {"items": tool.sort_by(items, key_func, reverse)}


@router.post("/with")
async def sort_with(items: list, comp: str):
    """使用比较器排序"""
    tool = get_sort_pred()
    comp_func = eval(comp)
    return {"items": tool.sort_with(items, comp_func)}
