"""平衡工具"""

from typing import List, Optional


class BalanceTool:
    _instance: Optional["BalanceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def balance(self, left: List[float], right: List[float], amount: float) -> List[List[float]]:
        return left, right


def get_balance_tool() -> BalanceTool:
    return BalanceTool()
