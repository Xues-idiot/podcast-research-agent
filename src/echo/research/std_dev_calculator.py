"""标准差计算器"""

from typing import Any, List, Optional
import statistics


class StdDevCalculator:
    _instance: Optional["StdDevCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stdev(self, items: List[float]) -> Optional[float]:
        if len(items) < 2:
            return None
        try:
            return statistics.stdev(items)
        except statistics.StatisticsError:
            return None

    def pstdev(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        try:
            return statistics.pstdev(items)
        except statistics.StatisticsError:
            return None


def get_std_dev_calculator() -> StdDevCalculator:
    return StdDevCalculator()
