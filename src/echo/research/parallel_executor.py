"""并行执行器"""

from typing import List, Callable, Any, Optional
import concurrent.futures


class ParallelExecutor:
    _instance: Optional["ParallelExecutor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def execute(self, funcs: List[Callable], max_workers: int = 4) -> List[Any]:
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(f) for f in funcs]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        return results


def get_parallel_executor() -> ParallelExecutor:
    return ParallelExecutor()
