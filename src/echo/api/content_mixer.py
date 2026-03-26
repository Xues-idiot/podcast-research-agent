"""内容混合API"""

from fastapi import APIRouter

from echo.research.content_mixer import get_content_mixer


router = APIRouter(prefix="/api/mix", tags=["mix"])


@router.post("/sequential")
async def mix_sequential(contents: list[str], separator: str = "\n\n---\n\n"):
    mixer = get_content_mixer()
    result = mixer.mix_sequential(contents, separator)
    return {"result": result, "source_count": len(contents)}


@router.post("/interleave")
async def mix_interleave(contents: list[str], segment_size: int = 3):
    mixer = get_content_mixer()
    result = mixer.mix_interleave(contents, segment_size)
    return {"result": result, "source_count": len(contents)}


@router.post("/weighted")
async def mix_weighted(contents: list[str], weights: list[float]):
    mixer = get_content_mixer()
    result = mixer.mix_summary(contents, weights)
    return {"result": result, "source_count": len(contents)}