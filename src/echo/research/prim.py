"""Prim最小生成树工具"""

from typing import Any, Dict, List, Optional, Tuple
import heapq


class Prim:
    _instance: Optional["Prim"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mst(self, graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> List[Tuple[Any, Any, int]]:
        visited = {start}
        edges = [(w, start, v) for v, w in graph.get(start, [])]
        heapq.heapify(edges)
        result = []

        while edges and len(visited) < len(graph):
            w, u, v = heapq.heappop(edges)
            if v in visited:
                continue
            visited.add(v)
            result.append((u, v, w))
            for next_v, next_w in graph.get(v, []):
                if next_v not in visited:
                    heapq.heappush(edges, (next_w, v, next_v))
        return result


def get_prim() -> Prim:
    return Prim()
