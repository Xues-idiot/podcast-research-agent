"""交叉合并列表API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.interleave_lists import get_interleave_lists_tool


router = APIRouter(prefix="/api/interleave-lists", tags=["interleave-lists"])


class InterleaveRequest(BaseModel):
    lists: List[List[Any]]


@router.post("/interleave")
async def interleave(request: InterleaveRequest):
    tool = get_interleave_lists_tool()
    return {"result": tool.interleave(*request.lists)}


@router.post("/round-robin")
async def round_robin(request: InterleaveRequest):
    tool = get_interleave_lists_tool()
    return {"result": tool.round_robin(*request.lists)}


class IntersperseRequest(BaseModel):
    items: List[Any]
    value: Any


@router.post("/intersperse")
async def intersperse(request: IntersperseRequest):
    tool = get_interleave_lists_tool()
    return {"result": tool.intersperse(request.items, request.value)}