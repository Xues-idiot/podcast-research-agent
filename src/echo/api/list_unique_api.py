"""列表去重API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_unique import list_unique, list_duplicates, list_is_unique


class UniqueRequest(BaseModel):
    list: List[Any]
    preserve_order: bool = True


class UniqueResponse(BaseModel):
    items: List[Any]
    count: int
    removed_count: int


router = APIRouter(prefix="/api/list-unique", tags=["list"])


@router.post("/", response_model=UniqueResponse)
async def unique_list(request: UniqueRequest) -> UniqueResponse:
    result = list_unique(request.list, request.preserve_order)
    return UniqueResponse(items=result.items, count=result.count, removed_count=result.removed_count)


@router.post("/duplicates")
async def duplicates(request: UniqueRequest) -> dict:
    result = list_duplicates(request.list)
    return {"items": result, "count": len(result)}


@router.post("/is-unique")
async def is_unique(request: UniqueRequest) -> dict:
    result = list_is_unique(request.list)
    return {"is_unique": result}

