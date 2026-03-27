"""卷积API"""

from fastapi import APIRouter

from echo.research.convolution_tool import get_convolution_tool


router = APIRouter(prefix="/api/convolution", tags=["convolution"])


@router.post("/convolve")
async def convolve(a: list, b: list):
    return {"result": get_convolution_tool().convolve(a, b)}
