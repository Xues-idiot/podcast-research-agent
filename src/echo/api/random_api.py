"""随机工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.random_utils import random_int, random_float, random_choice, random_sample, random_string, random_uuid, random_bool, random_color, random_date


class IntRequest(BaseModel):
    min_val: int = 0
    max_val: int = 100


class FloatRequest(BaseModel):
    min_val: float = 0.0
    max_val: float = 1.0


class ChoiceRequest(BaseModel):
    choices: List


class SampleRequest(BaseModel):
    population: List
    n: int = 1


class StringRequest(BaseModel):
    length: int = 10
    charset: str = None


router = APIRouter(prefix="/api/random", tags=["random"])


@router.post("/int")
async def rand_int(request: IntRequest) -> dict:
    return {"result": random_int(request.min_val, request.max_val)}


@router.post("/float")
async def rand_float(request: FloatRequest) -> dict:
    return {"result": random_float(request.min_val, request.max_val)}


@router.post("/choice")
async def rand_choice(request: ChoiceRequest) -> dict:
    return {"result": random_choice(request.choices)}


@router.post("/sample")
async def rand_sample(request: SampleRequest) -> dict:
    return {"result": random_sample(request.population, request.n)}


@router.post("/string")
async def rand_string(request: StringRequest) -> dict:
    return {"result": random_string(request.length, request.charset)}


@router.post("/uuid")
async def rand_uuid() -> dict:
    return {"result": random_uuid()}


@router.post("/bool")
async def rand_bool() -> dict:
    return {"result": random_bool()}


@router.post("/color")
async def rand_color() -> dict:
    return {"result": random_color()}


@router.post("/date")
async def rand_date() -> dict:
    return {"result": random_date()}
