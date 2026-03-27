"""3D线性插值"""

from typing import Optional, Tuple


class Lerp3D:
    _instance: Optional["Lerp3D"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def lerp_3d(self, a: Tuple[float, float, float], b: Tuple[float, float, float], t: float) -> Tuple[float, float, float]:
        return (
            a[0] + (b[0] - a[0]) * t,
            a[1] + (b[1] - a[1]) * t,
            a[2] + (b[2] - a[2]) * t,
        )


def get_lerp_3d() -> Lerp3D:
    return Lerp3D()
