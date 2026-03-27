"""LRU缓存工具"""

from typing import Any, Optional, Dict
from collections import OrderedDict


class LRUCache:
    _instance: Optional["LRUCache"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_cache"):
            self._cache: OrderedDict = OrderedDict()
            self._max_size: int = 100

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key: str, value: Any) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._max_size:
            self._cache.popitem(last=False)


def get_lru_cache() -> LRUCache:
    return LRUCache()
