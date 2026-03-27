"""首尾检查API"""

from fastapi import APIRouter

from echo.research.starts_ends import get_starts_ends


router = APIRouter(prefix="/api/starts-ends", tags=["starts-ends"])


@router.post("/starts-with")
async def starts_with(items: list, prefix: list):
    """检查是否以指定元素开头"""
    tool = get_starts_ends()
    return {"result": tool.starts_with(items, prefix)}


@router.post("/ends-with")
async def ends_with(items: list, suffix: list):
    """检查是否以指定元素结尾"""
    tool = get_starts_ends()
    return {"result": tool.ends_with(items, suffix)}


@router.post("/starts-with-pred")
async def starts_with_pred(items: list, pred: str):
    """按条件检查开头"""
    tool = get_starts_ends()
    pred_func = eval(pred)
    return {"result": tool.starts_with_pred(items, pred_func)}


@router.post("/ends-with-pred")
async def ends_with_pred(items: list, pred: str):
    """按条件检查结尾"""
    tool = get_starts_ends()
    pred_func = eval(pred)
    return {"result": tool.ends_with_pred(items, pred_func)}
