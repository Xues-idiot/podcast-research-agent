"""研究进度追踪器"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


class ProgressTracker:
    """研究进度追踪器"""

    STEPS = [
        "init",       # 初始化
        "download",    # 下载
        "transcribe", # 转录
        "summary",    # 摘要
        "keypoints",  # 要点
        "mindmap",    # 思维导图
        "qa",         # 问答
        "export",     # 导出
        "done",       # 完成
    ]

    def __init__(self, storage_path: Optional[str] = None):
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "progress"
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._progress_file = self.storage_path / "progress.json"
        self._progress: dict = {}
        self._load()

    def _load(self):
        if self._progress_file.exists():
            try:
                with open(self._progress_file, "r", encoding="utf-8") as f:
                    self._progress = json.load(f)
            except:
                self._progress = {}

    def _save(self):
        with open(self._progress_file, "w", encoding="utf-8") as f:
            json.dump(self._progress, f, ensure_ascii=False, indent=2)

    def start(self, research_id: str):
        self._progress[research_id] = {
            "current_step": "init",
            "steps_completed": [],
            "started_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "percent": 0,
        }
        self._save()

    def update(self, research_id: str, step: str, percent: float = 0):
        if research_id not in self._progress:
            self.start(research_id)

        self._progress[research_id]["current_step"] = step
        self._progress[research_id]["updated_at"] = datetime.now().isoformat()
        self._progress[research_id]["percent"] = percent

        if step in self.STEPS and step not in self._progress[research_id]["steps_completed"]:
            self._progress[research_id]["steps_completed"].append(step)

        self._save()

    def complete(self, research_id: str):
        self.update(research_id, "done", 100)

    def get(self, research_id: str) -> Optional[dict]:
        return self._progress.get(research_id)

    def list_active(self) -> list:
        return [
            {"id": rid, **data}
            for rid, data in self._progress.items()
            if data.get("current_step") != "done"
        ]


_tracker: Optional[ProgressTracker] = None

def get_progress_tracker() -> ProgressTracker:
    global _tracker
    if _tracker is None:
        _tracker = ProgressTracker()
    return _tracker
