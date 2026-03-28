"""四元数工具"""

import math
from typing import List, Optional


class Quaternion:
    _instance: Optional["Quaternion"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def multiply(self, q1: List[float], q2: List[float]) -> List[float]:
        w1, x1, y1, z1 = q1
        w2, x2, y2, z2 = q2
        return [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
        ]

    def conjugate(self, q: List[float]) -> List[float]:
        return [q[0], -q[1], -q[2], -q[3]]

    def norm(self, q: List[float]) -> float:
        return math.sqrt(sum(x ** 2 for x in q))


def get_quaternion() -> Quaternion:
    return Quaternion()
