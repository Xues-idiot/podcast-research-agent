"""任意全部无匹配API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Callable

from echo.research.any_all_none import get_any_all_none_tool


router = APIRouter(prefix="/api/any-all-none", tags=["any-all-none"])


class MatchRequest(BaseModel):
    items: List[Any]


@router.post("/any-match")
async def any_match(request: MatchRequest):
    tool = get_any_all_none_tool()
    return {"result": tool.any_match(request.items, lambda x: bool(x))}


@router.post("/all-match")
async def all_match(request: MatchRequest):
    tool = get_any_all_none_tool()
    return {"result": tool.all_match(request.items, lambda x: bool(x))}


@router.post("/none-match")
async def none_match(request: MatchRequest):
    tool = get_any_all_none_tool()
    return {"result": tool.none_match(request.items, lambda x: bool(x))}