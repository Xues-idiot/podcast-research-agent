"""按键分组API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.group_by_key import get_group_by_key


router = APIRouter(prefix="/api/group-by-key", tags=["group-by-key"])


class GroupRequest(BaseModel):
    items: list
    key_func: str = "lambda x: x"


@router.post("/group")
async def group(request: GroupRequest):
    key_func = eval(request.key_func)
    return {"result": get_group_by_key().group(request.items, key_func)}
