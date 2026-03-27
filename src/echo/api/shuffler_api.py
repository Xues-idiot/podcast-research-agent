"""打乱API"""

from fastapi import APIRouter

from echo.research.shuffler import get_shuffler


router = APIRouter(prefix="/api/shuffler", tags=["shuffler"])


@router.post("/shuffle")
async def shuffle(items: list):
    return {"result": get_shuffler().shuffle(items)}