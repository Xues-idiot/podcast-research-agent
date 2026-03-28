"""有界队列API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Optional

from echo.research.bounded_queue import get_bounded_queue_tool


router = APIRouter(prefix="/api/bounded-queue", tags=["bounded-queue"])

_queues = {}


class CreateQueueRequest(BaseModel):
    max_size: int
    queue_id: str = "default"


@router.post("/create")
async def create(request: CreateQueueRequest):
    tool = get_bounded_queue_tool()
    q = tool.create(request.max_size)
    _queues[request.queue_id] = q
    return {"queue_id": request.queue_id, "queue": q}


class PushRequest(BaseModel):
    item: Any
    queue_id: str = "default"


@router.post("/push")
async def push(request: PushRequest):
    tool = get_bounded_queue_tool()
    if request.queue_id not in _queues:
        return {"error": "Queue not found"}
    _queues[request.queue_id] = tool.push(_queues[request.queue_id], request.item)
    return {"queue": _queues[request.queue_id]}


class PopRequest(BaseModel):
    queue_id: str = "default"


@router.post("/pop")
async def pop(request: PopRequest):
    tool = get_bounded_queue_tool()
    if request.queue_id not in _queues:
        return {"error": "Queue not found"}
    item, _queues[request.queue_id] = tool.pop(_queues[request.queue_id])
    return {"item": item, "queue": _queues[request.queue_id]}


@router.post("/peek")
async def peek(request: PopRequest):
    tool = get_bounded_queue_tool()
    if request.queue_id not in _queues:
        return {"error": "Queue not found"}
    return {"item": tool.peek(_queues[request.queue_id])}


@router.post("/size")
async def size(request: PopRequest):
    tool = get_bounded_queue_tool()
    if request.queue_id not in _queues:
        return {"error": "Queue not found"}
    return {"size": tool.size(_queues[request.queue_id])}


@router.post("/status")
async def status(request: PopRequest):
    tool = get_bounded_queue_tool()
    if request.queue_id not in _queues:
        return {"error": "Queue not found"}
    q = _queues[request.queue_id]
    return {
        "is_full": tool.is_full(q),
        "is_empty": tool.is_empty(q),
        "size": tool.size(q)
    }