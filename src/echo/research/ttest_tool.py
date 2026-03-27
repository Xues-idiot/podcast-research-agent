"""t检验工具"""

import statistics
import math
from typing import List, Optional


class TTestTool:
    _instance: Optional["TTestTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def one_sample_t(self, sample: List[float], pop_mean: float) -> Optional[float]:
        if len(sample) < 2:
            return None
        n = len(sample)
        mean = statistics.mean(sample)
        stdev = statistics.stdev(sample)
        if stdev == 0:
            return None
        return (mean - pop_mean) / (stdev / math.sqrt(n))

    def two_sample_t(self, sample1: List[float], sample2: List[float]) -> Optional[float]:
        if len(sample1) < 2 or len(sample2) < 2:
            return None
        mean1, mean2 = statistics.mean(sample1), statistics.mean(sample2)
        var1, var2 = statistics.variance(sample1), statistics.variance(sample2)
        n1, n2 = len(sample1), len(sample2)
        pooled_se = math.sqrt(var1/n1 + var2/n2)
        if pooled_se == 0:
            return None
        return (mean1 - mean2) / pooled_se


def get_ttest_tool() -> TTestTool:
    return TTestTool()
