"""偏函数API"""

from fastapi import APIRouter

from echo.research.functools_partial import get_functools_partial


router = APIRouter(prefix="/api/partial", tags=["partial"])


@router.post("/make")
async def make():
    return {"result": None}
