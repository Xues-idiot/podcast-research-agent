"""布隆过滤器"""

from typing import Any, Optional
import hashlib


class BloomFilter:
    _instance: Optional["BloomFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._bits = set()

    def add(self, item: Any) -> None:
        for i in range(3):
            h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            self._bits.add(int(h, 16) % 1000)

    def contains(self, item: Any) -> bool:
        for i in range(3):
            h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            if int(h, 16) % 1000 not in self._bits:
                return False
        return True

    def reset(self) -> None:
        self._bits.clear()


def get_bloom_filter() -> BloomFilter:
    return BloomFilter()
