"""百分比排名API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.percent_rank import get_percent_rank_tool


router = APIRouter(prefix="/api/percent-rank", tags=["percent-rank"])


class PercentileRequest(BaseModel):
    values: List[float]
    p: float


@router.post("/percentile")
async def percentile(request: PercentileRequest):
    tool = get_percent_rank_tool()
    return {"result": tool.percentile(request.values, request.p)}


class PercentileRankRequest(BaseModel):
    values: List[float]
    v: float


@router.post("/percentile-rank")
async def percentile_rank(request: PercentileRankRequest):
    tool = get_percent_rank_tool()
    return {"result": tool.percentile_rank(request.values, request.v)}


@router.post("/quartiles")
async def quartiles(request: PercentileRequest):
    tool = get_percent_rank_tool()
    q1, q2, q3 = tool.quartiles(request.values)
    return {"q1": q1, "q2": q2, "q3": q3}


@router.post("/iqr")
async def iqr(request: PercentileRequest):
    tool = get_percent_rank_tool()
    return {"result": tool.iqr(request.values)}