"""任意全部无匹配工具"""

from typing import List, Any, Callable, Optional


class AnyAllNoneTool:
    _instance: Optional["AnyAllNoneTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def any_match(self, items: List[Any], predicate: Callable[[Any], bool]) -> bool:
        return any(predicate(item) for item in items)

    def all_match(self, items: List[Any], predicate: Callable[[Any], bool]) -> bool:
        return all(predicate(item) for item in items)

    def none_match(self, items: List[Any], predicate: Callable[[Any], bool]) -> bool:
        return not any(predicate(item) for item in items)


def get_any_all_none_tool() -> AnyAllNoneTool:
    return AnyAllNoneTool()