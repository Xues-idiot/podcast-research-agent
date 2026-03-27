"""第一个元素API"""

from fastapi import APIRouter

from echo.research.first_finder import get_first_finder


router = APIRouter(prefix="/api/first-finder", tags=["first-finder"])


@router.post("/first")
async def first(items: list):
    return {"result": get_first_finder().first(items)}