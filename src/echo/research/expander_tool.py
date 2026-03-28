"""扩展器"""

from typing import List, Optional


class ExpanderTool:
    _instance: Optional["ExpanderTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def expand(self, signal: List[float], threshold: float = 0.1, ratio: float = 2.0) -> List[float]:
        result = []
        for s in signal:
            if abs(s) < threshold:
                result.append(s * ratio)
            else:
                result.append(s)
        return result


def get_expander_tool() -> ExpanderTool:
    return ExpanderTool()
