"""快捷操作API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.shortcuts import (
    ActionType,
    Shortcut,
    get_shortcut_manager,
)


router = APIRouter(prefix="/api/shortcuts", tags=["shortcuts"])


class AddShortcutRequest(BaseModel):
    """添加快捷操作请求"""
    id: str
    name: str
    description: str
    action_type: str
    action: str
    params: dict = {}
    icon: str = ""


@router.get("/")
async def list_shortcuts():
    """列出所有快捷操作

    Returns:
        快捷操作列表
    """
    manager = get_shortcut_manager()
    shortcuts = manager.get_all()

    return {
        "shortcuts": [
            {
                **s.__dict__,
                "action_type": s.action_type.value,
            }
            for s in shortcuts
        ],
        "count": len(shortcuts),
    }


@router.get("/{shortcut_id}")
async def get_shortcut(shortcut_id: str):
    """获取快捷操作详情

    Args:
        shortcut_id: 快捷操作ID

    Returns:
        快捷操作详情
    """
    manager = get_shortcut_manager()
    shortcut = manager.get(shortcut_id)
    if not shortcut:
        raise HTTPException(status_code=404, detail="Shortcut not found")

    return {
        **shortcut.__dict__,
        "action_type": shortcut.action_type.value,
    }


@router.post("/")
async def add_shortcut(request: AddShortcutRequest):
    """添加快捷操作

    Args:
        request: 快捷操作信息

    Returns:
        添加结果
    """
    manager = get_shortcut_manager()

    try:
        action_type = ActionType(request.action_type)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid action type: {request.action_type}")

    shortcut = Shortcut(
        id=request.id,
        name=request.name,
        description=request.description,
        action_type=action_type,
        action=request.action,
        params=request.params,
        icon=request.icon,
    )

    if not manager.add(shortcut):
        raise HTTPException(status_code=400, detail="Shortcut already exists")

    return {
        **shortcut.__dict__,
        "action_type": shortcut.action_type.value,
    }


@router.delete("/{shortcut_id}")
async def remove_shortcut(shortcut_id: str):
    """移除快捷操作

    Args:
        shortcut_id: 快捷操作ID

    Returns:
        操作结果
    """
    manager = get_shortcut_manager()
    if not manager.remove(shortcut_id):
        raise HTTPException(status_code=404, detail="Shortcut not found")
    return {"status": "removed", "shortcut_id": shortcut_id}


@router.post("/{shortcut_id}/execute")
async def execute_shortcut(shortcut_id: str):
    """执行快捷操作

    Args:
        shortcut_id: 快捷操作ID

    Returns:
        执行结果
    """
    manager = get_shortcut_manager()
    result = manager.execute(shortcut_id)
    if not result.get("success"):
        raise HTTPException(status_code=404, detail=result.get("error"))
    return result
