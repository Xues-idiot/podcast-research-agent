"""列表合并API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional, Tuple
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_zip import list_zip, list_concat, list_interleave, list_zip_dict


class ZipRequest(BaseModel):
    lists: List[List[Any]]
    fillvalue: Optional[Any] = None


class ConcatRequest(BaseModel):
    lists: List[List[Any]]


class InterleaveRequest(BaseModel):
    lists: List[List[Any]]


class ZipDictRequest(BaseModel):
    keys: List[Any]
    values: List[Any]


class ZipResponse(BaseModel):
    items: List[tuple]
    count: int


router = APIRouter(prefix="/api/list-zip", tags=["list"])


@router.post("/", response_model=ZipResponse)
async def zip_lists(request: ZipRequest) -> ZipResponse:
    result = list_zip(*request.lists, fillvalue=request.fillvalue)
    return ZipResponse(items=result.items, count=result.count)


@router.post("/concat")
async def concat_lists(request: ConcatRequest) -> dict:
    result = list_concat(*request.lists)
    return {"items": result, "count": len(result)}


@router.post("/interleave")
async def interleave_lists(request: InterleaveRequest) -> dict:
    result = list_interleave(*request.lists)
    return {"items": result, "count": len(result)}


@router.post("/dict")
async def zip_dict(request: ZipDictRequest) -> dict:
    result = list_zip_dict(request.keys, request.values)
    return {"dict": result}

