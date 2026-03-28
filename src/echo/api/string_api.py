"""字符串处理API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.string_utils import str_reverse, str_upper, str_lower, str_title, str_capitalize, str_strip, str_split_lines, str_count, str_replace, str_contains


class StringRequest(BaseModel):
    value: str


class SplitLinesRequest(BaseModel):
    value: str


class ReplaceRequest(BaseModel):
    value: str
    old: str
    new: str


class ContainsRequest(BaseModel):
    value: str
    sub: str


router = APIRouter(prefix="/api/string", tags=["string"])


@router.post("/reverse")
async def reverse(request: StringRequest) -> dict:
    result = str_reverse(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/upper")
async def upper(request: StringRequest) -> dict:
    result = str_upper(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/lower")
async def lower(request: StringRequest) -> dict:
    result = str_lower(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/title")
async def title(request: StringRequest) -> dict:
    result = str_title(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/capitalize")
async def capitalize(request: StringRequest) -> dict:
    result = str_capitalize(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/strip")
async def strip(request: StringRequest) -> dict:
    result = str_strip(request.value)
    return {"result": result.result, "length": result.length}


@router.post("/split")
async def split_lines(request: SplitLinesRequest) -> dict:
    result = str_split_lines(request.value)
    return {"lines": result, "count": len(result)}


@router.post("/count")
async def count(request: ContainsRequest) -> dict:
    result = str_count(request.value, request.sub)
    return {"count": result}


@router.post("/replace")
async def replace(request: ReplaceRequest) -> dict:
    result = str_replace(request.value, request.old, request.new)
    return {"result": result.result, "length": result.length}


@router.post("/contains")
async def contains(request: ContainsRequest) -> dict:
    result = str_contains(request.value, request.sub)
    return {"contains": result}

