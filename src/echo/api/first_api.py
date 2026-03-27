"""第一个元素API"""

from fastapi import APIRouter

from echo.research.first_tool import get_first_tool


router = APIRouter(prefix="/api/first", tags=["first"])


@router.post("/first")
async def first(items: list):
    return {"result": get_first_tool().first(items)}