"""空值合并API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.coalesce_val import get_coalesce_tool


router = APIRouter(prefix="/api/coalesce", tags=["coalesce"])


@router.post("/coalesce")
async def coalesce(request: List[Any]):
    tool = get_coalesce_tool()
    return {"result": tool.coalesce(*request)}


class IfNoneRequest(BaseModel):
    value: Any
    default: Any


@router.post("/if-none")
async def if_none(request: IfNoneRequest):
    tool = get_coalesce_tool()
    return {"result": tool.if_none(request.value, request.default)}


class IfEmptyRequest(BaseModel):
    items: List[Any]
    default: Any


@router.post("/if-empty")
async def if_empty(request: IfEmptyRequest):
    tool = get_coalesce_tool()
    return {"result": tool.if_empty(request.items, request.default)}