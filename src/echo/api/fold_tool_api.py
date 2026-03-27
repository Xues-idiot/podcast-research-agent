"""折叠工具API"""

from fastapi import APIRouter
from typing import Any, Callable

from echo.research.fold_tool import get_fold_tool


router = APIRouter(prefix="/api/fold", tags=["fold"])


@router.post("/reduce")
async def fold_items(items: list, func: str, initial: Any = None):
    """折叠/归约列表元素"""
    tool = get_fold_tool()
    func_obj = eval(func) if isinstance(func, str) else func
    return {"result": tool.fold(items, func_obj, initial)}
