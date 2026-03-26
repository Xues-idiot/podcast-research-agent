"""智能分块API"""

from fastapi import APIRouter

from echo.research.chunks import get_chunking_strategy


router = APIRouter(prefix="/api/chunks", tags=["chunks"])


@router.post("/chunk")
async def chunk_content(
    content: str,
    strategy: str = "size",
    max_size: int = 1000,
    overlap: int = 100,
    max_paragraphs: int = 5
):
    chunker = get_chunking_strategy(strategy)

    if strategy == "paragraph":
        chunks = chunker.chunk_by_paragraph(content, max_paragraphs)
    elif strategy == "topic":
        chunks = chunker.chunk_by_topic(content)
    else:
        chunks = chunker.chunk_by_size(content, max_size, overlap)

    return {
        "strategy": strategy,
        "chunk_count": len(chunks),
        "chunks": [
            {
                "content": c.content[:200] + "..." if len(c.content) > 200 else c.content,
                "start_index": c.start_index,
                "end_index": c.end_index,
                "chunk_type": c.chunk_type,
            }
            for c in chunks
        ]
    }