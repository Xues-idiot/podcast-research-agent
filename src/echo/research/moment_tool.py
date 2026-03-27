"""矩计算器"""

import statistics
from typing import List, Optional


class MomentTool:
    _instance: Optional["MomentTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def raw_moment(self, data: List[float], order: int) -> Optional[float]:
        if order < 0 or len(data) == 0:
            return None
        return statistics.mean([x ** order for x in data])

    def central_moment(self, data: List[float], order: int) -> Optional[float]:
        if order < 0 or len(data) == 0:
            return None
        mean = statistics.mean(data)
        return statistics.mean([(x - mean) ** order for x in data])


def get_moment_tool() -> MomentTool:
    return MomentTool()
