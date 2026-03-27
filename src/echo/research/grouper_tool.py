"""分组工具"""

from typing import Optional, Callable, Any


class GroupTool:
    """分组工具"""

    def group_by(self, items: list, key_func: Callable) -> dict:
        """按键分组"""
        result = {}
        for item in items:
            key = key_func(item)
            if key not in result:
                result[key] = []
            result[key].append(item)
        return result

    def partition(self, items: list, predicate: Callable) -> tuple:
        """分区"""
        group_a = []
        group_b = []
        for item in items:
            if predicate(item):
                group_a.append(item)
            else:
                group_b.append(item)
        return (group_a, group_b)


_grouper: Optional[GroupTool] = None


def get_grouper_tool() -> GroupTool:
    global _grouper
    if _grouper is None:
        _grouper = GroupTool()
    return _grouper