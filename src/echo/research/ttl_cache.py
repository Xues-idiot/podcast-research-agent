"""TTL缓存工具"""

import time
from typing import Any, Optional, Dict, Tuple


class TTLCache:
    _instance: Optional["TTLCache"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_cache"):
            self._cache: Dict[str, Tuple[Any, float]] = {}
            self._ttl: int = 300

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        value, expiry = self._cache[key]
        if time.time() > expiry:
            del self._cache[key]
            return None
        return value

    def put(self, key: str, value: Any, ttl: int = 300) -> None:
        self._cache[key] = (value, time.time() + ttl)


def get_ttl_cache() -> TTLCache:
    return TTLCache()
