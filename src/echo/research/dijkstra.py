"""Dijkstra最短路径工具"""

from typing import Any, Dict, List, Optional, Tuple
import heapq


class Dijkstra:
    _instance: Optional["Dijkstra"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shortest_path(self, graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Dict[Any, int]:
        distances = {v: float("inf") for v in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, weight in graph.get(node, []):
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return distances


def get_dijkstra() -> Dijkstra:
    return Dijkstra()
