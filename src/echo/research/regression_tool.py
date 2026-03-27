"""线性回归工具"""

import statistics
from typing import List, Optional, Tuple


class RegressionTool:
    _instance: Optional["RegressionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear_regression(self, x: List[float], y: List[float]) -> Optional[Tuple[float, float]]:
        if len(x) != len(y) or len(x) < 2:
            return None
        try:
            slope, intercept = statistics.linear_regression(x, y)
            return (slope, intercept)
        except statistics.StatisticsError:
            return None

    def predict(self, slope: float, intercept: float, x: float) -> float:
        return slope * x + intercept


def get_regression_tool() -> RegressionTool:
    return RegressionTool()
