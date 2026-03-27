"""任意匹配API"""

from fastapi import APIRouter

from echo.research.any_of import get_any_of


router = APIRouter(prefix="/api/any-of", tags=["any-of"])


@router.post("/check")
async def check_any_of(items: list, pred: str = None):
    """检查是否有任意元素满足条件"""
    tool = get_any_of()
    if pred:
        pred_func = eval(pred)
        return {"result": tool.any_of(items, pred_func)}
    return {"result": tool.any_of(items)}
