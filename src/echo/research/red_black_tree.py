"""红黑树工具"""

from typing import Any, Optional


class RBNode:
    def __init__(self, value: Any, color: str = "RED"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    _instance: Optional["RedBlackTree"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_node(self, value: Any) -> RBNode:
        return RBNode(value)

    def is_red(self, node: RBNode) -> bool:
        return node.color == "RED" if node else False

    def is_black(self, node: RBNode) -> bool:
        return node.color == "BLACK" if node else False


def get_red_black_tree() -> RedBlackTree:
    return RedBlackTree()
