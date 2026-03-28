"""列表查找工具 - 在列表中查找元素"""
from typing import Any, List, Optional, Callable
from dataclasses import dataclass


@dataclass
class FindResult:
    found: bool
    index: Optional[int]
    item: Optional[Any]


def list_find(
    lst: List[Any],
    predicate: Optional[Callable[[Any], bool]] = None,
    value: Optional[Any] = None
) -> FindResult:
    """
    在列表中查找元素

    Args:
        lst: 源列表
        predicate: 谓词函数
        value: 要查找的值

    Returns:
        FindResult: 查找结果
    """
    if value is not None:
        try:
            idx = lst.index(value)
            return FindResult(found=True, index=idx, item=value)
        except ValueError:
            return FindResult(found=False, index=None, item=None)
    elif predicate is not None:
        for idx, item in enumerate(lst):
            if predicate(item):
                return FindResult(found=True, index=idx, item=item)
        return FindResult(found=False, index=None, item=None)
    return FindResult(found=False, index=None, item=None)


def list_find_all(
    lst: List[Any],
    predicate: Optional[Callable[[Any], bool]] = None,
    value: Optional[Any] = None
) -> List[Any]:
    """查找所有匹配的元素"""
    if value is not None:
        return [x for x in lst if x == value]
    elif predicate is not None:
        return [x for x in lst if predicate(x)]
    return []


def list_contains(lst: List[Any], value: Any) -> bool:
    """检查列表是否包含元素"""
    return value in lst


def list_index_of(lst: List[Any], value: Any) -> int:
    """返回元素首次出现的索引，不存在返回-1"""
    try:
        return lst.index(value)
    except ValueError:
        return -1


def list_count(lst: List[Any], value: Any) -> int:
    """计算元素出现的次数"""
    return lst.count(value)

