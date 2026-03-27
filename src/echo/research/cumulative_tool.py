"""累积计算工具"""

from typing import List


class CumulativeTool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cumsum(self, data: List[float]) -> List[float]:
        result = []
        total = 0
        for x in data:
            total += x
            result.append(total)
        return result

    def cumprod(self, data: List[float]) -> List[float]:
        result = []
        total = 1
        for x in data:
            total *= x
            result.append(total)
        return result


def get_cumulative_tool() -> CumulativeTool:
    return CumulativeTool()
