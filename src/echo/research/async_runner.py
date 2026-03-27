"""异步运行器"""

import asyncio
from typing import Callable, Any, Optional


class AsyncRunner:
    _instance: Optional["AsyncRunner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def run_async(self, func: Callable, *args: Any) -> Any:
        if asyncio.iscoroutinefunction(func):
            return await func(*args)
        return func(*args)

    def run_sync(self, func: Callable, *args: Any) -> Any:
        return asyncio.run(func(*args))


def get_async_runner() -> AsyncRunner:
    return AsyncRunner()
