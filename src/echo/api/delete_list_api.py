"""删除API"""

from fastapi import APIRouter

from echo.research.delete_list import get_delete_list


router = APIRouter(prefix="/api/delete", tags=["delete"])


@router.post("/at")
async def delete_at(items: list, index: int):
    """删除指定位置元素"""
    tool = get_delete_list()
    return {"items": tool.delete(items, index)}


@router.post("/where")
async def delete_where(items: list, pred: str):
    """按条件删除"""
    tool = get_delete_list()
    pred_func = eval(pred)
    return {"items": tool.delete_where(items, pred_func)}


@router.post("/item")
async def remove_item(items: list, item: str):
    """删除元素"""
    tool = get_delete_list()
    return {"items": tool.remove(items, item)}
