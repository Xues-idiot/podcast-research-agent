"""标准化工具"""

import statistics
from typing import List, Optional


class Standardizer:
    _instance: Optional["Standardizer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def standardize(self, data: List[float]) -> Optional[List[float]]:
        if len(data) < 2:
            return None
        try:
            mean = statistics.mean(data)
            stdev = statistics.stdev(data)
            if stdev == 0:
                return [0.0] * len(data)
            return [(x - mean) / stdev for x in data]
        except:
            return None


def get_standardizer() -> Standardizer:
    return Standardizer()
