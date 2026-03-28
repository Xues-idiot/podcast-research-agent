"""比例计算工具"""

from typing import List, Optional


class RatioCalcTool:
    _instance: Optional["RatioCalcTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ratio(self, a: float, b: float) -> float:
        """计算a:b的比值"""
        if b == 0:
            return float('inf')
        return a / b

    def simplify_ratio(self, a: float, b: float) -> tuple:
        """简化比例"""
        from math import gcd
        if b == 0:
            return (int(a), 0) if a != 0 else (0, 0)
        g = gcd(int(a), int(b))
        return (int(a) // g, int(b) // g)

    def proportion(self, value: float, total: float) -> float:
        """计算占比"""
        if total == 0:
            return 0.0
        return value / total

    def scale_values(self, values: List[float], target_min: float, target_max: float) -> List[float]:
        """将值缩放到指定范围"""
        if not values:
            return []
        min_val = min(values)
        max_val = max(values)
        if max_val == min_val:
            mid = (target_min + target_max) / 2
            return [mid] * len(values)
        return [target_min + (v - min_val) / (max_val - min_val) * (target_max - target_min) for v in values]


def get_ratio_calc_tool() -> RatioCalcTool:
    return RatioCalcTool()