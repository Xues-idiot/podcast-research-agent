"""双边滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.bilateral_filter import get_bilateral_filter


router = APIRouter(prefix="/api/bilateral", tags=["bilateral"])


class BilateralRequest(BaseModel):
    data: list
    spatial_sigma: float = 1.0
    range_sigma: float = 1.0
    window: int = 3


@router.post("/filter")
async def filter(request: BilateralRequest):
    return {"result": get_bilateral_filter().filter(
        request.data, request.spatial_sigma, request.range_sigma, request.window
    )}
