"""对数工具"""

from typing import Optional
import math


class LogTool:
    """对数工具"""

    def log(self, value: float, base: float = math.e) -> float:
        """计算对数"""
        if value <= 0:
            return 0
        return math.log(value, base)

    def log10(self, value: float) -> float:
        """常用对数"""
        if value <= 0:
            return 0
        return math.log10(value)

    def log2(self, value: float) -> float:
        """二进制对数"""
        if value <= 0:
            return 0
        return math.log2(value)


_log_tool: Optional[LogTool] = None


def get_log_tool() -> LogTool:
    global _log_tool
    if _log_tool is None:
        _log_tool = LogTool()
    return _log_tool