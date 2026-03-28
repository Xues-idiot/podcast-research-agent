"""列表排序API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List, Optional, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_sort import list_sort, list_reverse, list_shuffle, list_sort_by_length


class SortRequest(BaseModel):
    list: List[Any]
    reverse: bool = False
    key: Optional[str] = None


class SortResponse(BaseModel):
    items: List[Any]
    count: int
    reverse: bool


router = APIRouter(prefix="/api/list-sort", tags=["list"])


@router.post("/", response_model=SortResponse)
async def sort_list(request: SortRequest) -> SortResponse:
    key_fn = None
    if request.key:
        key_fn = lambda x: x.get(request.key) if isinstance(x, dict) else getattr(x, request.key, x)
    result = list_sort(request.list, request.reverse, key_fn)
    return SortResponse(items=result.items, count=result.count, reverse=result.reverse)


@router.post("/reverse")
async def reverse_list(request: BaseModel) -> dict:
    result = list_reverse(request.list)
    return {"items": result, "count": len(result)}


@router.post("/shuffle")
async def shuffle_list(request: BaseModel) -> dict:
    result = list_shuffle(request.list)
    return {"items": result, "count": len(result)}


@router.post("/by-length")
async def sort_by_length(request: SortRequest) -> SortResponse:
    result = list_sort_by_length(request.list, request.reverse)
    return SortResponse(items=result.items, count=result.count, reverse=result.reverse)

