"""列表扁平化API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_flatten import (
    list_flatten,
    list_flatten_once,
    list_chunk_by_size,
    list_window
)


class FlattenRequest(BaseModel):
    """扁平化请求"""
    list: List[Any]
    depth: int = -1


class FlattenOnceRequest(BaseModel):
    """扁平化一层请求"""
    list: List[Any]


class ChunkRequest(BaseModel):
    """分块请求"""
    list: List[Any]
    chunk_size: int


class WindowRequest(BaseModel):
    """滑动窗口请求"""
    list: List[Any]
    window_size: int
    step: int = 1


class FlattenResponse(BaseModel):
    """扁平化响应"""
    items: List[Any]
    count: int
    depth: int


router = APIRouter(prefix="/api/list-flatten", tags=["list"])


@router.post("/", response_model=FlattenResponse)
async def flatten_list(request: FlattenRequest) -> FlattenResponse:
    """将嵌套列表扁平化"""
    result = list_flatten(request.list, request.depth)
    return FlattenResponse(
        items=result.items,
        count=result.count,
        depth=result.depth
    )


@router.post("/once")
async def flatten_once(request: FlattenOnceRequest) -> dict:
    """将嵌套列表扁平化一层"""
    result = list_flatten_once(request.list)
    return {"items": result, "count": len(result)}


@router.post("/chunk")
async def chunk_list(request: ChunkRequest) -> dict:
    """将列表分块"""
    try:
        result = list_chunk_by_size(request.list, request.chunk_size)
        return {"items": result, "count": len(result)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/window")
async def window_list(request: WindowRequest) -> dict:
    """创建滑动窗口"""
    try:
        result = list_window(request.list, request.window_size, request.step)
        return {"items": result, "count": len(result)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
