"""逻辑工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.logic_utils import is_none, is_not_none, is_empty, is_truthy, is_falsy, if_fn, coalesce, default_to


class ValueRequest(BaseModel):
    value: Any


class IfRequest(BaseModel):
    condition: bool
    true_val: Any
    false_val: Any


class CoalesceRequest(BaseModel):
    values: List[Any]


class DefaultToRequest(BaseModel):
    value: Any
    default: Any


router = APIRouter(prefix="/api/logic", tags=["logic"])


@router.post("/is-none")
async def is_none_endpoint(request: ValueRequest) -> dict:
    return {"result": is_none(request.value)}


@router.post("/is-not-none")
async def is_not_none_endpoint(request: ValueRequest) -> dict:
    return {"result": is_not_none(request.value)}


@router.post("/is-empty")
async def is_empty_endpoint(request: ValueRequest) -> dict:
    return {"result": is_empty(request.value)}


@router.post("/is-truthy")
async def is_truthy_endpoint(request: ValueRequest) -> dict:
    return {"result": is_truthy(request.value)}


@router.post("/is-falsy")
async def is_falsy_endpoint(request: ValueRequest) -> dict:
    return {"result": is_falsy(request.value)}


@router.post("/if")
async def if_endpoint(request: IfRequest) -> dict:
    return {"result": if_fn(request.condition, request.true_val, request.false_val)}


@router.post("/coalesce")
async def coalesce_endpoint(request: CoalesceRequest) -> dict:
    return {"result": coalesce(*request.values)}


@router.post("/default-to")
async def default_to_endpoint(request: DefaultToRequest) -> dict:
    return {"result": default_to(request.value, request.default)}
