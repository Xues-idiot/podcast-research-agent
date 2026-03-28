"""宽高比计算工具"""

from typing import Optional, Tuple


class AspectRatioTool:
    _instance: Optional["AspectRatioTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate(self, width: int, height: int) -> Tuple[int, int]:
        if width <= 0 or height <= 0:
            return 1, 1
        gcd = self._gcd(width, height)
        return width // gcd, height // gcd

    def ratio_to_string(self, width: int, height: int) -> str:
        w, h = self.calculate(width, height)
        return f"{w}:{h}"

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


def get_aspect_ratio_tool() -> AspectRatioTool:
    return AspectRatioTool()