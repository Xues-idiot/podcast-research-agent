"""分组工具"""

from typing import Optional, Any


class Grouper:
    """分组工具"""

    def group_by(self, items: list, key: str) -> dict:
        """按键分组"""
        result = {}
        for item in items:
            if isinstance(item, dict):
                group_key = item.get(key, 'unknown')
                if group_key not in result:
                    result[group_key] = []
                result[group_key].append(item)
        return result

    def chunk(self, items: list, size: int) -> list:
        """分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]

    def partition(self, items: list, predicate) -> tuple:
        """分区"""
        true_items = []
        false_items = []
        for item in items:
            if predicate(item):
                true_items.append(item)
            else:
                false_items.append(item)
        return (true_items, false_items)


_grouper: Optional[Grouper] = None


def get_grouper() -> Grouper:
    global _grouper
    if _grouper is None:
        _grouper = Grouper()
    return _grouper