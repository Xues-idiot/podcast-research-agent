"""随机漫步工具"""

from typing import Optional, List
import random


class RandomWalkTool:
    _instance: Optional["RandomWalkTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def walk_1d(self, steps: int, start: float = 0, step_size: float = 1) -> List[float]:
        """一维随机漫步"""
        path = [start]
        pos = start
        for _ in range(steps):
            pos += random.choice([-step_size, step_size])
            path.append(pos)
        return path

    def walk_2d(self, steps: int, start_x: float = 0, start_y: float = 0) -> List[tuple]:
        """二维随机漫步"""
        path = [(start_x, start_y)]
        x, y = start_x, start_y
        for _ in range(steps):
            direction = random.choice(["N", "S", "E", "W"])
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            else:
                x -= 1
            path.append((x, y))
        return path

    def walk_gaussian(self, steps: int, start: float = 0, std: float = 1) -> List[float]:
        """高斯随机漫步"""
        path = [start]
        pos = start
        for _ in range(steps):
            pos += random.gauss(0, std)
            path.append(pos)
        return path

    def final_distance(self, path: List[tuple]) -> float:
        """计算最终距离"""
        if not path:
            return 0
        start = path[0]
        end = path[-1]
        return ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5


_rw_instance: Optional[RandomWalkTool] = None


def get_random_walk_tool() -> RandomWalkTool:
    global _rw_instance
    if _rw_instance is None:
        _rw_instance = RandomWalkTool()
    return _rw_instance