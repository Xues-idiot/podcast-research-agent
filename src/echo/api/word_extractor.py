"""单词提取API"""

from fastapi import APIRouter

from echo.research.word_extractor import get_word_extractor


router = APIRouter(prefix="/api/words", tags=["words"])


@router.post("/extract")
async def extract_words(text: str, min_length: int = 2):
    extractor = get_word_extractor()
    return {"words": extractor.extract_words(text, min_length)}


@router.post("/chinese")
async def extract_chinese(text: str, min_length: int = 2):
    extractor = get_word_extractor()
    return {"words": extractor.extract_chinese_words(text, min_length)}


@router.post("/ngrams")
async def extract_ngrams(text: str, n: int = 2):
    extractor = get_word_extractor()
    return {"ngrams": extractor.extract_ngrams(text, n)}


@router.post("/frequency")
async def word_frequency(text: str, top_n: int = 20):
    extractor = get_word_extractor()
    return {"frequencies": extractor.word_frequency(text, top_n)}