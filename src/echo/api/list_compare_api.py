"""列表比较API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_compare import list_compare, list_is_subsequence, list_starts_with, list_ends_with


class CompareRequest(BaseModel):
    list1: List[Any]
    list2: List[Any]


class SubsequenceRequest(BaseModel):
    sub: List[Any]
    main: List[Any]


class PrefixSuffixRequest(BaseModel):
    list: List[Any]
    prefix: List[Any]


class CompareResponse(BaseModel):
    equal: bool
    same_length: bool
    length_diff: int
    common: List[Any]
    only_in_first: List[Any]
    only_in_second: List[Any]


router = APIRouter(prefix="/api/list-compare", tags=["list"])


@router.post("/", response_model=CompareResponse)
async def compare_lists(request: CompareRequest) -> CompareResponse:
    result = list_compare(request.list1, request.list2)
    return CompareResponse(
        equal=result.equal,
        same_length=result.same_length,
        length_diff=result.length_diff,
        common=result.common,
        only_in_first=result.only_in_first,
        only_in_second=result.only_in_second
    )


@router.post("/subsequence")
async def is_subsequence(request: SubsequenceRequest) -> dict:
    result = list_is_subsequence(request.sub, request.main)
    return {"is_subsequence": result}


@router.post("/starts-with")
async def starts_with(request: PrefixSuffixRequest) -> dict:
    result = list_starts_with(request.list, request.prefix)
    return {"result": result}


@router.post("/ends-with")
async def ends_with(request: PrefixSuffixRequest) -> dict:
    result = list_ends_with(request.list, request.prefix)
    return {"result": result}

