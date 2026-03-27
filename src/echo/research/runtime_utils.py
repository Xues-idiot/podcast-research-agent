"""运行时工具"""

import time
from typing import Callable, Optional, Any


class RuntimeUtils:
    _instance: Optional["RuntimeUtils"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def measure(self, func: Callable, *args, **kwargs) -> tuple:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        return result, elapsed


def get_runtime_utils() -> RuntimeUtils:
    return RuntimeUtils()
