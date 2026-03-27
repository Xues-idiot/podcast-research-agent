"""Huffman编码工具"""

from typing import Any, Dict, List, Optional, Tuple
import heapq


class HuffmanNode:
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanTool:
    _instance: Optional["HuffmanTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, text: str) -> Tuple[Dict[str, str], str]:
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1

        heap = [HuffmanNode(char, f) for char, f in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        codes = {}

        def generate_codes(node, code=""):
            if node:
                if node.char:
                    codes[node.char] = code
                generate_codes(node.left, code + "0")
                generate_codes(node.right, code + "1")

        if heap:
            generate_codes(heap[0])
        encoded = "".join(codes.get(c, "") for c in text)
        return codes, encoded


def get_huffman_tool() -> HuffmanTool:
    return HuffmanTool()
