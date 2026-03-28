"""色度特征API"""

from fastapi import APIRouter

from echo.research.chroma_features import get_chroma_features


router = APIRouter(prefix="/api/chroma", tags=["chroma"])


@router.post("/compute")
async def compute_chroma(spectrum: list[float], sample_rate: float = 44100):
    chroma = get_chroma_features()
    return {"chroma": chroma.compute(spectrum, sample_rate)}
