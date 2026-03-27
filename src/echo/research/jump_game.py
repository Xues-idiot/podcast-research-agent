"""跳跃游戏工具"""

from typing import List, Optional


class JumpGame:
    _instance: Optional["JumpGame"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def can_reach_end(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True


def get_jump_game() -> JumpGame:
    return JumpGame()
