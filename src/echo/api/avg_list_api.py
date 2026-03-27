"""平均值API"""

from fastapi import APIRouter

from echo.research.avg_list import get_avg_list


router = APIRouter(prefix="/api/avg", tags=["avg"])


@router.post("/mean")
async def avg_mean(items: list):
    """计算平均值"""
    tool = get_avg_list()
    return {"avg": tool.avg(items)}


@router.post("/by")
async def avg_by(items: list, key: str):
    """按键计算平均值"""
    tool = get_avg_list()
    key_func = eval(key)
    return {"avg": tool.avg_by(items, key_func)}
