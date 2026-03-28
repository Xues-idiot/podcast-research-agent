"""字典工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, List, Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.dict_utils import dict_get, dict_set, dict_delete, dict_keys, dict_values, dict_items, dict_merge, dict_filter, dict_exclude, dict_invert, dict_flatten


class DictRequest(BaseModel):
    dict: Dict[str, Any]


class KeyRequest(BaseModel):
    dict: Dict[str, Any]
    key: str
    default: Optional[Any] = None


class SetRequest(BaseModel):
    dict: Dict[str, Any]
    key: str
    value: Any


class MergeRequest(BaseModel):
    dicts: List[Dict[str, Any]]


class FilterKeysRequest(BaseModel):
    dict: Dict[str, Any]
    keys: List[str]


class FlattenRequest(BaseModel):
    dict: Dict[str, Any]
    separator: str = "."


router = APIRouter(prefix="/api/dict", tags=["dict"])


@router.post("/get")
async def get(request: KeyRequest) -> dict:
    return {"value": dict_get(request.dict, request.key, request.default)}


@router.post("/set")
async def set(request: SetRequest) -> dict:
    return {"dict": dict_set(request.dict, request.key, request.value)}


@router.post("/delete")
async def delete(request: KeyRequest) -> dict:
    return {"dict": dict_delete(request.dict, request.key)}


@router.post("/keys")
async def keys(request: DictRequest) -> dict:
    return {"keys": dict_keys(request.dict)}


@router.post("/values")
async def values(request: DictRequest) -> dict:
    return {"values": dict_values(request.dict)}


@router.post("/items")
async def items(request: DictRequest) -> dict:
    return {"items": dict_items(request.dict)}


@router.post("/merge")
async def merge(request: MergeRequest) -> dict:
    return {"dict": dict_merge(*request.dicts)}


@router.post("/filter")
async def filter(request: FilterKeysRequest) -> dict:
    return {"dict": dict_filter(request.dict, request.keys)}


@router.post("/exclude")
async def exclude(request: FilterKeysRequest) -> dict:
    return {"dict": dict_exclude(request.dict, request.keys)}


@router.post("/invert")
async def invert(request: DictRequest) -> dict:
    return {"dict": dict_invert(request.dict)}


@router.post("/flatten")
async def flatten(request: FlattenRequest) -> dict:
    return {"dict": dict_flatten(request.dict, request.separator)}

