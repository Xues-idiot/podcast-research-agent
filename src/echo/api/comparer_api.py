"""比较API"""

from fastapi import APIRouter

from echo.research.comparer_tool import get_comparer_tool


router = APIRouter(prefix="/api/comparer", tags=["comparer"])


@router.post("/compare")
async def compare(a, b):
    return {"result": get_comparer_tool().compare(a, b)}