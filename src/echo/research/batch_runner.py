"""批处理运行器"""

from typing import Any, Callable, List, Optional, TypeVar


T = TypeVar("T")


class BatchRunner:
    _instance: Optional["BatchRunner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def run_batch(self, func: Callable[[T], Any], items: List[T], batch_size: int = 10) -> List[Any]:
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            results.extend([func(item) for item in batch])
        return results

    def run_transform(self, func: Callable[[List[T]], List[Any]], items: List[T]) -> List[Any]:
        return func(items)


def get_batch_runner() -> BatchRunner:
    return BatchRunner()
