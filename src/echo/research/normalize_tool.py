"""归一化工具"""

from typing import List, Optional


class NormalizeTool:
    _instance: Optional["NormalizeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, data: List[float]) -> List[float]:
        if not data:
            return []
        min_val = min(data)
        max_val = max(data)
        if max_val == min_val:
            return [0.5] * len(data)
        return [(x - min_val) / (max_val - min_val) for x in data]

    def standardize(self, data: List[float]) -> List[float]:
        if len(data) < 2:
            return [0.0] * len(data)
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        stdev = variance ** 0.5
        if stdev == 0:
            return [0.0] * len(data)
        return [(x - mean) / stdev for x in data]


def get_normalize_tool() -> NormalizeTool:
    return NormalizeTool()
