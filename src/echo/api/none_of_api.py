"""无匹配API"""

from fastapi import APIRouter

from echo.research.none_of import get_none_of


router = APIRouter(prefix="/api/none-of", tags=["none-of"])


@router.post("/check")
async def check_none_of(items: list, pred: str = None):
    """检查是否没有元素满足条件"""
    tool = get_none_of()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.none_of(items, pred_func)}
    return {"result": tool.none_of(items)}
