"""最小最大工具"""

from typing import List, Any, Optional


class MinMaxTool:
    _instance: Optional["MinMaxTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_min(self, items: List[Any]) -> Any:
        if not items:
            return None
        return min(items)

    def find_max(self, items: List[Any]) -> Any:
        if not items:
            return None
        return max(items)

    def find_min_max(self, items: List[Any]) -> tuple:
        if not items:
            return None, None
        return min(items), max(items)


def get_min_max_tool() -> MinMaxTool:
    return MinMaxTool()