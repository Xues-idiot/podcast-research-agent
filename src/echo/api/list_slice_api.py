"""列表切片API路由"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Any, List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_slice import list_slice, list_first_n, list_last_n, list_at_index


class SliceRequest(BaseModel):
    """切片请求"""
    list: List[Any]
    start: Optional[int] = None
    end: Optional[int] = None
    step: int = 1


class FirstNRequest(BaseModel):
    """前n个请求"""
    list: List[Any]
    n: int = 5


class LastNRequest(BaseModel):
    """后n个请求"""
    list: List[Any]
    n: int = 5


class AtIndexRequest(BaseModel):
    """指定索引请求"""
    list: List[Any]
    index: int
    default: Optional[Any] = None


class SliceResponse(BaseModel):
    """切片响应"""
    items: List[Any]
    count: int
    start: int
    end: int
    step: int


router = APIRouter(prefix="/api/list-slice", tags=["list"])


@router.post("/", response_model=SliceResponse)
async def slice_list(request: SliceRequest) -> SliceResponse:
    """获取列表切片"""
    try:
        result = list_slice(request.list, request.start, request.end, request.step)
        return SliceResponse(
            items=result.items,
            count=result.count,
            start=result.start,
            end=result.end,
            step=result.step
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/first")
async def first_n(request: FirstNRequest) -> SliceResponse:
    """获取前n个元素"""
    result = list_first_n(request.list, request.n)
    return SliceResponse(
        items=result.items,
        count=result.count,
        start=result.start,
        end=result.end,
        step=result.step
    )


@router.post("/last")
async def last_n(request: LastNRequest) -> SliceResponse:
    """获取后n个元素"""
    result = list_last_n(request.list, request.n)
    return SliceResponse(
        items=result.items,
        count=result.count,
        start=result.start,
        end=result.end,
        step=result.step
    )


@router.post("/at")
async def at_index(request: AtIndexRequest) -> dict:
    """获取指定索引元素"""
    result = list_at_index(request.list, request.index, request.default)
    return {
        "item": result,
        "index": request.index,
        "found": result is not None or request.default is not None
    }
