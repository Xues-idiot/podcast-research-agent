"""AVL树工具"""

from typing import Any, Optional


class AVLNode:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTool:
    _instance: Optional["AVLTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def height(self, node: AVLNode) -> int:
        return node.height if node else 0

    def balance(self, node: AVLNode) -> int:
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x


def get_avl_tool() -> AVLTool:
    return AVLTool()
