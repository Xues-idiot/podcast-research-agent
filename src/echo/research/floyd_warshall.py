"""Floyd-Warshall最短路径工具"""

from typing import Any, Dict, List, Optional


class FloydWarshall:
    _instance: Optional["FloydWarshall"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def all_pairs_shortest(self, vertices: List[Any], edges: List[Tuple[Any, Any, int]]) -> Dict[Any, Dict[Any, int]]:
        dist = {v: {u: float("inf") for u in vertices} for v in vertices}
        for v in vertices:
            dist[v][v] = 0
        for u, v, w in edges:
            dist[u][v] = w

        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist


def get_floyd_warshall() -> FloydWarshall:
    return FloydWarshall()
