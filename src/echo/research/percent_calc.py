"""百分比计算工具"""

from typing import Optional


class PercentCalcTool:
    _instance: Optional["PercentCalcTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate(self, part: float, whole: float) -> float:
        """计算百分比"""
        if whole == 0:
            return 0.0
        return (part / whole) * 100

    def of(self, percent: float, whole: float) -> float:
        """百分比的绝对值"""
        return (percent / 100) * whole

    def change(self, old_val: float, new_val: float) -> float:
        """计算变化百分比"""
        if old_val == 0:
            return 0.0
        return ((new_val - old_val) / old_val) * 100

    def increase(self, original: float, percent: float) -> float:
        """增加百分比后的值"""
        return original * (1 + percent / 100)

    def decrease(self, original: float, percent: float) -> float:
        """减少百分比后的值"""
        return original * (1 - percent / 100)

    def reverse(self, reduced_val: float, percent: float) -> float:
        """反向还原百分比(如折扣后还原原价)"""
        if percent >= 100:
            return 0.0
        return reduced_val / (1 - percent / 100)

    def proportion_to_percent(self, proportion: float) -> float:
        """比例转百分比"""
        return proportion * 100

    def percent_to_proportion(self, percent: float) -> float:
        """百分比转比例"""
        return percent / 100


_pct_instance: Optional[PercentCalcTool] = None


def get_percent_calc_tool() -> PercentCalcTool:
    global _pct_instance
    if _pct_instance is None:
        _pct_instance = PercentCalcTool()
    return _pct_instance