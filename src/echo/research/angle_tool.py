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

    def sin(self, degrees: float) -> float:
        """正弦"""
        return math.sin(math.radians(degrees))

    def cos(self, degrees: float) -> float:
        """余弦"""
        return math.cos(math.radians(degrees))


_angle_tool: Optional[AngleTool] = None


def get_angle_tool() -> AngleTool:
    global _angle_tool
    if _angle_tool is None:
        _angle_tool = AngleTool()
    return _angle_tool