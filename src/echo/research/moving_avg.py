"""移动平均工具"""

from typing import List, Optional


class MovingAvgTool:
    _instance: Optional["MovingAvgTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def simple(self, values: List[float], window: int) -> List[float]:
        """简单移动平均"""
        if window <= 0 or len(values) < window:
            return []
        result = []
        for i in range(len(values) - window + 1):
            window_vals = values[i:i + window]
            result.append(sum(window_vals) / window)
        return result

    def exponential(self, values: List[float], alpha: float = 0.3) -> List[float]:
        """指数移动平均"""
        if not values:
            return []
        result = [values[0]]
        for v in values[1:]:
            ema = alpha * v + (1 - alpha) * result[-1]
            result.append(ema)
        return result

    def weighted(self, values: List[float], window: int) -> List[float]:
        """加权移动平均"""
        if window <= 0 or len(values) < window:
            return []
        weights = list(range(1, window + 1))
        weight_sum = sum(weights)
        result = []
        for i in range(len(values) - window + 1):
            window_vals = values[i:i + window]
            weighted_sum = sum(w * v for w, v in zip(weights, window_vals))
            result.append(weighted_sum / weight_sum)
        return result


def get_moving_avg_tool() -> MovingAvgTool:
    return MovingAvgTool()