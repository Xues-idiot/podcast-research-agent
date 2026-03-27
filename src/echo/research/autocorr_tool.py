"""自相关工具"""

from typing import List, Optional


class AutocorrTool:
    _instance: Optional["AutocorrTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def autocorrelation(self, data: List[float], lag: int = 1) -> float:
        if lag >= len(data):
            return 0.0
        n = len(data) - lag
        mean = sum(data) / len(data)
        c0 = sum((x - mean) ** 2 for x in data) / len(data)
        clag = sum((data[i] - mean) * (data[i + lag] - mean) for i in range(n)) / n
        return clag / c0 if c0 != 0 else 0.0


def get_autocorr_tool() -> AutocorrTool:
    return AutocorrTool()
