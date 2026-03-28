"""和弦创建器"""

from typing import List, Optional


class ChordCreator:
    _instance: Optional["ChordCreator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_chord(self, root: float, chord_type: str) -> List[float]:
        intervals = {
            "major": [0, 4, 7],
            "minor": [0, 3, 7],
            "diminished": [0, 3, 6],
            "augmented": [0, 4, 8],
            "sus2": [0, 2, 7],
            "sus4": [0, 5, 7]
        }
        return [root * (2 ** (i / 12)) for i in intervals.get(chord_type, [0, 4, 7])]


def get_chord_creator() -> ChordCreator:
    return ChordCreator()
