"""最后一个元素API"""

from fastapi import APIRouter

from echo.research.last_finder import get_last_finder


router = APIRouter(prefix="/api/last-finder", tags=["last-finder"])


@router.post("/last")
async def last(items: list):
    return {"result": get_last_finder().last(items)}