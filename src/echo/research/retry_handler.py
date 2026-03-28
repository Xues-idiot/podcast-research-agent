"""重试工具"""

import time
from typing import Callable, Any, Optional


class RetryHandlerTool:
    _instance: Optional["RetryHandlerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def retry(self, func: Callable, max_attempts: int = 3, delay: float = 1.0) -> Any:
        attempts = 0
        while attempts < max_attempts:
            try:
                return func()
            except Exception as e:
                attempts += 1
                if attempts >= max_attempts:
                    raise e
                time.sleep(delay)
        return None


def get_retry_handler_tool() -> RetryHandlerTool:
    return RetryHandlerTool()