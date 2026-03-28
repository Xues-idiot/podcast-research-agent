"""比例计算API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.ratio_calc import get_ratio_calc_tool


router = APIRouter(prefix="/api/ratio-calc", tags=["ratio-calc"])


class RatioRequest(BaseModel):
    a: float
    b: float


@router.post("/ratio")
async def ratio(request: RatioRequest):
    tool = get_ratio_calc_tool()
    return {"result": tool.ratio(request.a, request.b)}


@router.post("/simplify")
async def simplify(request: RatioRequest):
    tool = get_ratio_calc_tool()
    simplified = tool.simplify_ratio(request.a, request.b)
    return {"result": {"a": simplified[0], "b": simplified[1]}}


class ProportionRequest(BaseModel):
    value: float
    total: float


@router.post("/proportion")
async def proportion(request: ProportionRequest):
    tool = get_ratio_calc_tool()
    return {"result": tool.proportion(request.value, request.total)}


class ScaleRequest(BaseModel):
    values: List[float]
    target_min: float
    target_max: float


@router.post("/scale")
async def scale(request: ScaleRequest):
    tool = get_ratio_calc_tool()
    return {"result": tool.scale_values(request.values, request.target_min, request.target_max)}