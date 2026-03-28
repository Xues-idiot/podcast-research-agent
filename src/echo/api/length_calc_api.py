"""长度工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.length_calc import get_length_calc_tool


router = APIRouter(prefix="/api/length-calc", tags=["length-calc"])


class ItemsRequest(BaseModel):
    items: List[Any]


@router.post("/length")
async def length(request: ItemsRequest):
    tool = get_length_calc_tool()
    return {"result": tool.length(request.items)}


@router.post("/is-empty")
async def is_empty(request: ItemsRequest):
    tool = get_length_calc_tool()
    return {"result": tool.is_empty(request.items)}


class CountRequest(BaseModel):
    items: List[Any]
    item: Any


@router.post("/count")
async def count(request: CountRequest):
    tool = get_length_calc_tool()
    return {"result": tool.count(request.items, request.item)}


class TextRequest(BaseModel):
    text: str


@router.post("/word-count")
async def word_count(request: TextRequest):
    tool = get_length_calc_tool()
    return {"result": tool.word_count(request.text)}


@router.post("/char-count")
async def char_count(request: TextRequest):
    tool = get_length_calc_tool()
    return {"result": tool.char_count(request.text)}