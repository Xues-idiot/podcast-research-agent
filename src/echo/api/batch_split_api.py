"""批处理分割API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Callable

from echo.research.batch_split import get_batch_split_tool


router = APIRouter(prefix="/api/batch-split", tags=["batch-split"])


class SplitBySizeRequest(BaseModel):
    items: List[Any]
    size: int


@router.post("/by-size")
async def split_by_size(request: SplitBySizeRequest):
    tool = get_batch_split_tool()
    return {"result": tool.split_by_size(request.items, request.size)}


class SplitByCountRequest(BaseModel):
    items: List[Any]
    count: int


@router.post("/by-count")
async def split_by_count(request: SplitByCountRequest):
    tool = get_batch_split_tool()
    return {"result": tool.split_by_count(request.items, request.count)}


class SplitAtIndexRequest(BaseModel):
    items: List[Any]
    index: int


@router.post("/at-index")
async def split_at_index(request: SplitAtIndexRequest):
    tool = get_batch_split_tool()
    matched, not_matched = tool.split_at_index(request.items, request.index)
    return {"matched": matched, "not_matched": not_matched}