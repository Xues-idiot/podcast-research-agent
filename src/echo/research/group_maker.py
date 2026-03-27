"""分组工具"""

from typing import Optional, List, Any


class GroupMaker:
    """分组工具"""

    def group_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        """按大小分组"""
        return [items[i:i + size] for i in range(0, len(items), size)]

    def group_by_key(self, items: List[dict], key: str) -> dict:
        """按键分组"""
        result = {}
        for item in items:
            k = item.get(key)
            if k not in result:
                result[k] = []
            result[k].append(item)
        return result


_group_maker: Optional[GroupMaker] = None


def get_group_maker() -> GroupMaker:
    global _group_maker
    if _group_maker is None:
        _group_maker = GroupMaker()
    return _group_maker