"""时间戳工具"""

from typing import Optional


class TimestampTool:
    """时间戳工具"""

    def now_unix(self) -> int:
        """当前Unix时间戳"""
        import time
        return int(time.time())

    def now_ms(self) -> int:
        """当前毫秒时间戳"""
        import time
        return int(time.time() * 1000)

    def from_unix(self, timestamp: int) -> str:
        """Unix时间戳转字符串"""
        import datetime
        return datetime.datetime.fromtimestamp(timestamp).isoformat()


_tool: Optional[TimestampTool] = None


def get_timestamp_tool() -> TimestampTool:
    global _tool
    if _tool is None:
        _tool = TimestampTool()
    return _tool