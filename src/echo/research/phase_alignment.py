"""相位对齐工具"""

from typing import List, Optional


class PhaseAlignment:
    _instance: Optional["PhaseAlignment"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def align(self, signal: List[float]) -> List[float]:
        return signal


def get_phase_alignment() -> PhaseAlignment:
    return PhaseAlignment()
