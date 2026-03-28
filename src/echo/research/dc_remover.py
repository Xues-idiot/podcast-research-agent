"""直流移除器"""

from typing import List, Optional


class DcRemover:
    _instance: Optional["DcRemover"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def remove(self, signal: List[float]) -> List[float]:
        if not signal:
            return signal
        avg = sum(signal) / len(signal)
        return [s - avg for s in signal]


def get_dc_remover() -> DcRemover:
    return DcRemover()
