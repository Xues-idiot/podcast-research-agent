"""平均值API"""

from fastapi import APIRouter

from echo.research.averager_tool import get_averager_tool


router = APIRouter(prefix="/api/averager-tool", tags=["averager-tool"])


@router.post("/average")
async def average(items: list):
    return {"result": get_averager_tool().average(items)}