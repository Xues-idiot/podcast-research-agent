"""ID生成API"""

from fastapi import APIRouter

from echo.research.id_generator import get_id_generator


router = APIRouter(prefix="/api/id", tags=["id"])


@router.post("/uuid")
async def generate_uuid():
    return {"id": get_id_generator().uuid4()}


@router.post("/short")
async def generate_short_id(length: int = 12):
    return {"id": get_id_generator().short_id(length)}


@router.post("/numeric")
async def generate_numeric_id(length: int = 8):
    return {"id": get_id_generator().numeric_id(length)}


@router.post("/hash")
async def generate_hash_id(text: str):
    return {"id": get_id_generator().hash_id(text)}