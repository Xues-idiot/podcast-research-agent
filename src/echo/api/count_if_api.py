"""条件计数API"""

from fastapi import APIRouter

from echo.research.count_if import get_count_if


router = APIRouter(prefix="/api/count-if", tags=["count-if"])


@router.post("/count")
async def count_if(items: list, pred: str):
    """统计满足条件的元素数量"""
    tool = get_count_if()
    pred_func = eval(pred)
    return {"count": tool.count_if(items, pred_func)}
