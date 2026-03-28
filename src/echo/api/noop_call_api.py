"""空操作API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.noop_call import get_noop_call_tool


router = APIRouter(prefix="/api/noop-call", tags=["noop-call"])


@router.post("/noop")
async def noop():
    tool = get_noop_call_tool()
    tool.noop()
    return {"message": "Noop executed"}


class IdentityRequest(BaseModel):
    value: Any


@router.post("/identity")
async def identity(request: IdentityRequest):
    tool = get_noop_call_tool()
    return {"result": tool.identity(request.value)}