"""列表并集API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_union import list_union, list_union_by_key


class UnionRequest(BaseModel):
    """并集请求"""
    lists: List[List[Any]]
    use_key: bool = False
    key: Optional[str] = None


class UnionResponse(BaseModel):
    """并集响应"""
    union: List[Any]
    count: int
    from_count: int


router = APIRouter(prefix="/api/list-union", tags=["list"])


@router.post("/", response_model=UnionResponse)
async def union_lists(request: UnionRequest) -> UnionResponse:
    """计算多个列表的并集"""
    if request.use_key and request.key:
        try:
            result = list_union_by_key(*request.lists, key=request.key)
            return UnionResponse(
                union=result,
                count=len(result),
                from_count=len(request.lists)
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        try:
            result = list_union(*request.lists)
            return UnionResponse(
                union=result.union,
                count=result.count,
                from_count=result.from_count
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def union_get(
    list1: str,
    list2: str,
    key: Optional[str] = None
) -> UnionResponse:
    """GET方式计算两个列表的并集"""
    import ast

    try:
        list1_parsed = ast.literal_eval(list1)
        list2_parsed = ast.literal_eval(list2)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid list format")

    if not isinstance(list1_parsed, list) or not isinstance(list2_parsed, list):
        raise HTTPException(status_code=400, detail="Arguments must be lists")

    result = list_union(list1_parsed, list2_parsed)
    return UnionResponse(
        union=result.union,
        count=result.count,
        from_count=result.from_count
    )
