"""延迟工具"""

import time
from typing import Optional


class DelayTool:
    """延迟工具"""

    def delay(self, seconds: float) -> None:
        """延迟秒数"""
        time.sleep(seconds)

    def delay_ms(self, milliseconds: int) -> None:
        """延迟毫秒"""
        time.sleep(milliseconds / 1000.0)


_delay_tool: Optional[DelayTool] = None


def get_delay_tool() -> DelayTool:
    global _delay_tool
    if _delay_tool is None:
        _delay_tool = DelayTool()
    return _delay_tool