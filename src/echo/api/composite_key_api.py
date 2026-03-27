"""组合键API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.composite_key import get_composite_key


router = APIRouter(prefix="/api/composite-key", tags=["composite-key"])


class CompositeKeyRequest(BaseModel):
    parts: list


@router.post("/make")
async def make(request: CompositeKeyRequest):
    return {"result": get_composite_key().make_key(*request.parts)}
