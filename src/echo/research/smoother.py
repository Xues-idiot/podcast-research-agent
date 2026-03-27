"""平滑工具"""

from typing import List


class Smoother:
    _instance: Optional["Smoother"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def moving_average(self, data: List[float], window: int) -> List[float]:
        if window <= 0 or window > len(data):
            return data
        result = []
        for i in range(len(data)):
            start = max(0, i - window + 1)
            result.append(sum(data[start:i+1]) / (i - start + 1))
        return result


def get_smoother() -> Smoother:
    return Smoother()
