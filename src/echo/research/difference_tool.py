"""差分工具"""

from typing import List


class DifferenceTool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def diff(self, data: List[float], periods: int = 1) -> List[float]:
        if len(data) <= periods:
            return []
        return [data[i] - data[i - periods] for i in range(periods, len(data))]


def get_difference_tool() -> DifferenceTool:
    return DifferenceTool()
