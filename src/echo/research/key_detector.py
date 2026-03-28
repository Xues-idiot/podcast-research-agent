"""调性检测器"""

from typing import List, Optional


class KeyDetector:
    _instance: Optional["KeyDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect_key(self, chroma: List[float]) -> str:
        keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        major_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        minor_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
        if not chroma:
            return "C"
        max_idx = chroma.index(max(chroma))
        return keys[max_idx]


def get_key_detector() -> KeyDetector:
    return KeyDetector()
