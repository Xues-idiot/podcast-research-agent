"""比较工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.compare_utils import compare, min_val, max_val, clamp, between, equal, greater_than, less_than


class TwoValues(BaseModel):
    a: Any
    b: Any


class ThreeValues(BaseModel):
    value: Any
    min_val: Any
    max_val: Any


class ManyValues(BaseModel):
    values: List[Any]


router = APIRouter(prefix="/api/compare", tags=["compare"])


@router.post("/min")
async def min_endpoint(request: ManyValues) -> dict:
    return {"result": min_val(*request.values)}


@router.post("/max")
async def max_endpoint(request: ManyValues) -> dict:
    return {"result": max_val(*request.values)}


@router.post("/clamp")
async def clamp_endpoint(request: ThreeValues) -> dict:
    return {"result": clamp(request.value, request.min_val, request.max_val)}


@router.post("/between")
async def between_endpoint(request: ThreeValues) -> dict:
    return {"result": between(request.value, request.min_val, request.max_val)}


@router.post("/equal")
async def equal_endpoint(request: TwoValues) -> dict:
    return {"result": equal(request.a, request.b)}


@router.post("/greater-than")
async def greater_than_endpoint(request: TwoValues) -> dict:
    return {"result": greater_than(request.a, request.b)}


@router.post("/less-than")
async def less_than_endpoint(request: TwoValues) -> dict:
    return {"result": less_than(request.a, request.b)}
