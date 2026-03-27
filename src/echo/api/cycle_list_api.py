"""循环API"""

from fastapi import APIRouter

from echo.research.cycle_list import get_cycle_list


router = APIRouter(prefix="/api/cycle", tags=["cycle"])


@router.post("/times")
async def cycle_times(items: list, n: int = None):
    """循环n次"""
    tool = get_cycle_list()
    return {"items": tool.cycle(items, n)}
