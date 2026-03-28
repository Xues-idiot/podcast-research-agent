"""立体声扩展工具"""

from typing import List, Optional


class StereoWidener:
    _instance: Optional["StereoWidener"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def widen(self, stereo: List[List[float]], width: float = 1.5) -> List[List[float]]:
        if not stereo or len(stereo[0]) < 2:
            return stereo
        left = [stereo[i][0] for i in range(len(stereo))]
        right = [stereo[i][1] for i in range(len(stereo))]
        mid = [(l + r) / 2 for l, r in zip(left, right)]
        side = [(l - r) / 2 for l, r in zip(left, right)]
        new_left = [m + s * width for m, s in zip(mid, side)]
        new_right = [m - s * width for m, s in zip(mid, side)]
        return [[new_left[i], new_right[i]] for i in range(len(new_left))]


def get_stereo_widener() -> StereoWidener:
    return StereoWidener()
