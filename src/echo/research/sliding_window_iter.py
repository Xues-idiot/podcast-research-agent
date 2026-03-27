"""滑动窗口迭代"""

from typing import Iterator, List, Any, Tuple


class SlidingWindowIter:
    _instance: Optional["SlidingWindowIter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def slide(self, items: List[Any], size: int, step: int = 1) -> Iterator[Tuple[Any, ...]]:
        for i in range(0, len(items) - size + 1, step):
            yield tuple(items[i:i+size])


def get_sliding_window_iter() -> SlidingWindowIter:
    return SlidingWindowIter()
