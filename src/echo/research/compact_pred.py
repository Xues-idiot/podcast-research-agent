"""压缩工具"""

from typing import List, Any, Optional, Callable


class CompactPred:
    _instance: Optional["CompactPred"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compact(self, items: List[Any]) -> List[Any]:
        return [item for item in items if item]

    def compact_by(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if pred(item)]

    def is_empty(self, items: List[Any]) -> bool:
        return len(items) == 0


def get_compact_pred() -> CompactPred:
    return CompactPred()
