"""RMS计算器"""

import math
from typing import List, Optional


class RmsCalculator:
    _instance: Optional["RmsCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, signal: List[float]) -> float:
        if not signal:
            return 0.0
        return math.sqrt(sum(x ** 2 for x in signal) / len(signal))


def get_rms_calculator() -> RmsCalculator:
    return RmsCalculator()
