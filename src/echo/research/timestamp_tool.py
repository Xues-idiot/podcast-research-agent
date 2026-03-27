"""时间戳工具"""

import time
from typing import Optional


class TimestampTool:
    """时间戳工具"""

    def now(self) -> float:
        """获取当前时间戳"""
        return time.time()

    def now_ms(self) -> int:
        """获取当前毫秒时间戳"""
        return int(time.time() * 1000)

    def from_timestamp(self, ts: float) -> str:
        """从时间戳获取可读时间"""
        return time.ctime(ts)


_timestamp_tool: Optional[TimestampTool] = None


def get_timestamp_tool() -> TimestampTool:
    global _timestamp_tool
    if _timestamp_tool is None:
        _timestamp_tool = TimestampTool()
    return _timestamp_tool