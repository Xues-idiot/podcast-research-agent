"""带索引压缩API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.zip_with_index import get_zip_with_index


router = APIRouter(prefix="/api/zip-index", tags=["zip-index"])


class ZipIndexRequest(BaseModel):
    items: list
    start: int = 0


@router.post("/zip")
async def zip_with_index(request: ZipIndexRequest):
    return {"result": get_zip_with_index().zip_with_index(request.items, request.start)}
