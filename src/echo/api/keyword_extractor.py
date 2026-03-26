"""关键词提取API"""

from fastapi import APIRouter

from echo.research.keyword_extractor import get_keyword_extractor


router = APIRouter(prefix="/api/keywords", tags=["keywords"])


@router.post("/extract")
async def extract_keywords(text: str, top_n: int = 10):
    extractor = get_keyword_extractor()
    keywords = extractor.extract(text, top_n)
    return {"keywords": keywords}


@router.post("/phrases")
async def extract_phrases(text: str, top_n: int = 5):
    extractor = get_keyword_extractor()
    phrases = extractor.extract_phrases(text, top_n)
    return {"phrases": phrases}