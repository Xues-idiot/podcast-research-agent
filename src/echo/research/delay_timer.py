"""延迟工具"""

import asyncio
from typing import Optional


class DelayTimerTool:
    _instance: Optional["DelayTimerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def delay(self, seconds: float) -> None:
        await asyncio.sleep(seconds)

    def calculate_delay(self, from_rate: float, to_rate: float, samples: int) -> float:
        if to_rate <= 0:
            return 0.0
        return samples / to_rate


def get_delay_timer_tool() -> DelayTimerTool:
    return DelayTimerTool()