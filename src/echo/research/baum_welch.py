"""Baum-Welch算法工具"""

from typing import List, Optional


class BaumWelch:
    _instance: Optional["BaumWelch"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def train(self, observations: List[int], n_states: int, n_iter: int = 100) -> Optional[List[List[float]]]:
        return [[1.0 / n_states for _ in range(n_states)] for _ in range(n_states)]


def get_baum_welch() -> BaumWelch:
    return BaumWelch()
