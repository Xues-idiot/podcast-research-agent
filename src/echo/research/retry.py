"""重试装饰器"""

import time
from typing import Callable, Any, Optional


class Retry:
    _instance: Optional["Retry"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def retry(self, func: Callable, max_attempts: int = 3, delay: float = 1.0) -> Any:
        for attempt in range(max_attempts):
            try:
                return func()
            except Exception:
                if attempt < max_attempts - 1:
                    time.sleep(delay)
                else:
                    return None
        return None


def get_retry() -> Retry:
    return Retry()
