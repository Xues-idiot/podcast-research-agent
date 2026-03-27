"""字典过滤工具"""

from typing import Optional, Any, Callable


class DictFilter:
    """字典过滤工具"""

    def filter_keys(self, data: dict, keys: list) -> dict:
        """保留指定键"""
        return {k: v for k, v in data.items() if k in keys}

    def exclude_keys(self, data: dict, keys: list) -> dict:
        """排除指定键"""
        return {k: v for k, v in data.items() if k not in keys}

    def filter_by_value(self, data: dict, predicate: Callable) -> dict:
        """按值过滤"""
        return {k: v for k, v in data.items() if predicate(v)}


_filter: Optional[DictFilter] = None


def get_dict_filter() -> DictFilter:
    global _filter
    if _filter is None:
        _filter = DictFilter()
    return _filter