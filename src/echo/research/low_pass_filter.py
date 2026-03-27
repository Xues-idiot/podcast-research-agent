"""低通滤波器"""

from typing import List, Optional


class LowPassFilter:
    _instance: Optional["LowPassFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], alpha: float = 0.3) -> List[float]:
        if len(data) == 0:
            return []
        result = [data[0]]
        for i in range(1, len(data)):
            result.append(alpha * data[i] + (1 - alpha) * result[-1])
        return result


def get_low_pass_filter() -> LowPassFilter:
    return LowPassFilter()
