"""傅里叶变换API"""

from fastapi import APIRouter

from echo.research.fourier_transform import get_fourier_transform


router = APIRouter(prefix="/api/fourier", tags=["fourier"])


@router.post("/dft")
async def dft(signal: list):
    return {"result": get_fourier_transform().dft(signal)}
