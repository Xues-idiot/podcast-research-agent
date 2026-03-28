"""累积和API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.cumulative_sum import get_cumulative_sum_tool


router = APIRouter(prefix="/api/cumulative-sum", tags=["cumulative-sum"])


class ValuesRequest(BaseModel):
    values: List[float]


@router.post("/cumsum")
async def cumsum(request: ValuesRequest):
    tool = get_cumulative_sum_tool()
    return {"result": tool.cumsum(request.values)}


@router.post("/cumprod")
async def cumprod(request: ValuesRequest):
    tool = get_cumulative_sum_tool()
    return {"result": tool.cumprod(request.values)}


@router.post("/diff")
async def diff(request: ValuesRequest):
    tool = get_cumulative_sum_tool()
    return {"result": tool.diff(request.values)}


@router.post("/normalize")
async def normalize(request: ValuesRequest):
    tool = get_cumulative_sum_tool()
    return {"result": tool.normalize(request.values)}