"""3D插值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.lerp_3d import get_lerp_3d


router = APIRouter(prefix="/api/lerp-3d", tags=["lerp-3d"])


class Lerp3DRequest(BaseModel):
    a: list
    b: list
    t: float


@router.post("/lerp")
async def lerp(request: Lerp3DRequest):
    return {"result": get_lerp_3d().lerp_3d(
        tuple(request.a), tuple(request.b), request.t
    )}
