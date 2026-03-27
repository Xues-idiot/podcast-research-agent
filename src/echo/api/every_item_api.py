"""每个元素检查API"""

from fastapi import APIRouter

from echo.research.every_item import get_every_item


router = APIRouter(prefix="/api/every", tags=["every"])


@router.post("/check")
async def check_every(items: list, pred: str = None):
    """检查是否每个元素都满足条件"""
    tool = get_every_item()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.every(items, pred_func)}
    return {"result": tool.every(items)}
