"""列表统计API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List, Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_stats import list_stats, list_sum, list_mean, list_max, list_min


class StatsRequest(BaseModel):
    list: List[Any]


class StatsResponse(BaseModel):
    count: int
    sum: float
    mean: Optional[float]
    median: Optional[float]
    min: Optional[Any]
    max: Optional[Any]


router = APIRouter(prefix="/api/list-stats", tags=["list"])


@router.post("/", response_model=StatsResponse)
async def stats(request: StatsRequest) -> StatsResponse:
    result = list_stats(request.list)
    return StatsResponse(count=result.count, sum=result.sum, mean=result.mean, median=result.median, min=result.min, max=result.max)


@router.post("/sum")
async def sum_list(request: StatsRequest) -> dict:
    return {"sum": list_sum(request.list)}


@router.post("/mean")
async def mean_list(request: StatsRequest) -> dict:
    return {"mean": list_mean(request.list)}


@router.post("/max")
async def max_list(request: StatsRequest) -> dict:
    return {"max": list_max(request.list)}


@router.post("/min")
async def min_list(request: StatsRequest) -> dict:
    return {"min": list_min(request.list)}

