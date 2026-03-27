"""折叠工具"""

from typing import List, Any, Callable, Optional


class FoldTool:
    _instance: Optional["FoldTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fold(self, items: List[Any], func: Callable, initial: Any = None) -> Any:
        if not items:
            return initial
        if initial is None:
            result = items[0]
            for item in items[1:]:
                result = func(result, item)
        else:
            result = initial
            for item in items:
                result = func(result, item)
        return result


def get_fold_tool() -> FoldTool:
    return FoldTool()
