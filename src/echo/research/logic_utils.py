"""逻辑工具集合"""
from typing import Any, Callable


def identity(x: Any) -> Any:
    return x


def always(x: Any) -> Callable:
    return lambda: x


def never(x: Any) -> bool:
    return False


def is_none(x: Any) -> bool:
    return x is None


def is_not_none(x: Any) -> bool:
    return x is not None


def is_empty(x: Any) -> bool:
    if x is None:
        return True
    if isinstance(x, (str, list, dict, tuple, set)):
        return len(x) == 0
    return False


def is_truthy(x: Any) -> bool:
    return bool(x)


def is_falsy(x: Any) -> bool:
    return not bool(x)


def if_fn(condition: bool, true_val: Any, false_val: Any) -> Any:
    return true_val if condition else false_val


def switch(value: Any, cases: dict, default: Any = None) -> Any:
    return cases.get(value, default)


def coalesce(*values: Any) -> Any:
    for v in values:
        if v is not None:
            return v
    return None


def default_to(value: Any, default: Any) -> Any:
    return value if value is not None else default


def pipe(*funcs: Callable) -> Callable:
    def piped(x):
        result = x
        for fn in funcs:
            result = fn(result)
        return result
    return piped


def compose(*funcs: Callable) -> Callable:
    def composed(x):
        result = x
        for fn in reversed(funcs):
            result = fn(result)
        return result
    return composed
