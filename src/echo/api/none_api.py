"""无匹配检查API"""

from fastapi import APIRouter

from echo.research.none_tool import get_none_tool


router = APIRouter(prefix="/api/none", tags=["none"])


@router.post("/none-match")
async def none_match(items: list, predicate):
    return {"result": get_none_tool().none_match(items, predicate)}