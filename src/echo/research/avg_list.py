"""平均值工具"""

from typing import List, Any, Optional, Callable


class AvgList:
    _instance: Optional["AvgList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def avg(self, items: List[float]) -> float:
        if not items:
            return 0
        return sum(items) / len(items)

    def avg_by(self, items: List[Any], key: Callable) -> float:
        if not items:
            return 0
        return sum(key(item) for item in items) / len(items)

    def mean(self, items: List[float]) -> float:
        return self.avg(items)


def get_avg_list() -> AvgList:
    return AvgList()
