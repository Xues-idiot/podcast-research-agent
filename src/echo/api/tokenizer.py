"""分词API"""

from fastapi import APIRouter

from echo.research.tokenizer import get_tokenizer


router = APIRouter(prefix="/api/tokenize", tags=["tokenize"])


@router.post("/cut")
async def tokenize(text: str):
    tokenizer = get_tokenizer()
    return {"tokens": tokenizer.tokenize(text)}


@router.post("/search")
async def tokenize_for_search(text: str):
    tokenizer = get_tokenizer()
    return {"tokens": tokenizer.tokenize_for_search(text)}


@router.post("/keywords")
async def extract_keywords(text: str, top_n: int = 20):
    tokenizer = get_tokenizer()
    return {"keywords": tokenizer.extract_keywords(text, top_n)}