"""超时工具"""

from typing import Optional, Callable, Any
import time


class TimeoutTool:
    """超时工具"""

    def timeout_after(self, seconds: float, func: Callable, *args, **kwargs) -> Any:
        """超时后执行函数"""
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        if elapsed > seconds:
            raise TimeoutError(f"Function took {elapsed:.2f}s, expected {seconds}s")
        return result


_timeout_tool: Optional[TimeoutTool] = None


def get_timeout_tool() -> TimeoutTool:
    global _timeout_tool
    if _timeout_tool is None:
        _timeout_tool = TimeoutTool()
    return _timeout_tool