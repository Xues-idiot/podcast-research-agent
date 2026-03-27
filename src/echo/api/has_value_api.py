"""存在检查API"""

from fastapi import APIRouter
from typing import Callable

from echo.research.has_value import get_has_value


router = APIRouter(prefix="/api/has", tags=["has"])


@router.post("/value")
async def has_value(items: list, value: Any):
    """检查列表是否包含指定值"""
    tool = get_has_value()
    return {"result": tool.has(items, value)}


@router.post("/pred")
async def has_pred(items: list, pred: str):
    """检查列表是否有满足条件的元素"""
    tool = get_has_value()
    pred_func = eval(pred)
    return {"result": tool.has_pred(items, pred_func)}
