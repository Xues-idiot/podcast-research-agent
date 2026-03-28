"""列表拼接API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.list_append import get_list_append_tool


router = APIRouter(prefix="/api/list-append", tags=["list-append"])


class AddItemRequest(BaseModel):
    items: List[Any]
    item: Any


@router.post("/add-item")
async def add_item(request: AddItemRequest):
    tool = get_list_append_tool()
    return {"result": tool.add_item(request.items, request.item)}


class AddItemsRequest(BaseModel):
    items: List[Any]
    new_items: List[Any]


@router.post("/add-items")
async def add_items(request: AddItemsRequest):
    tool = get_list_append_tool()
    return {"result": tool.add_items(request.items, request.new_items)}


class JoinStringsRequest(BaseModel):
    strings: List[str]
    separator: str = ""


@router.post("/join")
async def join_strings(request: JoinStringsRequest):
    tool = get_list_append_tool()
    return {"result": tool.join_strings(request.strings, request.separator)}


class SplitJoinRequest(BaseModel):
    items: List[Any]
    sep: str = ", "


@router.post("/split-join")
async def split_join(request: SplitJoinRequest):
    tool = get_list_append_tool()
    return {"result": tool.split_join(request.items, request.sep)}