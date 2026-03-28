"""最小最大API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.min_max import get_min_max_tool


router = APIRouter(prefix="/api/min-max", tags=["min-max"])


class MinMaxRequest(BaseModel):
    items: List[Any]


@router.post("/min")
async def find_min(request: MinMaxRequest):
    tool = get_min_max_tool()
    return {"result": tool.find_min(request.items)}


@router.post("/max")
async def find_max(request: MinMaxRequest):
    tool = get_min_max_tool()
    return {"result": tool.find_max(request.items)}


@router.post("/min-max")
async def find_min_max(request: MinMaxRequest):
    tool = get_min_max_tool()
    min_val, max_val = tool.find_min_max(request.items)
    return {"min": min_val, "max": max_val}