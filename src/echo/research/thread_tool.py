"""线程池工具"""

from typing import Any, Callable, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed


class ThreadPoolTool:
    _instance: Optional["ThreadPoolTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def map(self, func: Callable, items: List[Any], max_workers: int = 4) -> List[Any]:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(func, items))
        return results

    def submit(self, func: Callable, *args, **kwargs):
        with ThreadPoolExecutor(max_workers=1) as executor:
            return executor.submit(func, *args, **kwargs)


def get_thread_pool_tool() -> ThreadPoolTool:
    return ThreadPoolTool()
