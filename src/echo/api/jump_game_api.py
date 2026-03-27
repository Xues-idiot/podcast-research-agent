"""跳跃游戏API"""

from fastapi import APIRouter

from echo.research.jump_game import get_jump_game


router = APIRouter(prefix="/api/jump-game", tags=["jump-game"])


@router.post("/can-reach")
async def can_reach(nums: list):
    """能否到达终点"""
    tool = get_jump_game()
    return {"can_reach": tool.can_reach_end(nums)}
