"""相等性API"""

from fastapi import APIRouter

from echo.research.equality_tool import get_equality_tool


router = APIRouter(prefix="/api/equality", tags=["equality"])


@router.post("/equals")
async def equals(a, b):
    return {"result": get_equality_tool().equals(a, b)}


@router.post("/not-equals")
async def not_equals(a, b):
    return {"result": get_equality_tool().not_equals(a, b)}