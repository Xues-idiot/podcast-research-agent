"""三角函数工具"""

from typing import Optional
import math


class TrigTool:
    """三角函数工具"""

    def sin(self, angle: float) -> float:
        """正弦"""
        return math.sin(math.radians(angle))

    def cos(self, angle: float) -> float:
        """余弦"""
        return math.cos(math.radians(angle))

    def tan(self, angle: float) -> float:
        """正切"""
        return math.tan(math.radians(angle))


_tool: Optional[TrigTool] = None


def get_trig_tool() -> TrigTool:
    global _tool
    if _tool is None:
        _tool = TrigTool()
    return _tool