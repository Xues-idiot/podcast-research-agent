"""图像嵌入API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.image_embed import get_image_embed_tool


router = APIRouter(prefix="/api/image-embed", tags=["image-embed"])


class EmbedRequest(BaseModel):
    base: list[list[list[float]]]
    overlay: list[list[list[float]]]
    x: int = 0
    y: int = 0
    alpha: float = 1.0


@router.post("/embed")
async def embed(request: EmbedRequest):
    tool = get_image_embed_tool()
    return {"result": tool.embed(request.base, request.overlay, request.x, request.y, request.alpha)}