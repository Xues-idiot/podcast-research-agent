"""Welch方法功率谱密度"""

import math
from typing import List, Optional


class WelchMethod:
    _instance: Optional["WelchMethod"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def psd(self, signal: List[float], nperseg: int = 256) -> List[float]:
        if len(signal) < nperseg:
            return []
        psd_values = []
        for i in range(0, len(signal) - nperseg, nperseg // 2):
            segment = signal[i:i+nperseg]
            psd_values.append(sum(x ** 2 for x in segment) / nperseg)
        return psd_values


def get_welch_method() -> WelchMethod:
    return WelchMethod()
