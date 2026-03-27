"""Walker tool for traversing data structures"""

from typing import Any, Callable, List, Optional


class WalkerTool:
    _instance: Optional["WalkerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def walk(self, data: Any, callback: Callable[[Any], None]) -> None:
        """Walk through a data structure and apply callback to each element"""
        callback(data)
        if isinstance(data, list):
            for item in data:
                self.walk(item, callback)
        elif isinstance(data, dict):
            for value in data.values():
                self.walk(value, callback)

    def walk_with_path(self, data: Any, callback: Callable[[Any, str], None], path: str = "") -> None:
        """Walk through data structure with path information"""
        callback(data, path)
        if isinstance(data, list):
            for i, item in enumerate(data):
                self.walk_with_path(item, callback, f"{path}[{i}]")
        elif isinstance(data, dict):
            for key, value in data.items():
                new_path = f"{path}.{key}" if path else key
                self.walk_with_path(value, callback, new_path)

    def collect(self, data: Any, predicate: Callable[[Any], bool]) -> List[Any]:
        """Collect elements matching a predicate"""
        results = []
        def collector(item):
            if predicate(item):
                results.append(item)
        self.walk(data, collector)
        return results

    def process(self, data: Any) -> Any:
        """Process data by walking through it"""
        return data


def get_walker_tool() -> WalkerTool:
    return WalkerTool()