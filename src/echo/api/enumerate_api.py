"""枚举API"""

from fastapi import APIRouter

from echo.research.enumerate_tool import get_enumerate_tool


router = APIRouter(prefix="/api/enumerate", tags=["enumerate"])


@router.post("/enumerate")
async def enumerate_items(items: list, start: int = 0):
    return {"result": get_enumerate_tool().enumerate_items(items, start)}