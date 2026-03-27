"""对数工具"""

from typing import Optional
import math


class LogarithmTool:
    """对数工具"""

    def log(self, value: float, base: float = math.e) -> float:
        """对数"""
        return math.log(value, base) if value > 0 else 0

    def log10(self, value: float) -> float:
        """常用对数"""
        return math.log10(value) if value > 0 else 0


_tool: Optional[LogarithmTool] = None


def get_logarithm_tool() -> LogarithmTool:
    global _tool
    if _tool is None:
        _tool = LogarithmTool()
    return _tool