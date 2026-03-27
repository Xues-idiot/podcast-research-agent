"""无元素检查API"""

from fastapi import APIRouter

from echo.research.no_item import get_no_item


router = APIRouter(prefix="/api/no-item", tags=["no-item"])


@router.post("/check")
async def check_no_item(items: list, pred: str = None):
    """检查是否没有元素满足条件"""
    tool = get_no_item()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.none(items, pred_func)}
    return {"result": tool.none(items)}
