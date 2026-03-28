"""列表变换API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_transform import list_transform, list_accumulate, list_distinct, list_compact, list_flatten_deep


class TransformRequest(BaseModel):
    list: List[Any]
    transform_name: str = "double"


class AccumulateRequest(BaseModel):
    list: List[Any]
    func_name: str = "add"


class CompactRequest(BaseModel):
    list: List[Any]


class FlattenDeepRequest(BaseModel):
    list: List[Any]
    depth: int = -1


TRANSFORMS = {
    "double": lambda x: x * 2 if isinstance(x, (int, float)) else x,
    "square": lambda x: x ** 2 if isinstance(x, (int, float)) else x,
    "str": lambda x: str(x),
    "upper": lambda x: str(x).upper() if isinstance(x, str) else x,
    "lower": lambda x: str(x).lower() if isinstance(x, str) else x,
}

FUNCS = {
    "add": lambda a, b: a + b,
    "multiply": lambda a, b: a * b,
}


router = APIRouter(prefix="/api/list-transform", tags=["list"])


@router.post("/")
async def transform_list(request: TransformRequest) -> dict:
    transform = TRANSFORMS.get(request.transform_name, lambda x: x)
    result = list_transform(request.list, transform)
    return {"items": result.items, "count": result.count}


@router.post("/accumulate")
async def accumulate_list(request: AccumulateRequest) -> dict:
    func = FUNCS.get(request.func_name, lambda a, b: a + b)
    result = list_accumulate(request.list, func)
    return {"items": result, "count": len(result)}


@router.post("/distinct")
async def distinct_list(request: CompactRequest) -> dict:
    result = list_distinct(request.list)
    return {"items": result, "count": len(result)}


@router.post("/compact")
async def compact_list(request: CompactRequest) -> dict:
    result = list_compact(request.list)
    return {"items": result, "count": len(result)}


@router.post("/flatten")
async def flatten_deep(request: FlattenDeepRequest) -> dict:
    result = list_flatten_deep(request.list, request.depth)
    return {"items": result, "count": len(result)}

