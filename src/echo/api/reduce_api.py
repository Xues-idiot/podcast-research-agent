"""归约API"""

from fastapi import APIRouter

from echo.research.reduce_tool import get_reduce_tool


router = APIRouter(prefix="/api/reduce", tags=["reduce"])


@router.post("/reduce")
async def reduce_items(items: list, func, initial=None):
    return {"result": get_reduce_tool().reduce_items(items, func, initial)}