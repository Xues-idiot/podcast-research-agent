"""卷积工具"""

from typing import List, Optional


class ConvolveTool:
    _instance: Optional["ConvolveTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convolve(self, signal: List[float], kernel: List[float]) -> List[float]:
        result = []
        for i in range(len(signal) - len(kernel) + 1):
            val = sum(signal[i + j] * kernel[j] for j in range(len(kernel)))
            result.append(val)
        return result


def get_convolve_tool() -> ConvolveTool:
    return ConvolveTool()
