"""回归API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.regression_tool import get_regression_tool


router = APIRouter(prefix="/api/regression", tags=["regression"])


class RegressionRequest(BaseModel):
    x: list
    y: list


@router.post("/linear")
async def linear(request: RegressionRequest):
    return {"result": get_regression_tool().linear_regression(request.x, request.y)}
