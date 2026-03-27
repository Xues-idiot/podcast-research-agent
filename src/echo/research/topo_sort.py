"""拓扑排序工具"""

from typing import Any, Dict, List, Optional, Set


class TopoSort:
    _instance: Optional["TopoSort"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sort(self, graph: Dict[Any, List[Any]]) -> List[Any]:
        in_degree = {v: 0 for v in graph}
        for u in graph:
            for v in graph[u]:
                in_degree[v] = in_degree.get(v, 0) + 1

        queue = [v for v in in_degree if in_degree[v] == 0]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in graph.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result


def get_topo_sort() -> TopoSort:
    return TopoSort()
