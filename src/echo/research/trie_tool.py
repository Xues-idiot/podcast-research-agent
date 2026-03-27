"""字典树工具"""

from typing import Any, Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False


class TrieTool:
    _instance: Optional["TrieTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self) -> TrieNode:
        return TrieNode()

    def insert(self, root: TrieNode, word: str) -> None:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, root: TrieNode, word: str) -> bool:
        node = root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


def get_trie_tool() -> TrieTool:
    return TrieTool()
