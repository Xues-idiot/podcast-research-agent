"""环绕声工具"""

from typing import List, Optional


class SurroundSound:
    _instance: Optional["SurroundSound"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_5_1(self, stereo: List[List[float]]) -> List[List[float]]:
        if not stereo:
            return []
        left = [s[0] for s in stereo]
        right = [s[1] for s in stereo]
        center = [(l + r) / 2 for l, r in zip(left, right)]
        lfe = [c * 0.1 for c in center]
        surround_left = [l * 0.7 for l in left]
        surround_right = [r * 0.7 for r in right]
        return [center, left, right, lfe, surround_left, surround_right]


def get_surround_sound() -> SurroundSound:
    return SurroundSound()
