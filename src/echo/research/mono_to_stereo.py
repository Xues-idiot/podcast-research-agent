"""单声道转立体声工具"""

from typing import List, Optional


class MonoToStereo:
    _instance: Optional["MonoToStereo"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, mono: List[float]) -> List[List[float]]:
        return [[s, s] for s in mono]


def get_mono_to_stereo() -> MonoToStereo:
    return MonoToStereo()
