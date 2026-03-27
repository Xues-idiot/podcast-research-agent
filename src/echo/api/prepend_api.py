"""前置API"""

from fastapi import APIRouter

from echo.research.prepend_tool import get_prepend_tool


router = APIRouter(prefix="/api/prepend", tags=["prepend"])


@router.post("/prepend")
async def prepend(items: list, item):
    return {"result": get_prepend_tool().prepend(items, item)}