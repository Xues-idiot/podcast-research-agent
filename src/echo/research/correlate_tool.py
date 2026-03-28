"""相关工具"""

from typing import List, Optional


class CorrelateTool:
    _instance: Optional["CorrelateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def correlate(self, a: List[float], b: List[float]) -> float:
        if not a or not b or len(a) != len(b):
            return 0.0
        return sum(x * y for x, y in zip(a, b))


def get_correlate_tool() -> CorrelateTool:
    return CorrelateTool()
