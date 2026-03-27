"""功率谱计算器"""

import math
from typing import List, Optional


class PowerSpectrum:
    _instance: Optional["PowerSpectrum"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, signal: List[float]) -> List[float]:
        if len(signal) == 0:
            return []
        n = len(signal)
        spectrum = [abs(x) ** 2 for x in signal]
        return [s / n for s in spectrum]


def get_power_spectrum() -> PowerSpectrum:
    return PowerSpectrum()
