"""重试工具"""

import time
from typing import Callable, Optional, Any


class RetryFunc:
    _instance: Optional["RetryFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def retry(self, func: Callable, max_attempts: int = 3, delay: float = 1.0) -> Any:
        for attempt in range(max_attempts):
            try:
                return func()
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                time.sleep(delay)


def get_retry_func() -> RetryFunc:
    return RetryFunc()
