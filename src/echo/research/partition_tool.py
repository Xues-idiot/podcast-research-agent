"""分区工具"""

from typing import List, Any, Tuple


class PartitionTool:
    _instance: Optional["PartitionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def partition(self, items: List[Any], pred: callable) -> Tuple[List[Any], List[Any]]:
        true_list = []
        false_list = []
        for item in items:
            if pred(item):
                true_list.append(item)
            else:
                false_list.append(item)
        return (true_list, false_list)


def get_partition_tool() -> PartitionTool:
    return PartitionTool()
