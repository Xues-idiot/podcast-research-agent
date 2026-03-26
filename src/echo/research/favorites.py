"""研究结果收藏夹 - 收藏和整理喜欢的研究结果"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class FavoriteItem:
    """收藏项"""
    id: str = ""
    research_id: str = ""
    title: str = ""
    source: str = ""
    platform: str = ""
    notes: str = ""  # 用户笔记
    tags: list = field(default_factory=list)
    created_at: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(self.research_id.encode()).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


@dataclass
class FavoriteCollection:
    """收藏集合"""
    id: str = ""
    name: str = ""
    description: str = ""
    items: list = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(self.name.encode()).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = self.created_at


class FavoritesManager:
    """收藏夹管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化收藏管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "favorites"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._favorites_file = self.storage_path / "favorites.json"
        self._collections_file = self.storage_path / "collections.json"
        self._favorites: dict[str, FavoriteItem] = {}
        self._collections: dict[str, FavoriteCollection] = {}
        self._load()

    def _load(self):
        """加载收藏数据"""
        if self._favorites_file.exists():
            try:
                with open(self._favorites_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for item_data in data.values():
                        self._favorites[item_data["id"]] = FavoriteItem(**item_data)
            except (json.JSONDecodeError, KeyError):
                self._favorites = {}

        if self._collections_file.exists():
            try:
                with open(self._collections_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for coll_data in data.values():
                        self._collections[coll_data["id"]] = FavoriteCollection(**coll_data)
            except (json.JSONDecodeError, KeyError):
                self._collections = {}

    def _save(self):
        """保存收藏数据"""
        data = {fid: item.__dict__ for fid, item in self._favorites.items()}
        temp_file = self._favorites_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._favorites_file)

        data = {cid: coll.__dict__ for cid, coll in self._collections.items()}
        temp_file = self._collections_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._collections_file)

    def add(
        self,
        research_id: str,
        title: str = "",
        source: str = "",
        platform: str = "",
        tags: list = None,
    ) -> FavoriteItem:
        """添加收藏

        Args:
            research_id: 研究ID
            title: 标题
            source: 来源
            platform: 平台
            tags: 标签

        Returns:
            收藏项
        """
        # 检查是否已收藏
        for item in self._favorites.values():
            if item.research_id == research_id:
                return item

        item = FavoriteItem(
            research_id=research_id,
            title=title or research_id,
            source=source,
            platform=platform,
            tags=tags or [],
        )
        self._favorites[item.id] = item
        self._save()
        return item

    def remove(self, favorite_id: str) -> bool:
        """移除收藏"""
        if favorite_id in self._favorites:
            # 从所有集合中移除
            for coll in self._collections.values():
                if favorite_id in coll.items:
                    coll.items.remove(favorite_id)
            del self._favorites[favorite_id]
            self._save()
            return True
        return False

    def get(self, favorite_id: str) -> Optional[FavoriteItem]:
        """获取收藏项"""
        return self._favorites.get(favorite_id)

    def get_by_research_id(self, research_id: str) -> Optional[FavoriteItem]:
        """通过研究ID获取收藏"""
        for item in self._favorites.values():
            if item.research_id == research_id:
                return item
        return None

    def list_all(self) -> list[FavoriteItem]:
        """列出所有收藏"""
        return sorted(
            self._favorites.values(),
            key=lambda x: x.created_at,
            reverse=True
        )

    def list_by_tag(self, tag: str) -> list[FavoriteItem]:
        """按标签筛选"""
        return [
            item for item in self._favorites.values()
            if tag in item.tags
        ]

    def list_by_platform(self, platform: str) -> list[FavoriteItem]:
        """按平台筛选"""
        return [
            item for item in self._favorites.values()
            if item.platform == platform
        ]

    def update_notes(self, favorite_id: str, notes: str) -> bool:
        """更新笔记"""
        item = self._favorites.get(favorite_id)
        if item:
            item.notes = notes
            self._save()
            return True
        return False

    def update_tags(self, favorite_id: str, tags: list) -> bool:
        """更新标签"""
        item = self._favorites.get(favorite_id)
        if item:
            item.tags = tags
            self._save()
            return True
        return False

    def add_tag(self, favorite_id: str, tag: str) -> bool:
        """添加标签"""
        item = self._favorites.get(favorite_id)
        if item and tag not in item.tags:
            item.tags.append(tag)
            self._save()
            return True
        return False

    def remove_tag(self, favorite_id: str, tag: str) -> bool:
        """移除标签"""
        item = self._favorites.get(favorite_id)
        if item and tag in item.tags:
            item.tags.remove(tag)
            self._save()
            return True
        return False

    # 集合管理
    def create_collection(
        self,
        name: str,
        description: str = "",
    ) -> FavoriteCollection:
        """创建收藏集合"""
        coll = FavoriteCollection(
            name=name,
            description=description,
        )
        self._collections[coll.id] = coll
        self._save()
        return coll

    def delete_collection(self, collection_id: str) -> bool:
        """删除收藏集合"""
        if collection_id in self._collections:
            del self._collections[collection_id]
            self._save()
            return True
        return False

    def add_to_collection(self, collection_id: str, favorite_id: str) -> bool:
        """添加收藏到集合"""
        coll = self._collections.get(collection_id)
        item = self._favorites.get(favorite_id)
        if coll and item and favorite_id not in coll.items:
            coll.items.append(favorite_id)
            coll.updated_at = datetime.now().isoformat()
            self._save()
            return True
        return False

    def remove_from_collection(self, collection_id: str, favorite_id: str) -> bool:
        """从集合移除收藏"""
        coll = self._collections.get(collection_id)
        if coll and favorite_id in coll.items:
            coll.items.remove(favorite_id)
            coll.updated_at = datetime.now().isoformat()
            self._save()
            return True
        return False

    def list_collections(self) -> list[FavoriteCollection]:
        """列出所有收藏集合"""
        return sorted(
            self._collections.values(),
            key=lambda x: x.updated_at,
            reverse=True
        )

    def get_collection(self, collection_id: str) -> Optional[FavoriteCollection]:
        """获取收藏集合"""
        return self._collections.get(collection_id)

    def get_collection_items(self, collection_id: str) -> list[FavoriteItem]:
        """获取集合中的所有收藏"""
        coll = self._collections.get(collection_id)
        if not coll:
            return []
        return [
            self._favorites[fid]
            for fid in coll.items
            if fid in self._favorites
        ]

    def get_all_tags(self) -> list[str]:
        """获取所有标签"""
        tags = set()
        for item in self._favorites.values():
            tags.update(item.tags)
        return sorted(tags)


# 全局实例
_favorites_manager: Optional[FavoritesManager] = None


def get_favorites_manager() -> FavoritesManager:
    """获取全局收藏管理器"""
    global _favorites_manager
    if _favorites_manager is None:
        _favorites_manager = FavoritesManager()
    return _favorites_manager
