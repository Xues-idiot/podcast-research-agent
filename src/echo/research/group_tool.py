"""分组工具"""

from typing import List, Any, Optional, Callable, Dict


class GroupTool:
    _instance: Optional["GroupTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def group_by(self, items: List[Any], key: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
        """按键分组"""
        groups: Dict[Any, List[Any]] = {}
        for item in items:
            k = key(item)
            if k not in groups:
                groups[k] = []
            groups[k].append(item)
        return groups

    def group_by_field(self, items: List[dict], field: str) -> Dict[Any, List[dict]]:
        """按字段分组"""
        return self.group_by(items, lambda x: x.get(field))

    def chunk(self, items: List[Any], size: int) -> List[List[Any]]:
        """分块"""
        return [items[i:i + size] for i in range(0, len(items), size)]

    def window(self, items: List[Any], size: int, step: int = 1) -> List[List[Any]]:
        """滑动窗口"""
        return [items[i:i + size] for i in range(0, len(items) - size + 1, step)]

    def partition(self, items: List[Any], predicate: Callable[[Any], bool]) -> tuple:
        """分区"""
        matched = []
        not_matched = []
        for item in items:
            if predicate(item):
                matched.append(item)
            else:
                not_matched.append(item)
        return (matched, not_matched)


_group_instance: Optional[GroupTool] = None


def get_group_tool() -> GroupTool:
    global _group_instance
    if _group_instance is None:
        _group_instance = GroupTool()
    return _group_instance