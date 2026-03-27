"""最大值API"""

from fastapi import APIRouter

from echo.research.max_tool import get_max_tool


router = APIRouter(prefix="/api/max", tags=["max"])


@router.post("/max")
async def max_value(items: list):
    return {"result": get_max_tool().max_value(items)}