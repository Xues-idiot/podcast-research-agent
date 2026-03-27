"""Lomb-Scargle周期图"""

import math
from typing import List, Optional


class LombScargle:
    _instance: Optional["LombScargle"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def periodogram(self, t: List[float], y: List[float], frequencies: List[float]) -> List[float]:
        if len(t) != len(y) or len(t) == 0:
            return []
        n = len(t)
        mean_y = sum(y) / n
        normalized_y = [yi - mean_y for yi in y]
        powers = []
        for freq in frequencies:
            tau = 0.0
            theta = 2 * math.pi * freq
            cos_theta_t = sum(math.cos(theta * ti) for ti in t) / n
            sin_theta_t = sum(math.sin(theta * ti) for ti in t) / n
            power = 0.0
            for i in range(n):
                phi = theta * t[i] - tau
                power += normalized_y[i] * math.cos(phi)
            powers.append(power ** 2)
        return powers


def get_lomb_scargle() -> LombScargle:
    return LombScargle()
