"""队列工具"""

from typing import Any, Optional
from collections import deque


class QueueTool:
    _instance: Optional["QueueTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def enqueue(self, queue: deque, item: Any) -> None:
        queue.append(item)

    def dequeue(self, queue: deque) -> Any:
        return queue.popleft() if queue else None

    def peek(self, queue: deque) -> Any:
        return queue[0] if queue else None

    def size(self, queue: deque) -> int:
        return len(queue)


def get_queue_tool() -> QueueTool:
    return QueueTool()
