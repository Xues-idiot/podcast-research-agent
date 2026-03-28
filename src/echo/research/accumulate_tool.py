"""累积工具"""

from typing import List, Optional


class AccumulateTool:
    _instance: Optional["AccumulateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def accumulate(self, signal: List[float]) -> List[float]:
        result = []
        total = 0.0
        for s in signal:
            total += s
            result.append(total)
        return result


def get_accumulate_tool() -> AccumulateTool:
    return AccumulateTool()
