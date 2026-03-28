"""分组工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Callable, Dict

from echo.research.group_tool import get_group_tool


router = APIRouter(prefix="/api/group-tool", tags=["group-tool"])


class GroupByRequest(BaseModel):
    items: List[Any]
    key: Callable


@router.post("/group-by")
async def group_by(request: GroupByRequest):
    tool = get_group_tool()
    return {"result": tool.group_by(request.items, request.key)}


class GroupByFieldRequest(BaseModel):
    items: List[dict]
    field: str


@router.post("/group-by-field")
async def group_by_field(request: GroupByFieldRequest):
    tool = get_group_tool()
    return {"result": tool.group_by_field(request.items, request.field)}


class ChunkRequest(BaseModel):
    items: List[Any]
    size: int


@router.post("/chunk")
async def chunk(request: ChunkRequest):
    tool = get_group_tool()
    return {"result": tool.chunk(request.items, request.size)}


class WindowRequest(BaseModel):
    items: List[Any]
    size: int
    step: int = 1


@router.post("/window")
async def window(request: WindowRequest):
    tool = get_group_tool()
    return {"result": tool.window(request.items, request.size, request.step)}


class PartitionRequest(BaseModel):
    items: List[Any]
    predicate: Callable


@router.post("/partition")
async def partition(request: PartitionRequest):
    tool = get_group_tool()
    matched, not_matched = tool.partition(request.items, request.predicate)
    return {"matched": matched, "not_matched": not_matched}