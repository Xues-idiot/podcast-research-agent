"""学生t分布计算器"""

import math
from typing import Optional


class StudentT:
    _instance: Optional["StudentT"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, t: float, df: int) -> float:
        if df <= 0:
            return 0.0
        coef = math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2))
        return coef * (1 + t ** 2 / df) ** (-(df + 1) / 2)


def get_student_t() -> StudentT:
    return StudentT()
