"""树状数组工具"""

from typing import Any, List, Optional


class FenwickTree:
    _instance: Optional["FenwickTree"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, size: int) -> List[int]:
        return [0] * (size + 1)

    def update(self, tree: List[int], index: int, delta: int) -> None:
        n = len(tree) - 1
        while index <= n:
            tree[index] += delta
            index += index & (-index)

    def prefix_sum(self, tree: List[int], index: int) -> int:
        result = 0
        while index > 0:
            result += tree[index]
            index -= index & (-index)
        return result


def get_fenwick_tree() -> FenwickTree:
    return FenwickTree()
