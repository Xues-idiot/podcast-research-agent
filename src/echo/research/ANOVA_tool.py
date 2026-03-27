"""方差分析工具"""

import statistics
import math
from typing import List, Optional


class AnovaTool:
    _instance: Optional["AnovaTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def one_way_anova(self, *groups: List[float]) -> Optional[float]:
        if len(groups) < 2:
            return None
        all_data = [x for group in groups for x in group]
        if len(all_data) < 3:
            return None
        grand_mean = statistics.mean(all_data)
        ss_between = sum(len(g) * (statistics.mean(g) - grand_mean) ** 2 for g in groups)
        ss_within = sum(sum((x - statistics.mean(g)) ** 2 for x in g) for g in groups)
        df_between = len(groups) - 1
        df_within = len(all_data) - len(groups)
        if df_within == 0:
            return None
        ms_between = ss_between / df_between
        ms_within = ss_within / df_within
        if ms_within == 0:
            return None
        return ms_between / ms_within


def get_anova_tool() -> AnovaTool:
    return AnovaTool()
