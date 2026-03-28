"""NanoID生成API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.nanoid_gen import get_nanoid_gen_tool


router = APIRouter(prefix="/api/nanoid-gen", tags=["nanoid-gen"])


class GenerateRequest(BaseModel):
    size: int = 21


@router.post("/generate")
async def generate(request: GenerateRequest):
    tool = get_nanoid_gen_tool()
    return {"result": tool.generate(request.size)}


class BatchGenerateRequest(BaseModel):
    count: int
    size: int = 21


@router.post("/generate-batch")
async def generate_batch(request: BatchGenerateRequest):
    tool = get_nanoid_gen_tool()
    return {"result": tool.generate_multiple(request.count, request.size)}