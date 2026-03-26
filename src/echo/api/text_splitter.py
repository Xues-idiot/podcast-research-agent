"""文本分割API"""

from fastapi import APIRouter

from echo.research.text_splitter import get_text_splitter


router = APIRouter(prefix="/api/split", tags=["split"])


@router.post("/by_chars")
async def split_by_chars(text: str, chunk_size: int = 1000, overlap: int = 100):
    splitter = get_text_splitter()
    result = splitter.split_by_chars(text, chunk_size, overlap)
    return {"parts": result.parts, "part_count": result.part_count}


@router.post("/by_sentences")
async def split_by_sentences(text: str, sentences_per_chunk: int = 5):
    splitter = get_text_splitter()
    result = splitter.split_by_sentences(text, sentences_per_chunk)
    return {"parts": result.parts, "part_count": result.part_count}


@router.post("/by_paragraphs")
async def split_by_paragraphs(text: str, paragraphs_per_chunk: int = 3):
    splitter = get_text_splitter()
    result = splitter.split_by_paragraphs(text, paragraphs_per_chunk)
    return {"parts": result.parts, "part_count": result.part_count}