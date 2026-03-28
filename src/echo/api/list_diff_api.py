"""列表差集API路由"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Any, List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from research.list_diff import list_diff, list_symmetric_diff


class DiffRequest(BaseModel):
    """差集请求"""
    lists: List[List[Any]]
    symmetric: bool = False


class DiffResponse(BaseModel):
    """差集响应"""
    difference: List[Any]
    count: int
    from_count: int


router = APIRouter(prefix="/api/list-diff", tags=["list"])


@router.post("/", response_model=DiffResponse)
async def diff_lists(request: DiffRequest) -> DiffResponse:
    """计算多个列表的差集"""
    if request.symmetric:
        if len(request.lists) != 2:
            raise HTTPException(status_code=400, detail="对称差集需要恰好两个列表")
        result = list_symmetric_diff(request.lists[0], request.lists[1])
    else:
        if len(request.lists) < 2:
            raise HTTPException(status_code=400, detail="差集需要至少两个列表")
        result = list_diff(*request.lists)

    return DiffResponse(
        difference=result.difference,
        count=result.count,
        from_count=result.from_count
    )


@router.get("/")
async def diff_get(
    list1: str = Query(..., description="第一个列表"),
    list2: str = Query(..., description="第二个列表"),
    symmetric: bool = Query(False, description="是否对称差集")
) -> DiffResponse:
    """GET方式计算列表差集"""
    import ast

    try:
        list1_parsed = ast.literal_eval(list1)
        list2_parsed = ast.literal_eval(list2)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid list format")

    if not isinstance(list1_parsed, list) or not isinstance(list2_parsed, list):
        raise HTTPException(status_code=400, detail="Arguments must be lists")

    if symmetric:
        result = list_symmetric_diff(list1_parsed, list2_parsed)
    else:
        result = list_diff(list1_parsed, list2_parsed)

    return DiffResponse(
        difference=result.difference,
        count=result.count,
        from_count=result.from_count
    )
