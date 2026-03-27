"""拒绝工具"""

from typing import List, Any, Callable


class RejectBy:
    _instance: Optional["RejectBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reject(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if not pred(item)]


def get_reject_by() -> RejectBy:
    return RejectBy()
