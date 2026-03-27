"""队列API"""

from fastapi import APIRouter

from echo.research.queue_tool import get_queue_tool
from collections import deque


router = APIRouter(prefix="/api/queue", tags=["queue"])


@router.post("/peek")
async def peek(queue: list):
    """查看队首"""
    tool = get_queue_tool()
    q = deque(queue)
    return {"item": tool.peek(q)}


@router.post("/size")
async def size(queue: list):
    """获取大小"""
    tool = get_queue_tool()
    q = deque(queue)
    return {"size": tool.size(q)}
