"""循环生成API"""

from fastapi import APIRouter

from echo.research.cycle_gen import get_cycle_gen


router = APIRouter(prefix="/api/cycle-gen", tags=["cycle-gen"])


@router.post("/cycle")
async def cycle(items: list, count: int):
    """循环"""
    tool = get_cycle_gen()
    return {"result": tool.cycle(items, count)}
