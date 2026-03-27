"""前缀工具"""

from typing import List, Any, Optional


class PrependList:
    _instance: Optional["PrependList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def prepend(self, items: List[Any], item: Any) -> List[Any]:
        return [item] + items

    def prepend_all(self, items: List[Any], prefix_items: List[Any]) -> List[Any]:
        return prefix_items + items

    def cons(self, item: Any, items: List[Any]) -> List[Any]:
        return [item] + items


def get_prepend_list() -> PrependList:
    return PrependList()
