"""Promise工具"""

from typing import Any, Callable, Optional
import asyncio


class PromiseTool:
    _instance: Optional["PromiseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def promise(self, func: Callable, *args, **kwargs) -> Any:
        return await func(*args, **kwargs)

    def resolve(self, value: Any) -> Any:
        return value

    def reject(self, error: Exception) -> Exception:
        return error

    def all(self, promises: list) -> list:
        return promises


def get_promise_tool() -> PromiseTool:
    return PromiseTool()
