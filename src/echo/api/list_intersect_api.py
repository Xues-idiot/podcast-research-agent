"""列表交集API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_intersect import list_intersect, list_intersect_by_key


class IntersectRequest(BaseModel):
    """交集请求"""
    lists: List[List[Any]]
    use_key: bool = False
    key: Optional[str] = None


class IntersectResponse(BaseModel):
    """交集响应"""
    intersection: List[Any]
    count: int
    from_count: int


router = APIRouter(prefix="/api/list-intersect", tags=["list"])


@router.post("/", response_model=IntersectResponse)
async def intersect_lists(request: IntersectRequest) -> IntersectResponse:
    """计算多个列表的交集"""
    if request.use_key and request.key:
        try:
            result = list_intersect_by_key(*request.lists, key=request.key)
            return IntersectResponse(
                intersection=result,
                count=len(result),
                from_count=len(request.lists)
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        try:
            result = list_intersect(*request.lists)
            return IntersectResponse(
                intersection=result.intersection,
                count=result.count,
                from_count=result.from_count
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def intersect_get(
    list1: str,
    list2: str,
    key: Optional[str] = None
) -> IntersectResponse:
    """GET方式计算两个列表的交集"""
    import ast

    try:
        list1_parsed = ast.literal_eval(list1)
        list2_parsed = ast.literal_eval(list2)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid list format")

    if not isinstance(list1_parsed, list) or not isinstance(list2_parsed, list):
        raise HTTPException(status_code=400, detail="Arguments must be lists")

    result = list_intersect(list1_parsed, list2_parsed)
    return IntersectResponse(
        intersection=result.intersection,
        count=result.count,
        from_count=result.from_count
    )
