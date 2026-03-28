"""Zip最长工具"""

import itertools
from typing import List, Any, Optional


class ZipLongestTool:
    _instance: Optional["ZipLongestTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_longest(self, *lists: List[Any], fillvalue: Any = None) -> List[tuple]:
        return list(itertools.zip_longest(*lists, fillvalue=fillvalue))


def get_zip_longest_tool() -> ZipLongestTool:
    return ZipLongestTool()