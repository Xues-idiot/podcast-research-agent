"""扫描累加器"""

from typing import Any, Callable, List, Optional, TypeVar


T = TypeVar("T")


class ScanAccumulator:
    _instance: Optional["ScanAccumulator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scan(self, items: List[T], func: Callable[[Any, T], Any], initial: Any = None) -> List[Any]:
        results = []
        accumulator = initial
        for item in items:
            accumulator = func(accumulator, item)
            results.append(accumulator)
        return results

    def scan_left(self, items: List[T], func: Callable[[Any, T], Any], initial: Any) -> List[Any]:
        return self.scan(items, func, initial)


def get_scan_accumulator() -> ScanAccumulator:
    return ScanAccumulator()
