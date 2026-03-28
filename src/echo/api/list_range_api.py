"""列表范围API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Union
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_range import list_range, list_range_inclusive, list_times, list_cycle


class RangeRequest(BaseModel):
    start: Union[int, float]
    stop: Union[int, float]
    step: Union[int, float] = 1


class TimesRequest(BaseModel):
    n: int
    func_name: str = "none"


class CycleRequest(BaseModel):
    list: Any
    n: int


class RangeResponse(BaseModel):
    items: list
    count: int


router = APIRouter(prefix="/api/list-range", tags=["list"])


@router.post("/")
async def range_list(request: RangeRequest) -> RangeResponse:
    try:
        result = list_range(request.start, request.stop, request.step)
        return RangeResponse(items=result.items, count=result.count)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/inclusive")
async def range_inclusive(request: RangeRequest) -> RangeResponse:
    try:
        result = list_range_inclusive(request.start, request.stop, request.step)
        return RangeResponse(items=result.items, count=result.count)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/times")
async def times_list(request: TimesRequest) -> dict:
    funcs = {
        "none": None,
        "double": lambda i: i * 2,
        "square": lambda i: i * i,
        "identity": lambda i: i,
    }
    func = funcs.get(request.func_name)
    result = list_times(request.n, func)
    return {"items": result, "count": len(result)}


@router.post("/cycle")
async def cycle_list(request: CycleRequest) -> dict:
    result = list_cycle(request.list, request.n)
    return {"items": result, "count": len(result)}

