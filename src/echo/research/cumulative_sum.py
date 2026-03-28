"""累积和工具"""

from typing import List, Optional


class CumulativeSumTool:
    _instance: Optional["CumulativeSumTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cumsum(self, values: List[float]) -> List[float]:
        """累积和"""
        result = []
        total = 0
        for v in values:
            total += v
            result.append(total)
        return result

    def cumprod(self, values: List[float]) -> List[float]:
        """累积积"""
        result = []
        total = 1
        for v in values:
            total *= v
            result.append(total)
        return result

    def diff(self, values: List[float]) -> List[float]:
        """差分"""
        if len(values) < 2:
            return []
        return [values[i] - values[i-1] for i in range(1, len(values))]

    def normalize(self, values: List[float]) -> List[float]:
        """归一化到0-1"""
        if not values:
            return []
        min_val = min(values)
        max_val = max(values)
        if max_val == min_val:
            return [0.5] * len(values)
        return [(v - min_val) / (max_val - min_val) for v in values]


def get_cumulative_sum_tool() -> CumulativeSumTool:
    return CumulativeSumTool()