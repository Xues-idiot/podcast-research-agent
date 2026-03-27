"""反转API"""

from fastapi import APIRouter

from echo.research.reverser_tool import get_reverser_tool


router = APIRouter(prefix="/api/reverser", tags=["reverser"])


@router.post("/reverse")
async def reverse(items: list):
    return {"result": get_reverser_tool().reverse(items)}