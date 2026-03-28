"""梯度工具"""

from typing import List, Optional


class GradientTool:
    _instance: Optional["GradientTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gradient(self, signal: List[float]) -> List[float]:
        result = []
        for i in range(1, len(signal)):
            result.append(signal[i] - signal[i - 1])
        return result


def get_gradient_tool() -> GradientTool:
    return GradientTool()
