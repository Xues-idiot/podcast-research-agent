"""计数API"""

from fastapi import APIRouter

from echo.research.count_tool import get_count_tool


router = APIRouter(prefix="/api/count", tags=["count"])


@router.post("/count")
async def count(items: list):
    return {"result": get_count_tool().count(items)}