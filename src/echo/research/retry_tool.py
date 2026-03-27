"""重试工具"""

import time
from typing import Callable, Optional


class RetryTool:
    """重试工具"""

    def retry(self, func: Callable, max_attempts: int = 3, delay: float = 1.0) -> any:
        """重试执行"""
        last_error = None
        for attempt in range(max_attempts):
            try:
                return func()
            except Exception as e:
                last_error = e
                if attempt < max_attempts - 1:
                    time.sleep(delay)
        raise last_error


_tool: Optional[RetryTool] = None


def get_retry_tool() -> RetryTool:
    global _tool
    if _tool is None:
        _tool = RetryTool()
    return _tool