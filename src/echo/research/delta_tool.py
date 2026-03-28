"""差值工具"""

from typing import List, Optional


class DeltaTool:
    _instance: Optional["DeltaTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def delta(self, signal: List[float]) -> List[float]:
        result = []
        for i in range(1, len(signal)):
            result.append(signal[i] - signal[i - 1])
        return result


def get_delta_tool() -> DeltaTool:
    return DeltaTool()
