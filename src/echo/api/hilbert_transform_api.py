"""希尔伯特变换API"""

from fastapi import APIRouter

from echo.research.hilbert_transform import get_hilbert_transform


router = APIRouter(prefix="/api/hilbert", tags=["hilbert"])


@router.post("/transform")
async def transform(signal: list):
    return {"result": get_hilbert_transform().hilbert(signal)}
