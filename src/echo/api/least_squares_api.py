"""最小二乘法API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.least_squares import get_least_squares


router = APIRouter(prefix="/api/least-squares", tags=["least-squares"])


class LSRequest(BaseModel):
    x: list
    y: list


@router.post("/fit")
async def fit(request: LSRequest):
    return {"result": get_least_squares().fit(request.x, request.y)}
