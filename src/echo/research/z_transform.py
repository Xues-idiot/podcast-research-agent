"""Z变换工具"""

from typing import Callable, Optional


class ZTransform:
    _instance: Optional["ZTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def z_transform(self, func: Callable, z: float) -> Optional[complex]:
        try:
            return complex(func(z))
        except:
            return None


def get_z_transform() -> ZTransform:
    return ZTransform()
