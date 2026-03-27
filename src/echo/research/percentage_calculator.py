"""百分比计算器"""

from typing import Optional


class PercentageCalculator:
    """百分比计算器"""

    def calculate(self, value: float, total: float) -> float:
        """计算百分比"""
        if total == 0:
            return 0
        return (value / total) * 100

    def of(self, percentage: float, total: float) -> float:
        """百分比的值"""
        return (percentage / 100) * total

    def change(self, old_value: float, new_value: float) -> float:
        """计算变化百分比"""
        if old_value == 0:
            return 0
        return ((new_value - old_value) / old_value) * 100


_calculator: Optional[PercentageCalculator] = None


def get_percentage_calculator() -> PercentageCalculator:
    global _calculator
    if _calculator is None:
        _calculator = PercentageCalculator()
    return _calculator