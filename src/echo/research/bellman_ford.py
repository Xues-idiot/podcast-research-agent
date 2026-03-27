"""Bellman-Ford最短路径工具"""

from typing import Any, Dict, List, Optional, Tuple


class BellmanFord:
    _instance: Optional["BellmanFord"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shortest_path(self, vertices: List[Any], edges: List[Tuple[Any, Any, int]], start: Any) -> Dict[Any, int]:
        distances = {v: float("inf") for v in vertices}
        distances[start] = 0

        for _ in range(len(vertices) - 1):
            for u, v, w in edges:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        return distances


def get_bellman_ford() -> BellmanFord:
    return BellmanFord()
