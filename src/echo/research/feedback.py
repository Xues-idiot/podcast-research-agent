"""用户反馈系统"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Feedback:
    """用户反馈"""
    id: str
    type: str  # bug, feature, general
    content: str
    rating: int = 0  # 1-5
    created_at: str = ""


@dataclass
class BugReport:
    """Bug报告"""
    id: str
    description: str
    steps: str = ""
    severity: str = "medium"  # low, medium, high, critical
    status: str = "open"  # open, investigating, fixed, closed
    created_at: str = ""


class FeedbackManager:
    """反馈管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "feedback"
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._feedback_file = self.storage_path / "feedback.json"
        self._bugs_file = self.storage_path / "bugs.json"
        self._feedback: list = []
        self._bugs: dict = {}
        self._load()

    def _load(self):
        if self._feedback_file.exists():
            try:
                with open(self._feedback_file, "r", encoding="utf-8") as f:
                    self._feedback = json.load(f)
            except:
                self._feedback = []
        if self._bugs_file.exists():
            try:
                with open(self._bugs_file, "r", encoding="utf-8") as f:
                    self._bugs = json.load(f)
            except:
                self._bugs = {}

    def _save_feedback(self):
        with open(self._feedback_file, "w", encoding="utf-8") as f:
            json.dump(self._feedback, f, ensure_ascii=False, indent=2)

    def _save_bugs(self):
        with open(self._bugs_file, "w", encoding="utf-8") as f:
            json.dump(self._bugs, f, ensure_ascii=False, indent=2)

    def add_feedback(self, feedback_type: str, content: str, rating: int = 0) -> dict:
        fb = {
            "id": f"fb_{datetime.now().timestamp()}",
            "type": feedback_type,
            "content": content,
            "rating": rating,
            "created_at": datetime.now().isoformat(),
        }
        self._feedback.append(fb)
        self._save_feedback()
        return fb

    def add_bug(self, description: str, steps: str = "", severity: str = "medium") -> dict:
        bug_id = f"bug_{datetime.now().timestamp()}"
        bug = {
            "id": bug_id,
            "description": description,
            "steps": steps,
            "severity": severity,
            "status": "open",
            "created_at": datetime.now().isoformat(),
        }
        self._bugs[bug_id] = bug
        self._save_bugs()
        return bug

    def update_bug_status(self, bug_id: str, status: str) -> bool:
        if bug_id in self._bugs:
            self._bugs[bug_id]["status"] = status
            self._save_bugs()
            return True
        return False

    def list_feedback(self) -> list:
        return sorted(self._feedback, key=lambda x: x.get("created_at", ""), reverse=True)

    def list_bugs(self, status: str = None) -> list:
        bugs = list(self._bugs.values())
        if status:
            bugs = [b for b in bugs if b.get("status") == status]
        return sorted(bugs, key=lambda x: x.get("created_at", ""), reverse=True)

    def get_stats(self) -> dict:
        return {
            "total_feedback": len(self._feedback),
            "total_bugs": len(self._bugs),
            "open_bugs": sum(1 for b in self._bugs.values() if b.get("status") == "open"),
            "closed_bugs": sum(1 for b in self._bugs.values() if b.get("status") == "closed"),
        }


_feedback_manager: Optional[FeedbackManager] = None

def get_feedback_manager() -> FeedbackManager:
    global _feedback_manager
    if _feedback_manager is None:
        _feedback_manager = FeedbackManager()
    return _feedback_manager
