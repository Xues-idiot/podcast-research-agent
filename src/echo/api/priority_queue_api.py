"""优先级队列API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.priority_queue import get_priority_queue_tool


router = APIRouter(prefix="/api/priority-queue", tags=["priority-queue"])


class EnqueueRequest(BaseModel):
    item: Any
    priority: int = 0


@router.post("/enqueue")
async def enqueue(request: EnqueueRequest):
    tool = get_priority_queue_tool()
    tool.enqueue(request.item, request.priority)
    return {"size": tool.size()}


@router.post("/dequeue")
async def dequeue():
    tool = get_priority_queue_tool()
    item = tool.dequeue()
    return {"item": item, "size": tool.size()}


@router.post("/peek")
async def peek():
    tool = get_priority_queue_tool()
    return {"item": tool.peek()}


@router.post("/size")
async def size():
    tool = get_priority_queue_tool()
    return {"size": tool.size()}


@router.post("/is-empty")
async def is_empty():
    tool = get_priority_queue_tool()
    return {"is_empty": tool.is_empty()}


@router.post("/clear")
async def clear():
    tool = get_priority_queue_tool()
    tool.clear()
    return {"success": True}