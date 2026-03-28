"""列表批处理API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Callable
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.list_batch import list_map, list_filter


class MapRequest(BaseModel):
    list: List[Any]
    func_name: str = "identity"


class FilterRequest(BaseModel):
    list: List[Any]
    predicate_name: str = "truthy"


FUNCS = {
    "identity": lambda x: x,
    "upper": lambda x: str(x).upper(),
    "lower": lambda x: str(x).lower(),
    "len": lambda x: len(x),
    "str": lambda x: str(x),
    "int": lambda x: int(x) if str(x).isdigit() else x,
    "double": lambda x: x * 2 if isinstance(x, (int, float)) else x,
}

PREDICATES = {
    "truthy": lambda x: bool(x),
    "non_empty": lambda x: bool(x) and (isinstance(x, str) and len(x) > 0 or isinstance(x, (list, dict))),
    "positive": lambda x: isinstance(x, (int, float)) and x > 0,
    "even": lambda x: isinstance(x, int) and x % 2 == 0,
}


router = APIRouter(prefix="/api/list-batch", tags=["list"])


@router.post("/map")
async def map_list(request: MapRequest) -> dict:
    func = FUNCS.get(request.func_name, lambda x: x)
    result = list_map(request.list, func)
    return {"items": result, "count": len(result)}


@router.post("/filter")
async def filter_list(request: FilterRequest) -> dict:
    pred = PREDICATES.get(request.predicate_name, lambda x: bool(x))
    result = list_filter(request.list, pred)
    return {"items": result, "count": len(result)}

