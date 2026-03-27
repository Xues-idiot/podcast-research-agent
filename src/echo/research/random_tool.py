"""随机数工具"""

from typing import Optional, List
import random


class RandomTool:
    """随机数工具"""

    def random_int(self, low: int, high: int) -> int:
        """随机整数"""
        return random.randint(low, high)

    def random_float(self) -> float:
        """随机浮点数"""
        return random.random()

    def random_choice(self, items: List) -> any:
        """随机选择"""
        return random.choice(items)

    def shuffle(self, items: List) -> List:
        """打乱顺序"""
        result = list(items)
        random.shuffle(result)
        return result


_random_tool: Optional[RandomTool] = None


def get_random_tool() -> RandomTool:
    global _random_tool
    if _random_tool is None:
        _random_tool = RandomTool()
    return _random_tool