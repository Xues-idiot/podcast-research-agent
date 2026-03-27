"""傅里叶变换工具"""

import math
from typing import List, Optional, Tuple


class FourierTransform:
    _instance: Optional["FourierTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def dft(self, signal: List[float]) -> List[Tuple[float, float]]:
        n = len(signal)
        result = []
        for k in range(n):
            real = sum(signal[n] * math.cos(2 * math.pi * k * n / n) for n in range(n))
            imag = -sum(signal[n] * math.sin(2 * math.pi * k * n / n) for n in range(n))
            result.append((real, imag))
        return result


def get_fourier_transform() -> FourierTransform:
    return FourierTransform()
