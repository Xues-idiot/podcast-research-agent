"""偏函数API"""

from fastapi import APIRouter

from echo.research.partial_tool import get_partial_tool


router = APIRouter(prefix="/api/partial", tags=["partial"])


@router.post("/partial")
async def partial(func, *args, **kwargs):
    return {"result": get_partial_tool().partial(func, *args, **kwargs)}