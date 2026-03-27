"""角度工具"""

from typing import Optional
import math


class AngleTool:
    """角度工具"""

    def degrees_to_radians(self, degrees: float) -> float:
        """度转弧度"""
        return degrees * math.pi / 180

    def radians_to_degrees(self, radians: float) -> float:
        """弧度转度"""
        return radians * 180 / math.pi


_tool: Optional[AngleTool] = None


def get_angle_tool() -> AngleTool:
    global _tool
    if _tool is None:
        _tool = AngleTool()
    return _tool