"""噪声门"""

from typing import Optional


class NoiseGate:
    _instance: Optional["NoiseGate"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gate(self, signal: list[float], threshold: float = 0.01) -> list[float]:
        return [0.0 if abs(sample) < threshold else sample for sample in signal]


def get_noise_gate() -> NoiseGate:
    return NoiseGate()
