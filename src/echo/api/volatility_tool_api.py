"""波动率API"""

from fastapi import APIRouter

from echo.research.volatility_tool import get_volatility_tool


router = APIRouter(prefix="/api/volatility", tags=["volatility"])


@router.post("/historical")
async def historical(returns: list):
    return {"result": get_volatility_tool().historical_volatility(returns)}
