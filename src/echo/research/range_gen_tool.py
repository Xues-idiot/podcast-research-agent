"""范围生成工具"""

from typing import Optional


class RangeGenTool:
    """范围生成工具"""

    def range_int(self, start: int, stop: int, step: int = 1) -> list:
        """整数范围"""
        return list(range(start, stop, step))

    def range_float(self, start: float, stop: float, step: float) -> list:
        """浮点范围"""
        result = []
        current = start
        while current < stop:
            result.append(current)
            current += step
        return result


_gen: Optional[RangeGenTool] = None


def get_range_gen_tool() -> RangeGenTool:
    global _gen
    if _gen is None:
        _gen = RangeGenTool()
    return _gen