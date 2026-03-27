"""Bucket tool for bucketing items"""

from typing import Any, Callable, Dict, Hashable, List, Optional


class BucketTool:
    _instance: Optional["BucketTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bucket_by_key(self, items: List[Any], key_func: Callable[[Any], Hashable]) -> Dict[Hashable, List[Any]]:
        """Bucket items by a key function"""
        buckets: Dict[Hashable, List[Any]] = {}
        for item in items:
            key = key_func(item)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(item)
        return buckets

    def bucket_by_range(self, items: List[float], num_buckets: int) -> Dict[int, List[float]]:
        """Bucket numeric items into ranges"""
        if not items:
            return {}
        min_val, max_val = min(items), max(items)
        if min_val == max_val:
            return {0: items}
        bucket_size = (max_val - min_val) / num_buckets
        buckets: Dict[int, List[float]] = {i: [] for i in range(num_buckets)}
        for item in items:
            bucket_idx = min(int((item - min_val) / bucket_size), num_buckets - 1)
            buckets[bucket_idx].append(item)
        return buckets

    def bucket_by_size(self, items: List[Any], bucket_size: int) -> List[List[Any]]:
        """Bucket items into groups of fixed size"""
        buckets = []
        for i in range(0, len(items), bucket_size):
            buckets.append(items[i:i + bucket_size])
        return buckets

    def bucket_evenly(self, items: List[Any], num_buckets: int) -> List[List[Any]]:
        """Distribute items evenly across buckets"""
        if num_buckets <= 0:
            return []
        buckets: List[List[Any]] = [[] for _ in range(num_buckets)]
        for i, item in enumerate(items):
            buckets[i % num_buckets].append(item)
        return buckets

    def process(self, data: Any) -> Any:
        """Process data by bucketing"""
        return data


def get_bucket_tool() -> BucketTool:
    return BucketTool()