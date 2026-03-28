"""优先级队列工具"""

from typing import List, Any, Optional, Tuple


class PriorityQueueTool:
    _instance: Optional["PriorityQueueTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._items: List[Tuple[int, Any]] = []

    def enqueue(self, item: Any, priority: int = 0) -> None:
        """入队"""
        self._items.append((priority, item))
        self._items.sort(key=lambda x: x[0])

    def dequeue(self) -> Optional[Any]:
        """出队"""
        if not self._items:
            return None
        return self._items.pop(0)[1]

    def peek(self) -> Optional[Any]:
        """查看最高优先级项"""
        return self._items[0][1] if self._items else None

    def size(self) -> int:
        """大小"""
        return len(self._items)

    def is_empty(self) -> bool:
        """是否空"""
        return len(self._items) == 0

    def clear(self) -> None:
        """清空"""
        self._items.clear()


_pq_instance: Optional[PriorityQueueTool] = None


def get_priority_queue_tool() -> PriorityQueueTool:
    global _pq_instance
    if _pq_instance is None:
        _pq_instance = PriorityQueueTool()
    return _pq_instance