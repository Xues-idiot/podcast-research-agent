"""互相关工具"""

from typing import List, Optional


class CrosscorrTool:
    _instance: Optional["CrosscorrTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cross_correlation(self, x: List[float], y: List[float]) -> float:
        if len(x) != len(y):
            return 0.0
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        den = (sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y)) ** 0.5
        return num / den if den != 0 else 0.0


def get_crosscorr_tool() -> CrosscorrTool:
    return CrosscorrTool()
