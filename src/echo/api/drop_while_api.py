"""跳过元素API"""

from fastapi import APIRouter

from echo.research.drop_while import get_drop_while


router = APIRouter(prefix="/api/drop", tags=["drop"])


@router.post("/while")
async def drop_while(items: list, pred: str):
    """跳过满足条件的元素"""
    tool = get_drop_while()
    pred_func = eval(pred)
    return {"items": tool.drop_while(items, pred_func)}


@router.post("/n")
async def drop_n(items: list, n: int):
    """跳过前n个元素"""
    tool = get_drop_while()
    return {"items": tool.drop(items, n)}
