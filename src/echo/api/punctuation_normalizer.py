"""标点符号API"""

from fastapi import APIRouter

from echo.research.punctuation_normalizer import get_punctuation_normalizer


router = APIRouter(prefix="/api/punctuation", tags=["punctuation"])


@router.post("/normalize")
async def normalize(text: str):
    return {"result": get_punctuation_normalizer().normalize(text)}


@router.post("/add_spaces")
async def add_spaces(text: str):
    return {"result": get_punctuation_normalizer().add_spaces(text)}


@router.post("/remove_spaces")
async def remove_spaces(text: str):
    return {"result": get_punctuation_normalizer().remove_spaces(text)}