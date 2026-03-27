"""硬币找零API"""

from fastapi import APIRouter

from echo.research.coin_change import get_coin_change


router = APIRouter(prefix="/api/coin-change", tags=["coin-change"])


@router.post("/min-coins")
async def min_coins(coins: list, amount: int):
    """最少硬币数"""
    tool = get_coin_change()
    return {"result": tool.min_coins(coins, amount)}
