"""带索引压缩"""

from typing import List, Any, Tuple


class ZipWithIndex:
    _instance: Optional["ZipWithIndex"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def zip_with_index(self, items: List[Any], start: int = 0) -> List[Tuple[int, Any]]:
        return [(i + start, item) for i, item in enumerate(items)]


def get_zip_with_index() -> ZipWithIndex:
    return ZipWithIndex()
