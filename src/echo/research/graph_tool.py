"""图工具"""

from typing import Any, Dict, List, Optional, Set


class GraphTool:
    _instance: Optional["GraphTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bfs(self, graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
        visited: Set = set()
        queue = [start]
        result = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(graph.get(node, []))
        return result

    def dfs(self, graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
        visited: Set = set()
        result = []
        def dfs_rec(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                dfs_rec(neighbor)
        dfs_rec(start)
        return result


def get_graph_tool() -> GraphTool:
    return GraphTool()
