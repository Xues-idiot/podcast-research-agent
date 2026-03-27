"""字典映射工具"""

from typing import Optional, Any


class DictMapper:
    """字典映射工具"""

    def map_keys(self, data: dict, key_map: dict) -> dict:
        """映射键名"""
        return {key_map.get(k, k): v for k, v in data.items()}

    def map_values(self, data: dict, value_map: dict) -> dict:
        """映射键值"""
        return {k: value_map.get(v, v) for k, v in data.items()}

    def invert(self, data: dict) -> dict:
        """反转字典"""
        return {v: k for k, v in data.items()}


_mapper: Optional[DictMapper] = None


def get_dict_mapper() -> DictMapper:
    global _mapper
    if _mapper is None:
        _mapper = DictMapper()
    return _mapper