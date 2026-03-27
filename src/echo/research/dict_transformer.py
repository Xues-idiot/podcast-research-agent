"""字典转换工具"""

from typing import Optional, Any, Callable


class DictTransformer:
    """字典转换工具"""

    def map_keys(self, data: dict, func: Callable) -> dict:
        """映射键"""
        return {func(k): v for k, v in data.items()}

    def map_values(self, data: dict, func: Callable) -> dict:
        """映射值"""
        return {k: func(v) for k, v in data.items()}

    def invert(self, data: dict) -> dict:
        """反转字典"""
        return {v: k for k, v in data.items()}


_transformer: Optional[DictTransformer] = None


def get_dict_transformer() -> DictTransformer:
    global _transformer
    if _transformer is None:
        _transformer = DictTransformer()
    return _transformer