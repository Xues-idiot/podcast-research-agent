"""集合工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List, Set
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.collection_utils import set_union, set_intersect, set_diff, set_sym_diff, set_is_subset, set_to_list


class SetsRequest(BaseModel):
    sets: List[Set[Any]]


class TwoSetsRequest(BaseModel):
    set1: Set[Any]
    set2: Set[Any]


router = APIRouter(prefix="/api/collection", tags=["collection"])


@router.post("/union")
async def union(request: SetsRequest) -> dict:
    return {"result": list(set_union(*[set(x) for x in request.sets]))}


@router.post("/intersect")
async def intersect(request: SetsRequest) -> dict:
    return {"result": list(set_intersect(*[set(x) for x in request.sets]))}


@router.post("/diff")
async def diff(request: TwoSetsRequest) -> dict:
    return {"result": list(set_diff(set(request.set1), set(request.set2)))}


@router.post("/sym-diff")
async def sym_diff(request: TwoSetsRequest) -> dict:
    return {"result": list(set_sym_diff(set(request.set1), set(request.set2)))}


@router.post("/is-subset")
async def is_subset(request: TwoSetsRequest) -> dict:
    return {"result": set_is_subset(set(request.set1), set(request.set2))}


@router.post("/to-list")
async def to_list(request: SetsRequest) -> dict:
    return {"result": set_to_list(set(request.sets[0])) if request.sets else []}
