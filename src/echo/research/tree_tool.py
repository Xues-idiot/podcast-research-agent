"""树工具"""

from typing import Any, Optional


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.children = []


class TreeTool:
    _instance: Optional["TreeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_node(self, value: Any) -> TreeNode:
        return TreeNode(value)

    def add_child(self, parent: TreeNode, child: TreeNode) -> None:
        parent.children.append(child)

    def traverse(self, node: TreeNode) -> List[Any]:
        result = [node.value]
        for child in node.children:
            result.extend(self.traverse(child))
        return result


def get_tree_tool() -> TreeTool:
    return TreeTool()
