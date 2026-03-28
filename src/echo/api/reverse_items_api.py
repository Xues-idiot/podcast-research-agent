"""反转工具API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.reverse_items import get_reverse_items_tool


router = APIRouter(prefix="/api/reverse-items", tags=["reverse-items"])


class ReverseListRequest(BaseModel):
    items: List[Any]


@router.post("/reverse-list")
async def reverse_list(request: ReverseListRequest):
    tool = get_reverse_items_tool()
    return {"result": tool.reverse_list(request.items)}


class ReverseStringRequest(BaseModel):
    text: str


@router.post("/reverse-string")
async def reverse_string(request: ReverseStringRequest):
    tool = get_reverse_items_tool()
    return {"result": tool.reverse_string(request.text)}


@router.post("/palindrome-check")
async def palindrome_check(request: ReverseStringRequest):
    tool = get_reverse_items_tool()
    return {"result": tool.palindrome_check(request.text)}