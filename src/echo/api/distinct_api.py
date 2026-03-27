"""去重API"""

from fastapi import APIRouter

from echo.research.distinct_tool import get_distinct_tool


router = APIRouter(prefix="/api/distinct", tags=["distinct"])


@router.post("/distinct")
async def distinct(items: list):
    return {"result": get_distinct_tool().distinct(items)}