"""过滤器API"""

from fastapi import APIRouter

from echo.research.filter_tool import get_filter_tool


router = APIRouter(prefix="/api/filter", tags=["filter"])


@router.post("/filter")
async def filter_items(items: list, predicate):
    return {"result": get_filter_tool().filter_items(items, predicate)}