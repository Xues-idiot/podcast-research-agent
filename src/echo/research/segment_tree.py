"""线段树工具"""

from typing import Any, List, Optional


class SegmentTree:
    _instance: Optional["SegmentTree"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def build(self, arr: List[int]) -> List[int]:
        n = len(arr)
        size = 4 * n
        tree = [0] * size
        self._build_rec(tree, arr, 0, 0, n - 1)
        return tree

    def _build_rec(self, tree: List[int], arr: List[int], node: int, start: int, end: int) -> None:
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build_rec(tree, arr, 2 * node, start, mid)
            self._build_rec(tree, arr, 2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(self, tree: List[int], start: int, end: int, query_start: int, query_end: int) -> int:
        if query_end < start or query_start > end:
            return 0
        if query_start <= start and end <= query_end:
            return tree[start]
        mid = (start + end) // 2
        return self.query(tree, start, mid, query_start, query_end) + self.query(tree, mid + 1, end, query_start, query_end)


def get_segment_tree() -> SegmentTree:
    return SegmentTree()
