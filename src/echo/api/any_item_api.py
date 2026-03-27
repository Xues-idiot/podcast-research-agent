"""任意元素检查API"""

from fastapi import APIRouter

from echo.research.any_item import get_any_item


router = APIRouter(prefix="/api/any-item", tags=["any-item"])


@router.post("/check")
async def check_any_item(items: list, pred: str = None):
    """检查是否有任意元素满足条件"""
    tool = get_any_item()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.any(items, pred_func)}
    return {"result": tool.any(items)}
