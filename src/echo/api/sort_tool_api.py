"""排序工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Callable

from echo.research.sort_tool import get_sort_tool


router = APIRouter(prefix="/api/sort-tool", tags=["sort-tool"])


class SortRequest(BaseModel):
    items: List[Any]
    reverse: bool = False


@router.post("/bubble-sort")
async def bubble_sort(request: SortRequest):
    tool = get_sort_tool()
    return {"result": tool.bubble_sort(request.items, reverse=request.reverse)}


@router.post("/quick-sort")
async def quick_sort(request: SortRequest):
    tool = get_sort_tool()
    return {"result": tool.quick_sort(request.items, reverse=request.reverse)}


@router.post("/insertion-sort")
async def insertion_sort(request: SortRequest):
    tool = get_sort_tool()
    return {"result": tool.insertion_sort(request.items, reverse=request.reverse)}


class SortByFieldRequest(BaseModel):
    items: List[dict]
    field: str
    reverse: bool = False


@router.post("/sorted-by")
async def sorted_by(request: SortByFieldRequest):
    tool = get_sort_tool()
    return {"result": tool.sorted_by(request.items, request.field, request.reverse)}