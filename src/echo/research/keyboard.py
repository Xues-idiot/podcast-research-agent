"""键盘快捷键系统"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class KeyboardShortcut:
    """键盘快捷键"""
    key: str
    modifiers: list = None
    action: str = ""
    description: str = ""
    scope: str = "global"  # global, research, chat

    def __post_init__(self):
        if self.modifiers is None:
            self.modifiers = []


class KeyboardManager:
    """键盘快捷键管理器"""

    DEFAULT_SHORTCUTS = [
        KeyboardShortcut(key="k", modifiers=["ctrl"], action="search", description="打开搜索", scope="global"),
        KeyboardShortcut(key="/", modifiers=[], action="focus_search", description="聚焦搜索", scope="global"),
        KeyboardShortcut(key="j", modifiers=[], action="scroll_down", description="向下滚动", scope="global"),
        KeyboardShortcut(key="k", modifiers=[], action="scroll_up", description="向上滚动", scope="global"),
        KeyboardShortcut(key="Escape", modifiers=[], action="go_back", description="返回/取消", scope="global"),
        KeyboardShortcut(key="n", modifiers=["ctrl"], action="new_research", description="新建研究", scope="global"),
        KeyboardShortcut(key="s", modifiers=["ctrl"], action="export", description="导出", scope="research"),
        KeyboardShortcut(key="c", modifiers=["ctrl"], action="copy", description="复制", scope="research"),
        KeyboardShortcut(key="?", modifiers=[], action="show_help", description="显示帮助", scope="global"),
        KeyboardShortcut(key="Tab", modifiers=[], action="next_tab", description="下一个标签", scope="global"),
        KeyboardShortcut(key="ArrowUp", modifiers=["alt"], action="prev_tab", description="上一个标签", scope="global"),
    ]

    def __init__(self, storage_path: Optional[str] = None):
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "keyboard"
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._shortcuts_file = self.storage_path / "shortcuts.json"
        self._shortcuts: dict[str, KeyboardShortcut] = {}
        self._load()

    def _load(self):
        if self._shortcuts_file.exists():
            try:
                with open(self._shortcuts_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for key_id, sdata in data.items():
                        self._shortcuts[key_id] = KeyboardShortcut(**sdata)
            except:
                self._shortcuts = {s.action: s for s in self.DEFAULT_SHORTCUTS}
        else:
            self._shortcuts = {s.action: s for s in self.DEFAULT_SHORTCUTS}

    def _save(self):
        data = {action: s.__dict__ for action, s in self._shortcuts.items()}
        with open(self._shortcuts_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get(self, action: str) -> Optional[KeyboardShortcut]:
        return self._shortcuts.get(action)

    def list_all(self, scope: str = None) -> list[KeyboardShortcut]:
        shortcuts = list(self._shortcuts.values())
        if scope:
            shortcuts = [s for s in shortcuts if s.scope == scope]
        return shortcuts

    def update(self, action: str, key: str, modifiers: list = None) -> bool:
        if action in self._shortcuts:
            self._shortcuts[action].key = key
            self._shortcuts[action].modifiers = modifiers or []
            self._save()
            return True
        return False

    def reset(self):
        self._shortcuts = {s.action: s for s in self.DEFAULT_SHORTCUTS}
        self._save()


_keyboard_manager: Optional[KeyboardManager] = None

def get_keyboard_manager() -> KeyboardManager:
    global _keyboard_manager
    if _keyboard_manager is None:
        _keyboard_manager = KeyboardManager()
    return _keyboard_manager
