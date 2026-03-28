"""反相工具"""

from typing import List, Optional


class InvertTool:
    _instance: Optional["InvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def invert(self, signal: List[float]) -> List[float]:
        return [-s for s in signal]


def get_invert_tool() -> InvertTool:
    return InvertTool()
