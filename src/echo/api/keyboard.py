"""键盘快捷键API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.keyboard import get_keyboard_manager


router = APIRouter(prefix="/api/keyboard", tags=["keyboard"])


class UpdateShortcutRequest(BaseModel):
    action: str
    key: str
    modifiers: list = []


@router.get("/")
async def list_shortcuts(scope: str = None):
    manager = get_keyboard_manager()
    shortcuts = manager.list_all(scope=scope)
    return {"shortcuts": [s.__dict__ for s in shortcuts]}


@router.post("/")
async def update_shortcut(request: UpdateShortcutRequest):
    manager = get_keyboard_manager()
    if not manager.update(request.action, request.key, request.modifiers):
        return {"status": "not_found", "action": request.action}
    return {"status": "updated"}


@router.post("/reset")
async def reset_shortcuts():
    manager = get_keyboard_manager()
    manager.reset()
    return {"status": "reset"}
