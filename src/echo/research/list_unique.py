"""列表去重工具"""

from typing import Optional, Any


class ListUnique:
    """列表去重工具"""

    def unique(self, items: list) -> list:
        """去重保持顺序"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def unique_by(self, items: list, key: str) -> list:
        """按键去重"""
        seen = set()
        result = []
        for item in items:
            if isinstance(item, dict):
                k = item.get(key)
            else:
                k = getattr(item, key, None)
            if k not in seen:
                seen.add(k)
                result.append(item)
        return result


_unique: Optional[ListUnique] = None


def get_list_unique() -> ListUnique:
    global _unique
    if _unique is None:
        _unique = ListUnique()
    return _unique