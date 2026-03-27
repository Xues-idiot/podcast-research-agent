"""并发工具"""

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Optional, Any


class ConcurrentTool:
    _instance: Optional["ConcurrentTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parallel_map(self, func: Callable, items: List[Any], workers: int = 4) -> List[Any]:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            return list(executor.map(func, items))


def get_concurrent_tool() -> ConcurrentTool:
    return ConcurrentTool()
