"""Orderer tool for ordering items"""

from typing import Any, Callable, Dict, List, Optional, Tuple


class OrdererTool:
    _instance: Optional["OrdererTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def order_by(self, items: List[Any], key_func: Callable[[Any], Any], ascending: bool = True) -> List[Any]:
        """Order items by a key function"""
        return sorted(items, key=key_func, reverse=not ascending)

    def order_ascending(self, items: List[Any], key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Order items in ascending order"""
        return sorted(items, key=key_func)

    def order_descending(self, items: List[Any], key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Order items in descending order"""
        return sorted(items, key=key_func, reverse=True)

    def order_by_index(self, items: List[Any], indices: List[int]) -> List[Any]:
        """Reorder items by their indices"""
        if not indices:
            return []
        ordered = []
        for idx in indices:
            if 0 <= idx < len(items):
                ordered.append(items[idx])
        return ordered

    def order_naturally(self, items: List[str]) -> List[str]:
        """Order strings naturally (1, 2, 10 instead of 1, 10, 2)"""
        import re
        def natural_key(s):
            return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]
        return sorted(items, key=natural_key)

    def reverse_order(self, items: List[Any]) -> List[Any]:
        """Reverse the order of items"""
        return list(reversed(items))

    def shuffle(self, items: List[Any]) -> List[Any]:
        """Randomly shuffle items"""
        import random
        shuffled = list(items)
        random.shuffle(shuffled)
        return shuffled

    def process(self, data: Any) -> Any:
        """Process data by ordering"""
        return data


def get_orderer_tool() -> OrdererTool:
    return OrdererTool()