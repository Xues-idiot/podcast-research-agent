"""工作者工具"""

from typing import Any, Callable, List, Optional
from concurrent.futures import ProcessPoolExecutor, as_completed


class WorkerTool:
    _instance: Optional["WorkerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parallel(self, func: Callable, items: List[Any], max_workers: int = 4) -> List[Any]:
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(func, item): item for item in items}
            results = [future.result() for future in as_completed(futures)]
        return results

    def map_reduce(self, map_func: Callable, reduce_func: Callable, items: List[Any]) -> Any:
        mapped = [map_func(item) for item in items]
        return reduce_func(mapped)


def get_worker_tool() -> WorkerTool:
    return WorkerTool()
