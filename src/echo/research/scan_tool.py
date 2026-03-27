"""扫描工具"""

from typing import List, Any, Callable


class ScanTool:
    _instance: Optional["ScanTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scan(self, items: List[Any], func: Callable = None) -> List[Any]:
        if func is None:
            func = lambda a, b: a + b
        result = [items[0]] if items else []
        for item in items[1:]:
            result.append(func(result[-1], item))
        return result


def get_scan_tool() -> ScanTool:
    return ScanTool()
