"""双边滤波器"""

import math
from typing import List


class BilateralFilter:
    _instance: Optional["BilateralFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], spatial_sigma: float = 1.0, range_sigma: float = 1.0, window: int = 3) -> List[float]:
        if len(data) == 0:
            return []
        result = []
        half = window // 2
        for i in range(len(data)):
            weighted_sum = 0.0
            weight_sum = 0.0
            for j in range(max(0, i - half), min(len(data), i + half + 1)):
                spatial_weight = math.exp(-((i - j) ** 2) / (2 * spatial_sigma ** 2))
                range_weight = math.exp(-((data[i] - data[j]) ** 2) / (2 * range_sigma ** 2))
                weight = spatial_weight * range_weight
                weighted_sum += data[j] * weight
                weight_sum += weight
            result.append(weighted_sum / weight_sum if weight_sum > 0 else data[i])
        return result


def get_bilateral_filter() -> BilateralFilter:
    return BilateralFilter()
