"""数学工具API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.math_utils import math_add, math_subtract, math_multiply, math_divide, math_power, math_sqrt, math_abs, math_floor, math_ceil, math_round, math_factorial, math_gcd, math_lcm


class TwoOperands(BaseModel):
    a: Union[int, float]
    b: Union[int, float]


class OneOperand(BaseModel):
    a: Union[int, float]


class FactorialRequest(BaseModel):
    n: int


class ManyOperands(BaseModel):
    nums: List[int]


router = APIRouter(prefix="/api/math", tags=["math"])


@router.post("/add")
async def add(request: TwoOperands) -> dict:
    return {"result": math_add(request.a, request.b)}


@router.post("/subtract")
async def subtract(request: TwoOperands) -> dict:
    return {"result": math_subtract(request.a, request.b)}


@router.post("/multiply")
async def multiply(request: TwoOperands) -> dict:
    return {"result": math_multiply(request.a, request.b)}


@router.post("/divide")
async def divide(request: TwoOperands) -> dict:
    result = math_divide(request.a, request.b)
    return {"result": result}


@router.post("/power")
async def power(request: TwoOperands) -> dict:
    return {"result": math_power(request.a, request.b)}


@router.post("/sqrt")
async def sqrt(request: OneOperand) -> dict:
    return {"result": math_sqrt(request.a)}


@router.post("/abs")
async def abs(request: OneOperand) -> dict:
    return {"result": math_abs(request.a)}


@router.post("/floor")
async def floor(request: OneOperand) -> dict:
    return {"result": math_floor(request.a)}


@router.post("/ceil")
async def ceil(request: OneOperand) -> dict:
    return {"result": math_ceil(request.a)}


@router.post("/round")
async def round(request: OneOperand) -> dict:
    return {"result": math_round(request.a)}


@router.post("/factorial")
async def factorial(request: FactorialRequest) -> dict:
    return {"result": math_factorial(request.n)}


@router.post("/gcd")
async def gcd(request: ManyOperands) -> dict:
    return {"result": math_gcd(*request.nums)}


@router.post("/lcm")
async def lcm(request: ManyOperands) -> dict:
    return {"result": math_lcm(*request.nums)}

