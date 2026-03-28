"""数组工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.array_utils import array_unique, array_union, array_intersect, array_diff, array_chunk, array_flatten, array_zip, array_map, array_filter


class ArraysRequest(BaseModel):
    arrays: List[List[Any]]


class TwoArraysRequest(BaseModel):
    array1: List[Any]
    array2: List[Any]


class ChunkRequest(BaseModel):
    array: List[Any]
    size: int


router = APIRouter(prefix="/api/array", tags=["array"])


@router.post("/unique")
async def unique(request: ArraysRequest) -> dict:
    return {"result": array_unique(request.arrays[0]) if request.arrays else []}


@router.post("/union")
async def union(request: ArraysRequest) -> dict:
    return {"result": array_union(*request.arrays)}


@router.post("/intersect")
async def intersect(request: ArraysRequest) -> dict:
    return {"result": array_intersect(*request.arrays)}


@router.post("/diff")
async def diff(request: TwoArraysRequest) -> dict:
    return {"result": array_diff(request.array1, request.array2)}


@router.post("/chunk")
async def chunk(request: ChunkRequest) -> dict:
    return {"result": array_chunk(request.array, request.size)}


@router.post("/flatten")
async def flatten(request: ArraysRequest) -> dict:
    return {"result": array_flatten(request.arrays[0]) if request.arrays else []}


@router.post("/zip")
async def zip_arrays(request: ArraysRequest) -> dict:
    return {"result": array_zip(*request.arrays)}
