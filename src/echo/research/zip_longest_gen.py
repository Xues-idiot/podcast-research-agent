"""zip最长工具"""

from typing import Any, Iterator, List, Optional
from itertools import zip_longest


class ZipLongestTool:
    _instance: Optional["ZipLongestTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_longest(self, *iterables: List[Any], fillvalue: Any = None) -> Iterator[tuple]:
        return zip_longest(*iterables, fillvalue=fillvalue)

    def zip_equal(self, *iterables: List[Any]) -> Iterator[tuple]:
        return zip(*iterables)


def get_zip_longest_tool() -> ZipLongestTool:
    return ZipLongestTool()
