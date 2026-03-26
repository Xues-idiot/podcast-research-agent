"""研究任务队列 - 批量处理研究任务"""

import asyncio
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional


class QueueStatus(Enum):
    """队列状态"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class QueuePriority(Enum):
    """队列优先级"""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    URGENT = 4


@dataclass
class QueueItem:
    """队列项"""
    id: str = ""
    research_id: str = ""
    url: str = ""
    title: str = ""
    status: QueueStatus = QueueStatus.PENDING
    priority: QueuePriority = QueuePriority.NORMAL
    progress: float = 0.0  # 0.0 - 1.0
    error: str = ""
    created_at: str = ""
    started_at: str = ""
    completed_at: str = ""
    result: dict = field(default_factory=dict)  # 研究结果

    def __post_init__(self):
        if not self.id:
            self.id = f"q_{datetime.now().timestamp()}"
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class ResearchQueue:
    """研究任务队列"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化队列"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "queue"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._queue_file = self.storage_path / "queue.json"
        self._items: list[QueueItem] = []
        self._running = False
        self._load()

    def _load(self):
        """加载队列"""
        if self._queue_file.exists():
            try:
                with open(self._queue_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for item_data in data:
                        item_data["status"] = QueueStatus(item_data["status"])
                        item_data["priority"] = QueuePriority(item_data["priority"])
                        self._items.append(QueueItem(**item_data))
            except (json.JSONDecodeError, KeyError, ValueError):
                self._items = []

    def _save(self):
        """保存队列"""
        data = [
            {
                **item.__dict__,
                "status": item.status.value,
                "priority": item.priority.value,
            }
            for item in self._items
        ]
        temp_file = self._queue_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._queue_file)

    def add(
        self,
        url: str,
        title: str = "",
        priority: QueuePriority = QueuePriority.NORMAL,
    ) -> QueueItem:
        """添加队列项

        Args:
            url: 播客URL
            title: 标题
            priority: 优先级

        Returns:
            队列项
        """
        item = QueueItem(
            url=url,
            title=title or url,
            priority=priority,
        )
        self._items.append(item)
        self._sort()
        self._save()
        return item

    def _sort(self):
        """按优先级排序"""
        self._items.sort(
            key=lambda x: (
                -x.priority.value,
                datetime.fromisoformat(x.created_at).timestamp()
            )
        )

    def get_next(self) -> Optional[QueueItem]:
        """获取下一个待处理项"""
        for item in self._items:
            if item.status == QueueStatus.PENDING:
                return item
        return None

    def mark_running(self, item_id: str) -> bool:
        """标记为运行中"""
        for item in self._items:
            if item.id == item_id and item.status == QueueStatus.PENDING:
                item.status = QueueStatus.RUNNING
                item.started_at = datetime.now().isoformat()
                self._save()
                return True
        return False

    def mark_completed(self, item_id: str, result: dict = None):
        """标记为完成"""
        for item in self._items:
            if item.id == item_id and item.status == QueueStatus.RUNNING:
                item.status = QueueStatus.COMPLETED
                item.completed_at = datetime.now().isoformat()
                item.progress = 1.0
                if result:
                    item.result = result
                self._save()
                return True
        return False

    def mark_failed(self, item_id: str, error: str):
        """标记为失败"""
        for item in self._items:
            if item.id == item_id and item.status == QueueStatus.RUNNING:
                item.status = QueueStatus.FAILED
                item.completed_at = datetime.now().isoformat()
                item.error = error
                self._save()
                return True
        return False

    def update_progress(self, item_id: str, progress: float):
        """更新进度"""
        for item in self._items:
            if item.id == item_id:
                item.progress = min(1.0, max(0.0, progress))
                self._save()
                return True
        return False

    def cancel(self, item_id: str) -> bool:
        """取消队列项"""
        for item in self._items:
            if item.id == item_id and item.status == QueueStatus.PENDING:
                item.status = QueueStatus.CANCELLED
                item.completed_at = datetime.now().isoformat()
                self._save()
                return True
        return False

    def retry(self, item_id: str) -> bool:
        """重试失败的队列项"""
        for item in self._items:
            if item.id == item_id and item.status in [QueueStatus.FAILED, QueueStatus.CANCELLED]:
                item.status = QueueStatus.PENDING
                item.error = ""
                item.completed_at = ""
                item.progress = 0.0
                self._sort()
                self._save()
                return True
        return False

    def remove(self, item_id: str) -> bool:
        """移除队列项"""
        for i, item in enumerate(self._items):
            if item.id == item_id:
                del self._items[i]
                self._save()
                return True
        return False

    def list(
        self,
        status: Optional[QueueStatus] = None,
        limit: int = 50,
    ) -> list[QueueItem]:
        """列出队列项"""
        items = self._items
        if status:
            items = [i for i in items if i.status == status]
        return items[:limit]

    def get_stats(self) -> dict:
        """获取队列统计"""
        stats = {
            "total": len(self._items),
            "pending": 0,
            "running": 0,
            "completed": 0,
            "failed": 0,
            "cancelled": 0,
        }
        for item in self._items:
            if item.status == QueueStatus.PENDING:
                stats["pending"] += 1
            elif item.status == QueueStatus.RUNNING:
                stats["running"] += 1
            elif item.status == QueueStatus.COMPLETED:
                stats["completed"] += 1
            elif item.status == QueueStatus.FAILED:
                stats["failed"] += 1
            elif item.status == QueueStatus.CANCELLED:
                stats["cancelled"] += 1
        return stats

    def clear_completed(self):
        """清除已完成的项"""
        self._items = [
            i for i in self._items
            if i.status not in [QueueStatus.COMPLETED, QueueStatus.CANCELLED]
        ]
        self._save()

    async def process(
        self,
        process_func,  # 实际处理函数
        max_concurrent: int = 2,
    ):
        """处理队列

        Args:
            process_func: 处理函数，接收(url)并返回result
            max_concurrent: 最大并发数
        """
        self._running = True
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process_item(item: QueueItem):
            async with semaphore:
                self.mark_running(item.id)
                try:
                    result = await process_func(item.url)
                    self.mark_completed(item.id, result)
                except Exception as e:
                    self.mark_failed(item.id, str(e))

        while self._running:
            # 获取所有待处理的项
            pending = [i for i in self._items if i.status == QueueStatus.PENDING]
            if not pending:
                break

            # 并发处理
            tasks = [process_item(item) for item in pending[:max_concurrent]]
            await asyncio.gather(*tasks, return_exceptions=True)

        self._running = False

    def stop(self):
        """停止队列处理"""
        self._running = False


# 全局实例
_research_queue: Optional[ResearchQueue] = None


def get_research_queue() -> ResearchQueue:
    """获取全局研究队列"""
    global _research_queue
    if _research_queue is None:
        _research_queue = ResearchQueue()
    return _research_queue
