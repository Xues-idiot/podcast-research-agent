"""列表查找API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_find import list_find, list_find_all, list_contains, list_index_of, list_count


class FindRequest(BaseModel):
    list: List[Any]
    value: Optional[Any] = None


class FindResponse(BaseModel):
    found: bool
    index: Optional[int]
    item: Optional[Any]


router = APIRouter(prefix="/api/list-find", tags=["list"])


@router.post("/", response_model=FindResponse)
async def find_item(request: FindRequest) -> FindResponse:
    result = list_find(request.list, value=request.value)
    return FindResponse(found=result.found, index=result.index, item=result.item)


@router.post("/all")
async def find_all(request: FindRequest) -> dict:
    result = list_find_all(request.list, value=request.value)
    return {"items": result, "count": len(result)}


@router.post("/contains")
async def contains(request: FindRequest) -> dict:
    result = list_contains(request.list, request.value)
    return {"contains": result}


@router.post("/index-of")
async def index_of(request: FindRequest) -> dict:
    result = list_index_of(request.list, request.value)
    return {"index": result}


@router.post("/count")
async def count(request: FindRequest) -> dict:
    result = list_count(request.list, request.value)
    return {"count": result}

