"""数组工具集合"""
from typing import Any, List, Callable


def array_unique(arr: List[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def array_union(*arrays: List[Any]) -> List[Any]:
    result = []
    for arr in arrays:
        for item in arr:
            if item not in result:
                result.append(item)
    return result


def array_intersect(*arrays: List[Any]) -> List[Any]:
    if not arrays:
        return []
    result = set(arrays[0])
    for arr in arrays[1:]:
        result &= set(arr)
    return list(result)


def array_diff(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    return [x for x in arr1 if x not in arr2]


def array_chunk(arr: List[Any], size: int) -> List[List[Any]]:
    return [arr[i:i+size] for i in range(0, len(arr), size)]


def array_flatten(nested: List[Any]) -> List[Any]:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(array_flatten(item))
        else:
            result.append(item)
    return result


def array_zip(*arrays: List[Any]) -> List[tuple]:
    return list(zip(*arrays))


def array_map(arr: List[Any], fn: Callable[[Any], Any]) -> List[Any]:
    return [fn(x) for x in arr]


def array_filter(arr: List[Any], pred: Callable[[Any], bool]) -> List[Any]:
    return [x for x in arr if pred(x)]


def array_reduce(arr: List[Any], fn: Callable[[Any, Any], Any], init: Any = None) -> Any:
    if not arr:
        return init
    result = arr[0]
    for x in arr[1:]:
        result = fn(result, x)
    return result
