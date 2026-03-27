"""小波变换API"""

from fastapi import APIRouter

from echo.research.wavelet_transform import get_wavelet_transform


router = APIRouter(prefix="/api/wavelet", tags=["wavelet"])


@router.post("/haar")
async def haar(signal: list):
    return {"result": get_wavelet_transform().haar_transform(signal)}
