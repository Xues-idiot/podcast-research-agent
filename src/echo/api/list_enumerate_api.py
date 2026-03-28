"""列表枚举API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_enumerate import list_enumerate, list_enumerate_dict, list_with_index


class EnumerateRequest(BaseModel):
    """枚举请求"""
    list: List[Any]
    start: int = 0
    step: int = 1


class EnumerateDictRequest(BaseModel):
    """字典枚举请求"""
    list: List[Any]
    index_key: str = "index"
    value_key: str = "value"
    start: int = 0
    step: int = 1


class AtIndexRequest(BaseModel):
    """获取索引元素请求"""
    list: List[Any]
    index: int
    default: Optional[Any] = None


class EnumerateResponse(BaseModel):
    """枚举响应"""
    items: List[tuple]
    count: int


router = APIRouter(prefix="/api/list-enumerate", tags=["list"])


@router.post("/", response_model=EnumerateResponse)
async def enumerate_list(request: EnumerateRequest) -> EnumerateResponse:
    """为列表添加索引"""
    try:
        result = list_enumerate(request.list, request.start, request.step)
        return EnumerateResponse(
            items=result.items,
            count=result.count
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/dict")
async def enumerate_dict(request: EnumerateDictRequest) -> dict:
    """为列表添加索引，返回字典"""
    try:
        result = list_enumerate_dict(
            request.list,
            request.index_key,
            request.value_key,
            request.start,
            request.step
        )
        return {"items": result, "count": len(result)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/at")
async def at_index(request: AtIndexRequest) -> dict:
    """获取指定索引的元素"""
    result = list_with_index(request.list, request.index, request.default)
    return {
        "item": result,
        "index": request.index,
        "found": result is not None or request.default is not None
    }
