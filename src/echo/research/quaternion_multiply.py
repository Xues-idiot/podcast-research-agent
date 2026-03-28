"""四元数乘法工具"""

import math
from typing import List, Optional


class QuaternionMultiplyTool:
    _instance: Optional["QuaternionMultiplyTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def multiply(self, q1: List[float], q2: List[float]) -> List[float]:
        if len(q1) != 4 or len(q2) != 4:
            return q1
        w1, x1, y1, z1 = q1
        w2, x2, y2, z2 = q2
        return [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
        ]


def get_quaternion_multiply_tool() -> QuaternionMultiplyTool:
    return QuaternionMultiplyTool()