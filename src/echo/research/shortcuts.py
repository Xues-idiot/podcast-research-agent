"""快捷操作定义 - 定义常用操作的快捷方式"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ActionType(Enum):
    """操作类型"""
    RESEARCH = "research"  # 开始研究
    EXPORT = "export"  # 导出
    NAVIGATE = "navigate"  # 导航
    SEARCH = "search"  # 搜索
    ACTION = "action"  # 执行动作


@dataclass
class Shortcut:
    """快捷操作"""
    id: str
    name: str
    description: str
    action_type: ActionType
    action: str  # 操作标识
    params: dict = field(default_factory=dict)  # 操作参数
    icon: str = ""  # 图标


# 预设快捷操作
DEFAULT_SHORTCUTS = [
    Shortcut(
        id="quick_research",
        name="快速研究",
        description="输入URL快速开始研究",
        action_type=ActionType.RESEARCH,
        action="start_research",
        icon="play",
    ),
    Shortcut(
        id="export_all",
        name="导出全部",
        description="导出当前研究的所有格式",
        action_type=ActionType.EXPORT,
        action="export_all",
        icon="download",
    ),
    Shortcut(
        id="go_home",
        name="返回首页",
        description="返回首页",
        action_type=ActionType.NAVIGATE,
        action="navigate",
        params={"path": "/"},
        icon="home",
    ),
    Shortcut(
        id="go_history",
        name="研究历史",
        description="查看研究历史",
        action_type=ActionType.NAVIGATE,
        action="navigate",
        params={"path": "/history"},
        icon="clock",
    ),
    Shortcut(
        id="go_knowledge",
        name="知识库",
        description="查看知识库",
        action_type=ActionType.NAVIGATE,
        action="navigate",
        params={"path": "/knowledge"},
        icon="book",
    ),
    Shortcut(
        id="global_search",
        name="全局搜索",
        description="打开全局搜索",
        action_type=ActionType.SEARCH,
        action="open_search",
        icon="search",
    ),
    Shortcut(
        id="copy_summary",
        name="复制摘要",
        description="复制当前研究的摘要到剪贴板",
        action_type=ActionType.ACTION,
        action="copy_summary",
        icon="copy",
    ),
    Shortcut(
        id="toggle_theme",
        name="切换主题",
        description="切换浅色/深色主题",
        action_type=ActionType.ACTION,
        action="toggle_theme",
        icon="moon",
    ),
    Shortcut(
        id="refresh_research",
        name="刷新研究",
        description="刷新当前研究结果",
        action_type=ActionType.ACTION,
        action="refresh",
        icon="refresh",
    ),
]


class ShortcutManager:
    """快捷操作管理器"""

    def __init__(self):
        """初始化管理器"""
        self._shortcuts = {s.id: s for s in DEFAULT_SHORTCUTS}

    def get_all(self) -> list[Shortcut]:
        """获取所有快捷操作"""
        return list(self._shortcuts.values())

    def get(self, shortcut_id: str) -> Optional[Shortcut]:
        """获取快捷操作"""
        return self._shortcuts.get(shortcut_id)

    def add(self, shortcut: Shortcut) -> bool:
        """添加快捷操作"""
        if shortcut.id in self._shortcuts:
            return False
        self._shortcuts[shortcut.id] = shortcut
        return True

    def remove(self, shortcut_id: str) -> bool:
        """移除快捷操作"""
        if shortcut_id in self._shortcuts:
            del self._shortcuts[shortcut_id]
            return True
        return False

    def execute(self, shortcut_id: str) -> dict:
        """执行快捷操作

        Args:
            shortcut_id: 快捷操作ID

        Returns:
            执行结果
        """
        shortcut = self._shortcuts.get(shortcut_id)
        if not shortcut:
            return {"success": False, "error": "Shortcut not found"}

        # 返回操作信息
        return {
            "success": True,
            "action": shortcut.action,
            "params": shortcut.params,
        }


# 全局实例
_shortcut_manager: Optional[ShortcutManager] = None


def get_shortcut_manager() -> ShortcutManager:
    """获取全局快捷操作管理器"""
    global _shortcut_manager
    if _shortcut_manager is None:
        _shortcut_manager = ShortcutManager()
    return _shortcut_manager
