"""列表批处理工具 - 对列表元素进行批量操作"""
from typing import Any, List, Callable, Optional
from dataclasses import dataclass


@dataclass
class BatchResult:
    results: List[Any]
    count: int
    success_count: int
    error_count: int


def list_batch(
    lst: List[Any],
    func: Callable[[Any], Any],
    error_handling: str = "skip"  # "skip", "stop", "collect"
) -> BatchResult:
    """
    对列表元素进行批量操作

    Args:
        lst: 源列表
        func: 处理函数
        error_handling: 错误处理策略

    Returns:
        BatchResult: 批处理结果
    """
    results = []
    errors = []
    success_count = 0
    error_count = 0

    for item in lst:
        try:
            result = func(item)
            results.append(result)
            success_count += 1
        except Exception as e:
            error_count += 1
            if error_handling == "stop":
                break
            elif error_handling == "collect":
                errors.append(str(e))

    if error_handling == "collect":
        results.extend(errors)

    return BatchResult(
        results=results,
        count=len(results),
        success_count=success_count,
        error_count=error_count
    )


def list_map(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """对每个元素应用函数"""
    return [func(item) for item in lst]


def list_filter(lst: List[Any], predicate: Callable[[Any], bool]) -> List[Any]:
    """过滤元素"""
    return [item for item in lst if predicate(item)]


def list_reduce(
    lst: List[Any],
    func: Callable[[Any, Any], Any],
    initial: Optional[Any] = None
) -> Any:
    """归约操作"""
    if not lst:
        return initial
    if initial is None:
        return functools.reduce(func, lst)
    return functools.reduce(func, lst, initial)


import functools

