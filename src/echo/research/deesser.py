"""去咝声器"""

from typing import List, Optional


class Deesser:
    _instance: Optional["Deesser"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def deess(self, signal: List[float], threshold: float = 0.5) -> List[float]:
        return signal


def get_deesser() -> Deesser:
    return Deesser()
