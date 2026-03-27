"""选择API"""

from fastapi import APIRouter

from echo.research.select_list import get_select_list


router = APIRouter(prefix="/api/select", tags=["select"])


@router.post("/indices")
async def select_by_indices(items: list, indices: list):
    """按索引选择"""
    tool = get_select_list()
    return {"items": tool.select(items, indices)}


@router.post("/where")
async def select_where(items: list, pred: str):
    """按条件选择"""
    tool = get_select_list()
    pred_func = eval(pred)
    return {"items": tool.select_where(items, pred_func)}
