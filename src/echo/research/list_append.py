"""列表拼接工具"""

from typing import List, Any, Optional


class ListAppendTool:
    _instance: Optional["ListAppendTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_item(self, items: List[Any], item: Any) -> List[Any]:
        """添加单个元素"""
        return items + [item]

    def add_items(self, items: List[Any], new_items: List[Any]) -> List[Any]:
        """添加多个元素"""
        return items + new_items

    def join_strings(self, strings: List[str], separator: str = "") -> str:
        """连接字符串列表"""
        return separator.join(strings)

    def split_join(self, items: List[Any], sep: str = ", ") -> str:
        """转换为分隔符连接的字符串"""
        return sep.join(str(item) for item in items)


_list_append_instance: Optional[ListAppendTool] = None


def get_list_append_tool() -> ListAppendTool:
    global _list_append_instance
    if _list_append_instance is None:
        _list_append_instance = ListAppendTool()
    return _list_append_instance