"""异步池工具"""

from typing import Any, Callable, List, Optional
import asyncio


class AsyncPool:
    _instance: Optional["AsyncPool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def map_async(self, func: Callable, items: List[Any]) -> List[Any]:
        return [await func(item) for item in items]

    async def gather(self, *coros) -> List[Any]:
        return await asyncio.gather(*coros)

    async def wait(self, *coros):
        return await asyncio.wait(coros)


def get_async_pool() -> AsyncPool:
    return AsyncPool()
