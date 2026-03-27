"""最小值API"""

from fastapi import APIRouter

from echo.research.min_tool import get_min_tool


router = APIRouter(prefix="/api/min", tags=["min"])


@router.post("/min")
async def min_value(items: list):
    return {"result": get_min_tool().min_value(items)}