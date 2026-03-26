"""研究自动保存系统"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


class AutoSave:
    """自动保存器"""

    def __init__(self, storage_path: Optional[str] = None):
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "autosave"
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._drafts_file = self.storage_path / "drafts.json"
        self._drafts: dict = {}
        self._load()

    def _load(self):
        if self._drafts_file.exists():
            try:
                with open(self._drafts_file, "r", encoding="utf-8") as f:
                    self._drafts = json.load(f)
            except:
                self._drafts = {}

    def _save(self):
        with open(self._drafts_file, "w", encoding="utf-8") as f:
            json.dump(self._drafts, f, ensure_ascii=False, indent=2)

    def save_draft(self, research_id: str, data: dict):
        self._drafts[research_id] = {
            "data": data,
            "saved_at": datetime.now().isoformat(),
        }
        self._save()

    def get_draft(self, research_id: str) -> Optional[dict]:
        return self._drafts.get(research_id, {}).get("data")

    def delete_draft(self, research_id: str) -> bool:
        if research_id in self._drafts:
            del self._drafts[research_id]
            self._save()
            return True
        return False

    def list_drafts(self) -> list:
        return [
            {"id": rid, "saved_at": d["saved_at"]}
            for rid, d in self._drafts.items()
        ]


_autosave: Optional[AutoSave] = None

def get_autosave() -> AutoSave:
    global _autosave
    if _autosave is None:
        _autosave = AutoSave()
    return _autosave
