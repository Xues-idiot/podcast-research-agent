"""琶音器"""

from typing import List, Optional


class Arpeggiator:
    _instance: Optional["Arpeggiator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def arpeggiate(self, notes: List[float], pattern: str = "up") -> List[float]:
        if pattern == "up":
            return sorted(notes)
        elif pattern == "down":
            return sorted(notes, reverse=True)
        return notes


def get_arpeggiator() -> Arpeggiator:
    return Arpeggiator()
