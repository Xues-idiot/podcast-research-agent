"""众数计算器"""

from collections import Counter
from typing import List, Optional


class ModeCalc:
    _instance: Optional["ModeCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mode(self, values: List[float]) -> float:
        if not values:
            return 0.0
        counter = Counter(values)
        return counter.most_common(1)[0][0]


def get_mode_calc() -> ModeCalc:
    return ModeCalc()
