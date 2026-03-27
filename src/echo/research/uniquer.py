"""去重工具"""

from typing import Optional, Any


class UniquerTool:
    """去重工具"""

    def unique(self, items: list) -> list:
        """去重"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def unique_by(self, items: list, key_func: Callable) -> list:
        """按键去重"""
        seen = set()
        result = []
        for item in items:
            key = key_func(item)
            if key not in seen:
                seen.add(key)
                result.append(item)
        return result


_uniquer: Optional[UniquerTool] = None


def get_uniquer_tool() -> UniquerTool:
    global _uniquer
    if _uniquer is None:
        _uniquer = UniquerTool()
    return _uniquer