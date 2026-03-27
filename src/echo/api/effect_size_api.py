"""效应量API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.effect_size import get_effect_size


router = APIRouter(prefix="/api/effect-size", tags=["effect-size"])


class EffectSizeRequest(BaseModel):
    group1: list
    group2: list


@router.post("/cohens-d")
async def cohens_d(request: EffectSizeRequest):
    return {"result": get_effect_size().cohens_d(request.group1, request.group2)}
