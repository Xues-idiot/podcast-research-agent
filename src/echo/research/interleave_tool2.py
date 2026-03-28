"""插值工具v2"""

from typing import List, Optional


class InterleaveTool2:
    _instance: Optional["InterleaveTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interleave(self, *signals: List[float]) -> List[float]:
        max_len = max(len(s) for s in signals) if signals else 0
        result = []
        for i in range(max_len):
            for s in signals:
                if i < len(s):
                    result.append(s[i])
        return result


def get_interleave_tool2() -> InterleaveTool2:
    return InterleaveTool2()
