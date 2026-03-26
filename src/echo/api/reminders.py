"""提醒API"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.reminders import (
    ReminderType,
    ReminderStatus,
    get_reminder_scheduler,
)


router = APIRouter(prefix="/api/reminders", tags=["reminders"])


class CreateReminderRequest(BaseModel):
    """创建提醒请求"""
    title: str
    message: str = ""
    reminder_type: str = "once"
    scheduled_at: str = ""
    repeat_interval_hours: int = 0


@router.get("/")
async def list_reminders(status: Optional[str] = None):
    """列出所有提醒

    Args:
        status: 状态筛选

    Returns:
        提醒列表
    """
    scheduler = get_reminder_scheduler()
    reminders = scheduler.list_all()

    if status:
        try:
            filter_status = ReminderStatus(status)
            reminders = [r for r in reminders if r.status == filter_status]
        except ValueError:
            pass

    return {
        "reminders": [
            {
                **r.__dict__,
                "reminder_type": r.reminder_type.value,
                "status": r.status.value,
            }
            for r in reminders
        ],
        "count": len(reminders),
    }


@router.post("/")
async def create_reminder(request: CreateReminderRequest):
    """创建提醒

    Args:
        request: 提醒信息

    Returns:
        创建的提醒
    """
    scheduler = get_reminder_scheduler()

    try:
        rtype = ReminderType(request.reminder_type)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid reminder type: {request.reminder_type}")

    reminder = scheduler.create(
        title=request.title,
        message=request.message,
        reminder_type=rtype,
        scheduled_at=request.scheduled_at,
        repeat_interval_hours=request.repeat_interval_hours,
    )

    return {
        **reminder.__dict__,
        "reminder_type": reminder.reminder_type.value,
        "status": reminder.status.value,
    }


@router.post("/{reminder_id}/trigger")
async def trigger_reminder(reminder_id: str):
    """触发提醒

    Args:
        reminder_id: 提醒ID

    Returns:
        操作结果
    """
    scheduler = get_reminder_scheduler()
    if not scheduler.trigger(reminder_id):
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"status": "triggered", "reminder_id": reminder_id}


@router.post("/{reminder_id}/pause")
async def pause_reminder(reminder_id: str):
    """暂停提醒

    Args:
        reminder_id: 提醒ID

    Returns:
        操作结果
    """
    scheduler = get_reminder_scheduler()
    if not scheduler.pause(reminder_id):
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"status": "paused", "reminder_id": reminder_id}


@router.post("/{reminder_id}/resume")
async def resume_reminder(reminder_id: str):
    """恢复提醒

    Args:
        reminder_id: 提醒ID

    Returns:
        操作结果
    """
    scheduler = get_reminder_scheduler()
    if not scheduler.resume(reminder_id):
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"status": "resumed", "reminder_id": reminder_id}


@router.delete("/{reminder_id}")
async def cancel_reminder(reminder_id: str):
    """取消提醒

    Args:
        reminder_id: 提醒ID

    Returns:
        操作结果
    """
    scheduler = get_reminder_scheduler()
    if not scheduler.cancel(reminder_id):
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"status": "cancelled", "reminder_id": reminder_id}
