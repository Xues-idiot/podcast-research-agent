"""搜索工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Callable

from echo.research.search_tool import get_search_tool


router = APIRouter(prefix="/api/search-tool", tags=["search-tool"])


class LinearSearchRequest(BaseModel):
    items: List[Any]
    target: Any


@router.post("/linear")
async def linear_search(request: LinearSearchRequest):
    tool = get_search_tool()
    return {"result": tool.linear_search(request.items, request.target)}


class BinarySearchRequest(BaseModel):
    items: List[Any]
    target: Any


@router.post("/binary")
async def binary_search(request: BinarySearchRequest):
    tool = get_search_tool()
    return {"result": tool.binary_search(request.items, request.target)}


class FindAllRequest(BaseModel):
    items: List[Any]
    predicate: Callable


@router.post("/find-all")
async def find_all(request: FindAllRequest):
    tool = get_search_tool()
    return {"result": tool.find_all(request.items, request.predicate)}


@router.post("/find-min")
async def find_min(request: LinearSearchRequest):
    tool = get_search_tool()
    return {"result": tool.find_min(request.items)}


@router.post("/find-max")
async def find_max(request: LinearSearchRequest):
    tool = get_search_tool()
    return {"result": tool.find_max(request.items)}