"""文本截断API"""

from fastapi import APIRouter

from echo.research.truncator import get_text_truncator


router = APIRouter(prefix="/api/truncate", tags=["truncate"])


@router.post("/by_length")
async def truncate_by_length(text: str, max_length: int, suffix: str = "..."):
    truncator = get_text_truncator()
    result = truncator.truncate(text, max_length, suffix)
    return {
        "truncated_text": result.truncated_text,
        "original_length": result.original_length,
        "truncated_length": result.truncated_length,
        "was_truncated": result.was_truncated,
    }


@router.post("/by_words")
async def truncate_by_words(text: str, max_words: int, suffix: str = "..."):
    truncator = get_text_truncator()
    result = truncator.truncate_by_words(text, max_words, suffix)
    return {
        "truncated_text": result.truncated_text,
        "original_length": result.original_length,
        "truncated_length": result.truncated_length,
        "was_truncated": result.was_truncated,
    }


@router.post("/by_sentences")
async def truncate_by_sentences(text: str, max_sentences: int, suffix: str = "..."):
    truncator = get_text_truncator()
    result = truncator.truncate_sentences(text, max_sentences, suffix)
    return {
        "truncated_text": result.truncated_text,
        "original_length": result.original_length,
        "truncated_length": result.truncated_length,
        "was_truncated": result.was_truncated,
    }