"""Kruskal最小生成树工具"""

from typing import Any, List, Optional, Tuple


class Kruskal:
    _instance: Optional["Kruskal"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mst(self, vertices: List[Any], edges: List[Tuple[Any, Any, int]]) -> List[Tuple[Any, Any, int]]:
        edges = sorted(edges, key=lambda x: x[2])
        parent = {v: v for v in vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        result = []
        for u, v, w in edges:
            if find(u) != find(v):
                result.append((u, v, w))
                parent[find(u)] = find(v)
        return result


def get_kruskal() -> Kruskal:
    return Kruskal()
