"""比较工具集合"""
from typing import Any, List, Tuple


def compare(a: Any, b: Any) -> int:
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def min_val(*values: Any) -> Any:
    return min(values)


def max_val(*values: Any) -> Any:
    return max(values)


def clamp(value: Any, min_val: Any, max_val: Any) -> Any:
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


def between(value: Any, min_val: Any, max_val: Any) -> bool:
    return min_val <= value <= max_val


def equal(a: Any, b: Any) -> bool:
    return a == b


def not_equal(a: Any, b: Any) -> bool:
    return a != b


def greater_than(a: Any, b: Any) -> bool:
    return a > b


def less_than(a: Any, b: Any) -> bool:
    return a < b


def greater_or_equal(a: Any, b: Any) -> bool:
    return a >= b


def less_or_equal(a: Any, b: Any) -> bool:
    return a <= b


def in_list(value: Any, lst: List[Any]) -> bool:
    return value in lst


def not_in_list(value: Any, lst: List[Any]) -> bool:
    return value not in lst


def is_between(value: Any, start: Any, end: Any) -> bool:
    return start <= value <= end
