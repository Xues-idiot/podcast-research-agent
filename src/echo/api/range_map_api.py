"""范围映射API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.range_map import get_range_map_tool


router = APIRouter(prefix="/api/range-map", tags=["range-map"])


class MapValueRequest(BaseModel):
    value: float
    in_min: float
    in_max: float
    out_min: float
    out_max: float


@router.post("/map-value")
async def map_value(request: MapValueRequest):
    tool = get_range_map_tool()
    return {"result": tool.map_value(request.value, request.in_min, request.in_max, request.out_min, request.out_max)}


class MapRangeRequest(BaseModel):
    values: List[float]
    in_min: float
    in_max: float
    out_min: float
    out_max: float


@router.post("/map-range")
async def map_range(request: MapRangeRequest):
    tool = get_range_map_tool()
    return {"result": tool.map_range(request.values, request.in_min, request.in_max, request.out_min, request.out_max)}


class ClampRequest(BaseModel):
    value: float
    min_val: float
    max_val: float


@router.post("/clamp")
async def clamp(request: ClampRequest):
    tool = get_range_map_tool()
    return {"result": tool.clamp(request.value, request.min_val, request.max_val)}


class WrapRequest(BaseModel):
    value: float
    min_val: float
    max_val: float


@router.post("/wrap")
async def wrap(request: WrapRequest):
    tool = get_range_map_tool()
    return {"result": tool.wrap(request.value, request.min_val, request.max_val)}