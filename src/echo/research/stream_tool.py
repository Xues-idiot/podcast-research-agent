"""流式处理工具"""

from typing import Any, Callable, Iterator, Optional


class StreamTool:
    _instance: Optional["StreamTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stream(self, items: list) -> Iterator:
        return iter(items)

    def pipe(self, *funcs: Callable) -> Callable:
        def piped(value):
            result = value
            for func in funcs:
                result = func(result)
            return result
        return piped

    def filter_stream(self, items: list, pred: Callable) -> Iterator:
        return (item for item in items if pred(item))


def get_stream_tool() -> StreamTool:
    return StreamTool()
