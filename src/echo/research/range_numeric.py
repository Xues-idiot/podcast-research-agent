"""数字范围工具"""

from typing import List, Any, Optional


class RangeNumeric:
    _instance: Optional["RangeNumeric"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def range(self, start: int, end: int, step: int = 1) -> List[int]:
        if step == 0:
            return []
        return list(range(start, end, step))

    def range_to(self, end: int) -> List[int]:
        return list(range(end))

    def range_from_to(self, start: int, end: int) -> List[int]:
        return list(range(start, end))

    def inclusive_range(self, start: int, end: int, step: int = 1) -> List[int]:
        return list(range(start, end + 1, step))


def get_range_numeric() -> RangeNumeric:
    return RangeNumeric()
