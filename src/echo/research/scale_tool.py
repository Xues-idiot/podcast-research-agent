"""缩放工具"""

from typing import List, Optional


class ScaleTool:
    _instance: Optional["ScaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scale(self, signal: List[float], factor: float) -> List[float]:
        return [s * factor for s in signal]


def get_scale_tool() -> ScaleTool:
    return ScaleTool()
