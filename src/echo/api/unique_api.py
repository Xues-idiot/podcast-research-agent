"""唯一API"""

from fastapi import APIRouter

from echo.research.unique_tool import get_unique_tool


router = APIRouter(prefix="/api/unique", tags=["unique"])


@router.post("/unique")
async def unique(items: list):
    return {"result": get_unique_tool().unique(items)}