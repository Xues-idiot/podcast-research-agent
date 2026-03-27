"""最大流工具"""

from typing import Any, Dict, List, Optional


class MaxFlow:
    _instance: Optional["MaxFlow"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bfs(self, graph: Dict, start: Any, end: Any, parent: Dict) -> bool:
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            u = queue.pop(0)
            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    if v == end:
                        return True
                    queue.append(v)
        return False

    def max_flow(self, graph: Dict[Any, List[Any]], source: Any, sink: Any) -> int:
        parent = {}
        flow = 0
        while self.bfs(graph, source, sink, parent):
            path = []
            v = sink
            while v != source:
                path.append(v)
                v = parent[v]
            path.append(source)
            flow += 1
        return flow


def get_max_flow() -> MaxFlow:
    return MaxFlow()
