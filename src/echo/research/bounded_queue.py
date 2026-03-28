"""有界队列工具"""

from typing import List, Any, Optional
from collections import deque


class BoundedQueueTool:
    _instance: Optional["BoundedQueueTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, max_size: int) -> dict:
        """创建有界队列"""
        return {
            "max_size": max_size,
            "items": []
        }

    def push(self, queue: dict, item: Any) -> dict:
        """入队"""
        q = queue["items"]
        if len(q) >= queue["max_size"]:
            q.pop(0)
        q.append(item)
        return queue

    def pop(self, queue: dict) -> tuple:
        """出队"""
        if not queue["items"]:
            return None, queue
        item = queue["items"].pop(0)
        return item, queue

    def peek(self, queue: dict) -> Any:
        """查看队首"""
        return queue["items"][0] if queue["items"] else None

    def size(self, queue: dict) -> int:
        """大小"""
        return len(queue["items"])

    def is_full(self, queue: dict) -> bool:
        """是否满"""
        return len(queue["items"]) >= queue["max_size"]

    def is_empty(self, queue: dict) -> bool:
        """是否空"""
        return len(queue["items"]) == 0


def get_bounded_queue_tool() -> BoundedQueueTool:
    return BoundedQueueTool()