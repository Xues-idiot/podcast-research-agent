"""LRU缓存工具"""

from typing import Any, Optional
from collections import OrderedDict


class LRUCache:
    _instance: Optional["LRUCache"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, capacity: int = 100) -> OrderedDict:
        return OrderedDict()

    def get(self, cache: OrderedDict, key: Any) -> Any:
        if key in cache:
            cache.move_to_end(key)
            return cache[key]
        return None

    def put(self, cache: OrderedDict, key: Any, value: Any, capacity: int = 100) -> None:
        if key in cache:
            cache.move_to_end(key)
        cache[key] = value
        if len(cache) > capacity:
            cache.popitem(last=False)


def get_lru_cache() -> LRUCache:
    return LRUCache()
