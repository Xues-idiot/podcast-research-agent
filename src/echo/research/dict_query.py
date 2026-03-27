"""字典查询工具"""

from typing import Optional, Any


class DictQuerier:
    """字典查询工具"""

    def has_key(self, data: dict, key: str) -> bool:
        """是否有键"""
        return key in data

    def has_value(self, data: dict, value: Any) -> bool:
        """是否有值"""
        return value in data.values()

    def find_by_value(self, data: dict, value: Any) -> list:
        """按值查找键"""
        return [k for k, v in data.items() if v == value]


_querier: Optional[DictQuerier] = None


def get_dict_querier() -> DictQuerier:
    global _querier
    if _querier is None:
        _querier = DictQuerier()
    return _querier