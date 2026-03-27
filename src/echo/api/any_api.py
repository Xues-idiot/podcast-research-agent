"""任意检查API"""

from fastapi import APIRouter

from echo.research.any_tool import get_any_tool


router = APIRouter(prefix="/api/any", tags=["any"])


@router.post("/any-match")
async def any_match(items: list, predicate):
    return {"result": get_any_tool().any_match(items, predicate)}