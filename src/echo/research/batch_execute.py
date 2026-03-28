"""批量执行工具"""

from typing import List, Callable, Any, Optional


class BatchExecuteTool:
    _instance: Optional["BatchExecuteTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def batch_execute(self, func: Callable, items: List[Any], batch_size: int = 10) -> List[Any]:
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i+batch_size]
            results.extend([func(item) for item in batch])
        return results


def get_batch_execute_tool() -> BatchExecuteTool:
    return BatchExecuteTool()