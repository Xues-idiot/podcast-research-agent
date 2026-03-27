"""包含检查API"""

from fastapi import APIRouter

from echo.research.contains_list import get_contains_list


router = APIRouter(prefix="/api/contains", tags=["contains"])


@router.post("/item")
async def contains_item(items: list, item: str):
    """检查是否包含元素"""
    tool = get_contains_list()
    return {"contains": tool.contains(items, item)}


@router.post("/any")
async def contains_any(items: list, targets: list):
    """检查是否包含任一元素"""
    tool = get_contains_list()
    return {"contains": tool.contains_any(items, targets)}


@router.post("/all")
async def contains_all(items: list, targets: list):
    """检查是否包含所有元素"""
    tool = get_contains_list()
    return {"contains": tool.contains_all(items, targets)}


@router.post("/pred")
async def contains_pred(items: list, pred: str):
    """按条件检查包含"""
    tool = get_contains_list()
    pred_func = eval(pred)
    return {"contains": tool.contains_pred(items, pred_func)}
