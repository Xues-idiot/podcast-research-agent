"""绑定API"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/binding", tags=["binding"])


@router.post("/bind")
async def bind():
    return {"result": None}
