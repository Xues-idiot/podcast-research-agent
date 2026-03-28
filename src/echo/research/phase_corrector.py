"""相位校正工具"""

from typing import List, Optional


class PhaseCorrector:
    _instance: Optional["PhaseCorrector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def correct(self, signal: List[float]) -> List[float]:
        return signal


def get_phase_corrector() -> PhaseCorrector:
    return PhaseCorrector()
