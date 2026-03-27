"""谓词分组工具"""

from typing import List, Any, Callable, Optional, Dict


class GroupPred:
    _instance: Optional["GroupPred"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def group_by_pred(self, items: List[Any], pred: Callable) -> Dict[bool, List[Any]]:
        result: Dict[bool, List[Any]] = {True: [], False: []}
        for item in items:
            key = pred(item)
            result[key].append(item)
        return result

    def group_where(self, items: List[Any], pred: Callable) -> List[Any]:
        return [item for item in items if pred(item)]


def get_group_pred() -> GroupPred:
    return GroupPred()
