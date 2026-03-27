"""范围生成工具"""

from typing import Optional, Any


class RangeGen:
    """范围生成工具"""

    def range_int(self, start: int, end: int, step: int = 1) -> list:
        """整数范围"""
        return list(range(start, end, step))

    def range_float(self, start: float, end: float, step: float) -> list:
        """浮点范围"""
        result = []
        current = start
        while current < end:
            result.append(round(current, 10))
            current += step
        return result


_gen: Optional[RangeGen] = None


def get_range_gen() -> RangeGen:
    global _gen
    if _gen is None:
        _gen = RangeGen()
    return _gen