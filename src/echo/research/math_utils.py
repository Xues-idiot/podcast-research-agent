"""数学工具集合"""
from typing import Any, List, Union
from dataclasses import dataclass
import math


@dataclass
class MathResult:
    result: float
    exact: bool


def math_add(a: Union[int, float], b: Union[int, float]) -> float:
    return a + b


def math_subtract(a: Union[int, float], b: Union[int, float]) -> float:
    return a - b


def math_multiply(a: Union[int, float], b: Union[int, float]) -> float:
    return a * b


def math_divide(a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
    if b == 0:
        return "division by zero"
    return a / b


def math_power(a: Union[int, float], b: Union[int, float]) -> float:
    return a ** b


def math_sqrt(a: Union[int, float]) -> float:
    return math.sqrt(a) if a >= 0 else "invalid input"


def math_abs(a: Union[int, float]) -> float:
    return abs(a)


def math_floor(a: float) -> int:
    return math.floor(a)


def math_ceil(a: float) -> int:
    return math.ceil(a)


def math_round(a: float, n: int = 0) -> Union[float, int]:
    return round(a, n)


def math_factorial(n: int) -> int:
    if n < 0:
        return "invalid input"
    return math.factorial(n) if n <= 170 else "too large"


def math_gcd(*nums: int) -> int:
    from math import gcd as math_gcd
    result = nums[0]
    for n in nums[1:]:
        result = math_gcd(result, n)
    return result


def math_lcm(*nums: int) -> int:
    from math import gcd
    if not nums:
        return 1
    result = nums[0]
    for n in nums[1:]:
        result = result * n // gcd(result, n)
    return result

