"""误差函数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.error_function import get_error_function


router = APIRouter(prefix="/api/error-function", tags=["error-function"])


class ErfRequest(BaseModel):
    x: float


@router.post("/erf")
async def erf(request: ErfRequest):
    return {"result": get_error_function().erf(request.x)}
