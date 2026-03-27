"""谓词分组API"""

from fastapi import APIRouter

from echo.research.group_pred import get_group_pred


router = APIRouter(prefix="/api/group-pred", tags=["group-pred"])


@router.post("/by")
async def group_by_pred(items: list, pred: str):
    """按谓词分组"""
    tool = get_group_pred()
    pred_func = eval(pred)
    return tool.group_by_pred(items, pred_func)


@router.post("/where")
async def group_where(items: list, pred: str):
    """筛选满足条件的元素"""
    tool = get_group_pred()
    pred_func = eval(pred)
    return {"items": tool.group_where(items, pred_func)}
