"""高通滤波器"""

from typing import List


class HighPassFilter:
    _instance: Optional["HighPassFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], alpha: float = 0.7) -> List[float]:
        if len(data) == 0:
            return []
        result = [data[0]]
        for i in range(1, len(data)):
            result.append(alpha * (result[-1] + data[i] - data[i-1]))
        return result


def get_high_pass_filter() -> HighPassFilter:
    return HighPassFilter()
