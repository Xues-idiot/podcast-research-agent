"""计数器API"""

from fastapi import APIRouter

from echo.research.counter_tool import get_counter_tool


router = APIRouter(prefix="/api/counter-tool", tags=["counter-tool"])


@router.post("/count")
async def count(items: list):
    return {"result": get_counter_tool().count(items)}