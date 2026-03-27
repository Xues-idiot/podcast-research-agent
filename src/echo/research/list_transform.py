"""列表转换工具"""

from typing import Optional, Callable


class ListTransform:
    """列表转换工具"""

    def map(self, items: list, func: Callable) -> list:
        """映射"""
        return [func(item) for item in items]

    def filter(self, items: list, func: Callable) -> list:
        """过滤"""
        return [item for item in items if func(item)]

    def reduce(self, items: list, func: Callable, initial: any = None) -> any:
        """聚合"""
        return func(initial, items[0]) if len(items) == 1 else func(initial if initial is not None else items[0], items[1])


_transform: Optional[ListTransform] = None


def get_list_transform() -> ListTransform:
    global _transform
    if _transform is None:
        _transform = ListTransform()
    return _transform