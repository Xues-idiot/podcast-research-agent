"""哈希表工具"""

from typing import Any, Dict, List, Optional, Tuple


class HashTable:
    _instance: Optional["HashTable"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, size: int = 100) -> List[List[Tuple]]:
        return [[] for _ in range(size)]

    def hash(self, key: Any, size: int) -> int:
        return hash(key) % size

    def put(self, table: List[List[Tuple]], key: Any, value: Any) -> None:
        index = self.hash(key, len(table))
        bucket = table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, table: List[List[Tuple]], key: Any) -> Any:
        index = self.hash(key, len(table))
        bucket = table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None


def get_hash_table() -> HashTable:
    return HashTable()
