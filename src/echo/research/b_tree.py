"""B树工具"""

from typing import Any, List, Optional


class BNode:
    def __init__(self, keys: List[Any] = None, children: List["BNode"] = None, leaf: bool = True):
        self.keys = keys or []
        self.children = children or []
        self.leaf = leaf


class BTreeTool:
    _instance: Optional["BTreeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_node(self, leaf: bool = True) -> BNode:
        return BNode([], [], leaf)

    def search(self, node: BNode, key: Any) -> bool:
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self.search(node.children[i], key)


def get_b_tree_tool() -> BTreeTool:
    return BTreeTool()
