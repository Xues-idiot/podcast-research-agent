"""并查集工具"""

from typing import Any, Dict, Optional


class DisjointSet:
    _instance: Optional["DisjointSet"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, items: List[Any]) -> Dict[Any, Any]:
        return {item: item for item in items}

    def find(self, parent: Dict, x: Any) -> Any:
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent: Dict, x: Any, y: Any) -> None:
        px = self.find(parent, x)
        py = self.find(parent, y)
        if px != py:
            parent[px] = py


def get_disjoint_set() -> DisjointSet:
    return DisjointSet()
