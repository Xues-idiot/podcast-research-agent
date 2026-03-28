"""双端队列API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.deque_tool import get_deque_tool


router = APIRouter(prefix="/api/deque-tool", tags=["deque-tool"])


class ItemRequest(BaseModel):
    item: Any


@router.post("/append-left")
async def append_left(request: ItemRequest):
    tool = get_deque_tool()
    tool.append_left(request.item)
    return {"size": tool.size()}


@router.post("/append-right")
async def append_right(request: ItemRequest):
    tool = get_deque_tool()
    tool.append_right(request.item)
    return {"size": tool.size()}


@router.post("/pop-left")
async def pop_left():
    tool = get_deque_tool()
    item = tool.pop_left()
    return {"item": item, "size": tool.size()}


@router.post("/pop-right")
async def pop_right():
    tool = get_deque_tool()
    item = tool.pop_right()
    return {"item": item, "size": tool.size()}


@router.post("/peek-left")
async def peek_left():
    tool = get_deque_tool()
    return {"item": tool.peek_left()}


@router.post("/peek-right")
async def peek_right():
    tool = get_deque_tool()
    return {"item": tool.peek_right()}


@router.post("/size")
async def size():
    tool = get_deque_tool()
    return {"size": tool.size()}


@router.post("/is-empty")
async def is_empty():
    tool = get_deque_tool()
    return {"is_empty": tool.is_empty()}


@router.post("/clear")
async def clear():
    tool = get_deque_tool()
    tool.clear()
    return {"success": True}


class RotateRequest(BaseModel):
    n: int


@router.post("/rotate")
async def rotate(request: RotateRequest):
    tool = get_deque_tool()
    tool.rotate(request.n)
    return {"success": True}