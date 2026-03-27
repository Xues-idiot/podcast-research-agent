"""超时工具"""

import time
from typing import Optional


class TimeoutTool:
    """超时工具"""

    def is_timeout(self, start_time: float, timeout_seconds: float) -> bool:
        """是否超时"""
        return time.time() - start_time > timeout_seconds

    def remaining(self, start_time: float, timeout_seconds: float) -> float:
        """剩余时间"""
        remaining = timeout_seconds - (time.time() - start_time)
        return max(0, remaining)


_tool: Optional[TimeoutTool] = None


def get_timeout_tool() -> TimeoutTool:
    global _tool
    if _tool is None:
        _tool = TimeoutTool()
    return _tool