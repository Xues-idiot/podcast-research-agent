"""批处理执行器"""

from typing import List, Callable, Any, Optional


class BatchExecutor:
    _instance: Optional["BatchExecutor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def execute(self, tasks: List[Callable], batch_size: int = 10) -> List[Any]:
        results = []
        for i in range(0, len(tasks), batch_size):
            batch = tasks[i:i+batch_size]
            for task in batch:
                results.append(task())
        return results


def get_batch_executor() -> BatchExecutor:
    return BatchExecutor()
