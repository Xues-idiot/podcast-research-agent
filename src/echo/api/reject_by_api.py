"""拒绝API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.reject_by import get_reject_by


router = APIRouter(prefix="/api/reject", tags=["reject"])


class RejectRequest(BaseModel):
    items: list
    pred: str = "lambda x: False"


@router.post("/reject")
async def reject(request: RejectRequest):
    pred = eval(request.pred)
    return {"result": get_reject_by().reject(request.items, pred)}
