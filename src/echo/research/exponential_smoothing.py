"""指数平滑工具"""

from typing import List, Optional


class ExponentialSmoothing:
    _instance: Optional["ExponentialSmoothing"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def smooth(self, data: List[float], alpha: float = 0.3) -> List[float]:
        if not data or alpha <= 0 or alpha >= 1:
            return data
        result = [data[0]]
        for i in range(1, len(data)):
            result.append(alpha * data[i] + (1 - alpha) * result[-1])
        return result


def get_exponential_smoothing() -> ExponentialSmoothing:
    return ExponentialSmoothing()
