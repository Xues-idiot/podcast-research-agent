"""最大公约数计算器"""

from typing import Optional
import math


class GcdCalculator:
    _instance: Optional["GcdCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gcd(self, a: int, b: int) -> int:
        return math.gcd(a, b)

    def gcd_multiple(self, *numbers: int) -> int:
        if not numbers:
            return 0
        result = numbers[0]
        for num in numbers[1:]:
            result = math.gcd(result, num)
        return result

    def lcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)


def get_gcd_calculator() -> GcdCalculator:
    return GcdCalculator()
