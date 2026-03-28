"""椭圆曲线工具"""

from typing import Optional, Tuple


class EllipticCurve:
    _instance: Optional["EllipticCurve"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, p1: Tuple[float, float], p2: Tuple[float, float], a: float, b: float) -> Tuple[float, float]:
        if p1 == (0, 0):
            return p2
        if p2 == (0, 0):
            return p1
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2 and (y1 + y2) % 1 == 0:
            return (0, 0)
        if p1 != p2:
            lam = ((y2 - y1) / (x2 - x1)) % 1
        else:
            lam = ((3 * x1 ** 2 + a) / (2 * y1)) % 1
        x3 = (lam ** 2 - x1 - x2) % 1
        y3 = (lam * (x1 - x3) - y1) % 1
        return (x3, y3)


def get_elliptic_curve() -> EllipticCurve:
    return EllipticCurve()
