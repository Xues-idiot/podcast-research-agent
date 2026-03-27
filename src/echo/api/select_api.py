"""选择API"""

from fastapi import APIRouter

from echo.research.select_tool import get_select_tool


router = APIRouter(prefix="/api/select", tags=["select"])


@router.post("/select")
async def select(items: list, indices: list):
    return {"result": get_select_tool().select(items, indices)}