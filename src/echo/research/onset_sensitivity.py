"""onset敏感度工具"""

from typing import List, Optional


class OnsetSensitivity:
    _instance: Optional["OnsetSensitivity"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute_sensitivity(self, signal: List[float], threshold: float = 0.5) -> float:
        if not signal:
            return 0.0
        energy = sum(abs(s) ** 2 for s in signal) / len(signal)
        return energy * threshold


def get_onset_sensitivity() -> OnsetSensitivity:
    return OnsetSensitivity()
