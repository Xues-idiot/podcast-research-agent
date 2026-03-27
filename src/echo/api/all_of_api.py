"""全部匹配API"""

from fastapi import APIRouter

from echo.research.all_of import get_all_of


router = APIRouter(prefix="/api/all-of", tags=["all-of"])


@router.post("/check")
async def check_all_of(items: list, pred: str = None):
    """检查是否所有元素都满足条件"""
    tool = get_all_of()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.all_of(items, pred_func)}
    return {"result": tool.all_of(items)}
