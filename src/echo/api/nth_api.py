"""第N个元素API"""

from fastapi import APIRouter

from echo.research.nth_tool import get_nth_tool


router = APIRouter(prefix="/api/nth", tags=["nth"])


@router.post("/nth")
async def nth(items: list, n: int):
    return {"result": get_nth_tool().nth(items, n)}