"""句子分割API"""

from fastapi import APIRouter

from echo.research.sentence_splitter import get_sentence_splitter


router = APIRouter(prefix="/api/sentences", tags=["sentences"])


@router.post("/split")
async def split_sentences(text: str, language: str = "mixed"):
    splitter = get_sentence_splitter()
    if language == "chinese":
        sentences = splitter.split_chinese(text)
    elif language == "english":
        sentences = splitter.split_english(text)
    else:
        sentences = splitter.split_mixed(text)
    return {"sentences": sentences, "count": len(sentences)}


@router.post("/split_by_length")
async def split_by_length(text: str, max_length: int = 200):
    splitter = get_sentence_splitter()
    sentences = splitter.split_by_length(text, max_length)
    return {"sentences": sentences, "count": len(sentences)}