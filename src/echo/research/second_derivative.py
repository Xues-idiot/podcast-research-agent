"""二阶微分工具"""

from typing import List, Optional


class SecondDerivativeTool:
    _instance: Optional["SecondDerivativeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def second_derivative(self, signal: List[float]) -> List[float]:
        result = []
        for i in range(1, len(signal) - 1):
            result.append(signal[i + 1] - 2 * signal[i] + signal[i - 1])
        return result


def get_second_derivative_tool() -> SecondDerivativeTool:
    return SecondDerivativeTool()
