"""百分比工具"""

from typing import Optional


class PercentageTool:
    """百分比工具"""

    def to_percent(self, value: float, total: float) -> float:
        """转百分比"""
        return (value / total * 100) if total else 0

    def of_percent(self, percent: float, total: float) -> float:
        """百分比的值"""
        return (percent / 100) * total

    def change_percent(self, old_val: float, new_val: float) -> float:
        """变化百分比"""
        if old_val == 0:
            return 0
        return ((new_val - old_val) / old_val) * 100


_tool: Optional[PercentageTool] = None


def get_percentage_tool() -> PercentageTool:
    global _tool
    if _tool is None:
        _tool = PercentageTool()
    return _tool