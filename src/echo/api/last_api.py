"""最后一个元素API"""

from fastapi import APIRouter

from echo.research.last_tool import get_last_tool


router = APIRouter(prefix="/api/last", tags=["last"])


@router.post("/last")
async def last(items: list):
    return {"result": get_last_tool().last(items)}