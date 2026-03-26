"""研究历史版本控制 - 版本管理和回滚"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Version:
    """研究版本"""
    id: str = ""
    research_id: str = ""
    version_number: int = 1
    data: dict = field(default_factory=dict)  # 完整研究数据
    diff_summary: str = ""  # 变更摘要
    created_at: str = ""
    created_by: str = "system"  # 创建者
    is_auto_save: bool = False  # 是否自动保存

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(
                f"{self.research_id}:{self.version_number}".encode()
            ).hexdigest()[:12]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class VersionManager:
    """版本管理器"""

    # 最大保存版本数
    MAX_VERSIONS = 50

    def __init__(self, storage_path: Optional[str] = None):
        """初始化版本管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "versions"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._versions_dir = self.storage_path / "versions"
        self._versions_dir.mkdir(exist_ok=True)
        self._index_file = self.storage_path / "index.json"
        self._index: dict[str, list] = {}  # research_id -> [version_ids]
        self._load()

    def _load(self):
        """加载索引"""
        if self._index_file.exists():
            try:
                with open(self._index_file, "r", encoding="utf-8") as f:
                    self._index = json.load(f)
            except json.JSONDecodeError:
                self._index = {}

    def _save_index(self):
        """保存索引"""
        temp_file = self._index_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._index, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._index_file)

    def _get_version_file(self, version_id: str) -> Path:
        """获取版本文件路径"""
        return self._versions_dir / f"{version_id}.json"

    def save(
        self,
        research_id: str,
        data: dict,
        diff_summary: str = "",
        created_by: str = "system",
        is_auto_save: bool = False,
    ) -> Version:
        """保存版本

        Args:
            research_id: 研究ID
            data: 研究数据
            diff_summary: 变更摘要
            created_by: 创建者
            is_auto_save: 是否自动保存

        Returns:
            版本
        """
        # 获取下一个版本号
        version_ids = self._index.get(research_id, [])
        if version_ids:
            # 读取最新版本获取版本号
            latest_file = self._get_version_file(version_ids[-1])
            if latest_file.exists():
                with open(latest_file, "r", encoding="utf-8") as f:
                    latest = json.load(f)
                    next_version = latest.get("version_number", 0) + 1
            else:
                next_version = 1
        else:
            next_version = 1

        version = Version(
            research_id=research_id,
            version_number=next_version,
            data=data,
            diff_summary=diff_summary,
            created_by=created_by,
            is_auto_save=is_auto_save,
        )

        # 保存版本文件
        version_file = self._get_version_file(version.id)
        with open(version_file, "w", encoding="utf-8") as f:
            json.dump(version.__dict__, f, ensure_ascii=False, indent=2)

        # 更新索引
        if research_id not in self._index:
            self._index[research_id] = []
        self._index[research_id].append(version.id)

        # 限制版本数量
        if len(self._index[research_id]) > self.MAX_VERSIONS:
            old_versions = self._index[research_id][:-self.MAX_VERSIONS]
            for old_id in old_versions:
                old_file = self._get_version_file(old_id)
                if old_file.exists():
                    old_file.unlink()
            self._index[research_id] = self._index[research_id][-self.MAX_VERSIONS:]

        self._save_index()
        return version

    def get(self, version_id: str) -> Optional[Version]:
        """获取版本"""
        version_file = self._get_version_file(version_id)
        if not version_file.exists():
            return None

        with open(version_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return Version(**data)

    def get_latest(self, research_id: str) -> Optional[Version]:
        """获取最新版本"""
        version_ids = self._index.get(research_id, [])
        if not version_ids:
            return None
        return self.get(version_ids[-1])

    def get_versions(
        self,
        research_id: str,
        limit: int = 20,
        include_auto_save: bool = False,
    ) -> list[Version]:
        """获取版本列表

        Args:
            research_id: 研究ID
            limit: 数量限制
            include_auto_save: 是否包含自动保存

        Returns:
            版本列表
        """
        version_ids = self._index.get(research_id, [])
        versions = []

        for vid in reversed(version_ids):
            version = self.get(vid)
            if version:
                if version.is_auto_save and not include_auto_save:
                    continue
                versions.append(version)
                if len(versions) >= limit:
                    break

        return versions

    def rollback(self, version_id: str) -> Optional[dict]:
        """回滚到指定版本

        Args:
            version_id: 版本ID

        Returns:
            回滚后的数据
        """
        version = self.get(version_id)
        if not version:
            return None

        # 创建新版本记录回滚操作
        current = self.get_latest(version.research_id)
        if current:
            diff_summary = f"回滚到版本 {version.version_number}"
        else:
            diff_summary = f"初始版本（从版本 {version.version_number} 恢复）"

        self.save(
            research_id=version.research_id,
            data=version.data,
            diff_summary=diff_summary,
            created_by="rollback",
        )

        return version.data

    def compare(self, version_id_1: str, version_id_2: str) -> dict:
        """比较两个版本

        Args:
            version_id_1: 版本1
            version_id_2: 版本2

        Returns:
            差异信息
        """
        v1 = self.get(version_id_1)
        v2 = self.get(version_id_2)

        if not v1 or not v2:
            return {"error": "Version not found"}

        # 简单比较：检查关键字段变化
        changes = {
            "version1": v1.version_number,
            "version2": v2.version_number,
            "timestamp1": v1.created_at,
            "timestamp2": v2.created_at,
            "diffs": [],
        }

        # 比较summary
        if v1.data.get("summary", {}).get("content") != v2.data.get("summary", {}).get("content"):
            changes["diffs"].append({"field": "summary", "changed": True})

        # 比较keypoints数量
        if len(v1.data.get("keypoints", [])) != len(v2.data.get("keypoints", [])):
            changes["diffs"].append({
                "field": "keypoints",
                "count1": len(v1.data.get("keypoints", [])),
                "count2": len(v2.data.get("keypoints", [])),
            })

        return changes

    def delete_before(self, research_id: str, before_version: int) -> int:
        """删除指定版本之前的所有版本

        Args:
            research_id: 研究ID
            before_version: 版本号

        Returns:
            删除数量
        """
        version_ids = self._index.get(research_id, [])
        to_delete = []
        kept = []

        for vid in version_ids:
            version = self.get(vid)
            if version:
                if version.version_number < before_version:
                    to_delete.append(vid)
                else:
                    kept.append(vid)

        # 删除文件
        for vid in to_delete:
            version_file = self._get_version_file(vid)
            if version_file.exists():
                version_file.unlink()

        self._index[research_id] = kept
        self._save_index()

        return len(to_delete)

    def get_stats(self) -> dict:
        """获取版本统计"""
        total_versions = sum(len(versions) for versions in self._index.values())
        total_researches = len(self._index)

        return {
            "total_versions": total_versions,
            "total_researches": total_researches,
            "avg_versions_per_research": (
                total_versions / total_researches if total_researches > 0 else 0
            ),
        }


# 全局实例
_version_manager: Optional[VersionManager] = None


def get_version_manager() -> VersionManager:
    """获取全局版本管理器"""
    global _version_manager
    if _version_manager is None:
        _version_manager = VersionManager()
    return _version_manager
