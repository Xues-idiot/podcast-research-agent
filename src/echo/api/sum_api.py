"""求和API"""

from fastapi import APIRouter

from echo.research.sum_tool import get_sum_tool


router = APIRouter(prefix="/api/sum", tags=["sum"])


@router.post("/sum")
async def sum_values(items: list):
    return {"result": get_sum_tool().sum_values(items)}