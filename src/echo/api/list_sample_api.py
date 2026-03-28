"""列表采样API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_sample import list_sample, list_shuffle_sample, list_random_item, list_random_pair


class SampleRequest(BaseModel):
    list: List[Any]
    n: int = 1
    replace: bool = False


class FractionRequest(BaseModel):
    list: List[Any]
    fraction: float = 0.1


router = APIRouter(prefix="/api/list-sample", tags=["list"])


@router.post("/")
async def sample_list(request: SampleRequest) -> dict:
    result = list_sample(request.list, request.n, request.replace)
    return {"items": result, "count": len(result)}


@router.post("/fraction")
async def sample_fraction(request: FractionRequest) -> dict:
    result = list_shuffle_sample(request.list, request.fraction)
    return {"items": result, "count": len(result)}


@router.post("/random")
async def random_item(request: SampleRequest) -> dict:
    result = list_random_item(request.list)
    return {"item": result}


@router.post("/pair")
async def random_pair(request: SampleRequest) -> dict:
    result = list_random_pair(request.list)
    return {"items": result, "count": len(result)}

