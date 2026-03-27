"""效应量工具"""

import statistics
import math
from typing import List, Optional


class EffectSize:
    _instance: Optional["EffectSize"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cohens_d(self, group1: List[float], group2: List[float]) -> Optional[float]:
        if len(group1) < 2 or len(group2) < 2:
            return None
        mean1, mean2 = statistics.mean(group1), statistics.mean(group2)
        var1, var2 = statistics.variance(group1), statistics.variance(group2)
        n1, n2 = len(group1), len(group2)
        pooled_std = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
        if pooled_std == 0:
            return None
        return (mean1 - mean2) / pooled_std


def get_effect_size() -> EffectSize:
    return EffectSize()
