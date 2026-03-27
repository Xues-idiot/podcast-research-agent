"""数据生成API"""

from fastapi import APIRouter

from echo.research.data_generator import get_data_generator


router = APIRouter(prefix="/api/generate", tags=["generate"])


@router.post("/random_string")
async def random_string(length: int = 10):
    return {"result": get_data_generator().random_string(length)}


@router.post("/random_digits")
async def random_digits(length: int = 6):
    return {"result": get_data_generator().random_digits(length)}


@router.post("/random_hex")
async def random_hex(length: int = 8):
    return {"result": get_data_generator().random_hex(length)}