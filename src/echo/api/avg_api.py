"""平均值API"""

from fastapi import APIRouter

from echo.research.avg_tool import get_avg_tool


router = APIRouter(prefix="/api/avg", tags=["avg"])


@router.post("/average")
async def average(items: list):
    return {"result": get_avg_tool().average(items)}