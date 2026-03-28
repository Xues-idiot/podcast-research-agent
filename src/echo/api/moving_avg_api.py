"""移动平均API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.moving_avg import get_moving_avg_tool


router = APIRouter(prefix="/api/moving-avg", tags=["moving-avg"])


class MovingAvgRequest(BaseModel):
    values: List[float]
    window: int


@router.post("/simple")
async def simple_moving_avg(request: MovingAvgRequest):
    tool = get_moving_avg_tool()
    return {"result": tool.simple(request.values, request.window)}


@router.post("/weighted")
async def weighted_moving_avg(request: MovingAvgRequest):
    tool = get_moving_avg_tool()
    return {"result": tool.weighted(request.values, request.window)}


class ExpMovingAvgRequest(BaseModel):
    values: List[float]
    alpha: float = 0.3


@router.post("/exponential")
async def exponential_moving_avg(request: ExpMovingAvgRequest):
    tool = get_moving_avg_tool()
    return {"result": tool.exponential(request.values, request.alpha)}