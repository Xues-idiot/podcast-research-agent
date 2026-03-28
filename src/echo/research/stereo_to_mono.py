"""立体声转单声道工具"""

from typing import List, Optional


class StereoToMono:
    _instance: Optional["StereoToMono"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, stereo: List[List[float]]) -> List[float]:
        if not stereo or len(stereo[0]) < 2:
            return []
        return [(stereo[i][0] + stereo[i][1]) / 2 for i in range(len(stereo))]


def get_stereo_to_mono() -> StereoToMono:
    return StereoToMono()
