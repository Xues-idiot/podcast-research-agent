"""获取元素API"""

from fastapi import APIRouter

from echo.research.take_while import get_take_while


router = APIRouter(prefix="/api/take", tags=["take"])


@router.post("/while")
async def take_while(items: list, pred: str):
    """获取满足条件的元素"""
    tool = get_take_while()
    pred_func = eval(pred)
    return {"items": tool.take_while(items, pred_func)}


@router.post("/n")
async def take_n(items: list, n: int):
    """获取前n个元素"""
    tool = get_take_while()
    return {"items": tool.take(items, n)}
