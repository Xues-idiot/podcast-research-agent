"""深度扁平化API"""

from fastapi import APIRouter

from echo.research.flatten_deep import get_flatten_deep


router = APIRouter(prefix="/api/deep-flatten", tags=["deep-flatten"])


@router.post("/flatten")
async def flatten(items: list):
    return {"result": get_flatten_deep().flatten(items)}
