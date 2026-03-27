"""字典构建工具"""

from typing import Optional, Any


class DictBuilder:
    """字典构建工具"""

    def build(self, **kwargs) -> dict:
        """构建字典"""
        return kwargs

    def from_keys(self, keys: list, value: Any = None) -> dict:
        """从键构建"""
        return {k: value for k in keys}


_builder: Optional[DictBuilder] = None


def get_dict_builder() -> DictBuilder:
    global _builder
    if _builder is None:
        _builder = DictBuilder()
    return _builder