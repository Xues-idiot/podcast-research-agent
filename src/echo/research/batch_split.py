"""批处理分割工具"""

from typing import List, Any, Optional, Callable


class BatchSplitTool:
    _instance: Optional["BatchSplitTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def split_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        """按固定大小分割列表"""
        result = []
        for i in range(0, len(items), size):
            result.append(items[i:i + size])
        return result

    def split_by_count(self, items: List[Any], count: int) -> List[List[Any]]:
        """分割成指定数量"""
        if count <= 0:
            return [items]
        size = len(items) // count
        remainder = len(items) % count
        result = []
        idx = 0
        for i in range(count):
            batch_size = size + (1 if i < remainder else 0)
            result.append(items[idx:idx + batch_size])
            idx += batch_size
        return result

    def split_by_predicate(self, items: List[Any], predicate: Callable[[Any], bool]) -> tuple:
        """按谓词分割为两个列表"""
        matched = []
        not_matched = []
        for item in items:
            if predicate(item):
                matched.append(item)
            else:
                not_matched.append(item)
        return (matched, not_matched)

    def split_at_index(self, items: List[Any], index: int) -> tuple:
        """在指定索引分割"""
        if index < 0 or index > len(items):
            return (items, [])
        return (items[:index], items[index:])


def get_batch_split_tool() -> BatchSplitTool:
    return BatchSplitTool()