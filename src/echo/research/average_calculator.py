"""平均值计算器"""

from typing import Optional


class AverageCalculator:
    """平均值计算器"""

    def mean(self, values: list[float]) -> float:
        """算术平均"""
        if not values:
            return 0
        return sum(values) / len(values)

    def median(self, values: list[float]) -> float:
        """中位数"""
        if not values:
            return 0
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        if n % 2 == 0:
            return (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
        return sorted_vals[n//2]

    def mode(self, values: list) -> any:
        """众数"""
        from collections import Counter
        if not values:
            return None
        counter = Counter(values)
        return counter.most_common(1)[0][0]


_calculator: Optional[AverageCalculator] = None


def get_average_calculator() -> AverageCalculator:
    global _calculator
    if _calculator is None:
        _calculator = AverageCalculator()
    return _calculator