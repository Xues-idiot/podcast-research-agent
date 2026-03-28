"""压缩工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any, Tuple

from echo.research.zip_items import get_zip_items_tool


router = APIRouter(prefix="/api/zip-items", tags=["zip-items"])


class ZipListsRequest(BaseModel):
    lists: List[List[Any]]


@router.post("/zip")
async def zip_lists(request: ZipListsRequest):
    tool = get_zip_items_tool()
    return {"result": tool.zip_lists(*request.lists)}


class UnzipRequest(BaseModel):
    pairs: List[Tuple]


@router.post("/unzip")
async def unzip_pairs(request: UnzipRequest):
    tool = get_zip_items_tool()
    return {"result": tool.unzip_pairs(request.pairs)}


class ZipLongestRequest(BaseModel):
    lists: List[List[Any]]
    fillvalue: Any = None


@router.post("/zip-longest")
async def zip_longest_fill(request: ZipLongestRequest):
    tool = get_zip_items_tool()
    return {"result": tool.zip_longest_fill(*request.lists, fillvalue=request.fillvalue)}


@router.post("/to-dict")
async def dict_from_tuples(request: UnzipRequest):
    tool = get_zip_items_tool()
    return {"result": tool.dict_from_tuples(request.pairs)}