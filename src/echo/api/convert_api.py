"""转换工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.convert_utils import str_to_int, str_to_float, str_to_bool, int_to_str, float_to_str, bool_to_str, list_to_str, str_to_list, dict_to_json, json_to_dict


class StrRequest(BaseModel):
    value: str


class ToIntRequest(BaseModel):
    value: str
    default: int = 0


class ToFloatRequest(BaseModel):
    value: str
    default: float = 0.0


class ListRequest(BaseModel):
    value: List


class ListToStrRequest(BaseModel):
    value: List
    separator: str = ","


class StrToListRequest(BaseModel):
    value: str
    separator: str = ","


router = APIRouter(prefix="/api/convert", tags=["convert"])


@router.post("/to-int")
async def to_int(request: ToIntRequest) -> dict:
    return {"result": str_to_int(request.value, request.default)}


@router.post("/to-float")
async def to_float(request: ToFloatRequest) -> dict:
    return {"result": str_to_float(request.value, request.default)}


@router.post("/to-bool")
async def to_bool(request: StrRequest) -> dict:
    return {"result": str_to_bool(request.value)}


@router.post("/int-to-str")
async def int_to_str(request: ToIntRequest) -> dict:
    return {"result": int_to_str(request.value)}


@router.post("/float-to-str")
async def float_to_str(request: ToFloatRequest) -> dict:
    return {"result": float_to_str(request.value)}


@router.post("/bool-to-str")
async def bool_to_str(request: StrRequest) -> dict:
    return {"result": bool_to_str(request.value)}


@router.post("/list-to-str")
async def list_to_str(request: ListToStrRequest) -> dict:
    return {"result": list_to_str(request.value, request.separator)}


@router.post("/str-to-list")
async def str_to_list(request: StrToListRequest) -> dict:
    return {"result": str_to_list(request.value, request.separator)}
