"""更新API"""

from fastapi import APIRouter

from echo.research.update_list import get_update_list


router = APIRouter(prefix="/api/update", tags=["update"])


@router.post("/at")
async def update_at(items: list, index: int, item: str):
    """在指定位置更新"""
    tool = get_update_list()
    return {"items": tool.update(items, index, item)}


@router.post("/where")
async def update_where(items: list, pred: str, item: str):
    """按条件更新"""
    tool = get_update_list()
    pred_func = eval(pred)
    return {"items": tool.update_where(items, pred_func, item)}


@router.post("/replace")
async def replace_item(items: list, old: str, new: str):
    """替换元素"""
    tool = get_update_list()
    return {"items": tool.replace(items, old, new)}
