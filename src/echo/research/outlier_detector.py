"""异常值检测器"""

import statistics
from typing import List, Optional


class OutlierDetector:
    _instance: Optional["OutlierDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def iqr_outliers(self, data: List[float], multiplier: float = 1.5) -> List[float]:
        if len(data) < 4:
            return []
        sorted_data = sorted(data)
        n = len(sorted_data)
        q1 = sorted_data[n // 4]
        q3 = sorted_data[3 * n // 4]
        iqr = q3 - q1
        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr
        return [x for x in data if x < lower or x > upper]

    def zscore_outliers(self, data: List[float], threshold: float = 3.0) -> List[float]:
        if len(data) < 3:
            return []
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        if stdev == 0:
            return []
        return [x for x in data if abs((x - mean) / stdev) > threshold]


def get_outlier_detector() -> OutlierDetector:
    return OutlierDetector()
