"""压缩工具"""

from typing import List, Any, Optional, Tuple


class ZipItemsTool:
    _instance: Optional["ZipItemsTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_lists(self, *lists: List[Any]) -> List[Tuple]:
        """压缩多个列表"""
        return list(zip(*lists))

    def unzip_pairs(self, pairs: List[Tuple]) -> Tuple:
        """解压缩为元组列表"""
        return list(zip(*pairs))

    def zip_longest_fill(self, *lists: List[Any], fillvalue: Any = None) -> List[Tuple]:
        """最长压缩(不足填充)"""
        from itertools import zip_longest
        return list(zip_longest(*lists, fillvalue=fillvalue))

    def dict_from_tuples(self, tuples: List[Tuple]) -> dict:
        """元组列表转字典"""
        return dict(tuples)


_zip_instance: Optional[ZipItemsTool] = None


def get_zip_items_tool() -> ZipItemsTool:
    global _zip_instance
    if _zip_instance is None:
        _zip_instance = ZipItemsTool()
    return _zip_instance