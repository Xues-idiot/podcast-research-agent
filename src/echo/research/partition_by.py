"""分区工具"""

from typing import List, Any, Callable, Optional, Tuple


class PartitionBy:
    _instance: Optional["PartitionBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def partition_by(self, items: List[Any], pred: Callable) -> Tuple[List[Any], List[Any]]:
        true_items = []
        false_items = []
        for item in items:
            if pred(item):
                true_items.append(item)
            else:
                false_items.append(item)
        return true_items, false_items

    def partition_at(self, items: List[Any], index: int) -> Tuple[List[Any], List[Any]]:
        return items[:index], items[index:]


def get_partition_by() -> PartitionBy:
    return PartitionBy()
