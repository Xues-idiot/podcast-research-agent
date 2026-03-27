"""延迟工具"""

import time
from typing import Optional


class DelayTool:
    """延迟工具"""

    def delay(self, seconds: float):
        """延迟执行"""
        time.sleep(seconds)

    def retry_delay(self, max_attempts: int = 3, delay: float = 1.0):
        """重试延迟"""
        for i in range(max_attempts - 1):
            time.sleep(delay)


_tool: Optional[DelayTool] = None


def get_delay_tool() -> DelayTool:
    global _tool
    if _tool is None:
        _tool = DelayTool()
    return _tool