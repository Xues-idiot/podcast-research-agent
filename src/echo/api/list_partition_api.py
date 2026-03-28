"""列表分区API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_partition import list_partition, list_group_by, list_chunk_by_count, list_split_at


class PartitionRequest(BaseModel):
    list: List[Any]
    predicate_name: str = "truthy"


class GroupByRequest(BaseModel):
    list: List[Any]
    key_name: str = "identity"


class ChunkCountRequest(BaseModel):
    list: List[Any]
    chunk_count: int


class SplitAtRequest(BaseModel):
    list: List[Any]
    index: int


PREDICATES = {
    "truthy": lambda x: bool(x),
    "even": lambda x: isinstance(x, int) and x % 2 == 0,
    "odd": lambda x: isinstance(x, int) and x % 2 != 0,
    "positive": lambda x: isinstance(x, (int, float)) and x > 0,
    "negative": lambda x: isinstance(x, (int, float)) and x < 0,
    "zero": lambda x: x == 0,
}

KEYS = {
    "identity": lambda x: x,
    "type": lambda x: type(x).__name__,
    "first_char": lambda x: str(x)[0] if str(x) else "",
}


router = APIRouter(prefix="/api/list-partition", tags=["list"])


@router.post("/")
async def partition_list(request: PartitionRequest) -> dict:
    pred = PREDICATES.get(request.predicate_name, lambda x: bool(x))
    result = list_partition(request.list, pred)
    return {
        "matches": result.matches,
        "non_matches": result.non_matches,
        "match_count": result.match_count,
        "non_match_count": result.non_match_count
    }


@router.post("/group")
async def group_list(request: GroupByRequest) -> dict:
    key_fn = KEYS.get(request.key_name, lambda x: x)
    result = list_group_by(request.list, key_fn)
    return {"groups": result}


@router.post("/chunk")
async def chunk_list(request: ChunkCountRequest) -> dict:
    try:
        result = list_chunk_by_count(request.list, request.chunk_count)
        return {"chunks": result, "count": len(result)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/split")
async def split_list(request: SplitAtRequest) -> dict:
    before, after = list_split_at(request.list, request.index)
    return {"before": before, "after": after}

