"""所有检查API"""

from fastapi import APIRouter

from echo.research.all_tool import get_all_tool


router = APIRouter(prefix="/api/all", tags=["all"])


@router.post("/all-match")
async def all_match(items: list, predicate):
    return {"result": get_all_tool().all_match(items, predicate)}