"""堆工具"""

from typing import Any, List, Optional
import heapq


class HeapTool:
    _instance: Optional["HeapTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def push(self, heap: List[Any], item: Any) -> None:
        heapq.heappush(heap, item)

    def pop(self, heap: List[Any]) -> Any:
        return heapq.heappop(heap) if heap else None

    def peek(self, heap: List[Any]) -> Any:
        return heap[0] if heap else None

    def heapify(self, items: List[Any]) -> List[Any]:
        heapq.heapify(items)
        return items


def get_heap_tool() -> HeapTool:
    return HeapTool()
