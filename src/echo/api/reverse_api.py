"""反转API"""

from fastapi import APIRouter

from echo.research.reverse_tool import get_reverse_tool


router = APIRouter(prefix="/api/reverse", tags=["reverse"])


@router.post("/reverse")
async def reverse(items: list):
    return {"result": get_reverse_tool().reverse(items)}