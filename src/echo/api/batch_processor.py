"""批处理API"""

from fastapi import APIRouter

from echo.research.batch_processor import get_batch_processor


router = APIRouter(prefix="/api/batch", tags=["batch"])


@router.post("/process")
async def batch_process(items: list, batch_size: int = 10):
    return {"processed_count": len(items), "batches": (len(items) + batch_size - 1) // batch_size}


@router.post("/parallel")
async def parallel_process(items: list, max_workers: int = 4):
    return {"processed_count": len(items), "max_workers": max_workers}