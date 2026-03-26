"""研究结果分享系统 - 生成分享链接和访问控制"""

import hashlib
import json
import secrets
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


@dataclass
class ShareLink:
    """分享链接"""
    id: str = ""
    research_id: str = ""
    token: str = ""
    password: str = ""  # 可选密码保护
    expires_at: str = ""  # 过期时间
    view_count: int = 0  # 查看次数
    max_views: int = 0  # 最大查看次数，0表示不限
    created_at: str = ""
    last_accessed: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = secrets.token_hex(8)
        if not self.token:
            self.token = secrets.token_urlsafe(16)
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def is_expired(self) -> bool:
        """检查是否过期"""
        if not self.expires_at:
            return False
        return datetime.now() > datetime.fromisoformat(self.expires_at)

    def is_maxed(self) -> bool:
        """检查是否达到最大查看次数"""
        if self.max_views <= 0:
            return False
        return self.view_count >= self.max_views

    def can_access(self) -> bool:
        """检查是否可以访问"""
        return not self.is_expired() and not self.is_maxed()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "research_id": self.research_id,
            "token": self.token,
            "has_password": bool(self.password),
            "expires_at": self.expires_at,
            "view_count": self.view_count,
            "max_views": self.max_views,
            "created_at": self.created_at,
            "last_accessed": self.last_accessed,
        }


class ShareManager:
    """分享链接管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化分享管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "shares"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._shares_file = self.storage_path / "shares.json"
        self._research_file = self.storage_path / "research_shares.json"
        self._shares: dict[str, ShareLink] = {}
        self._research_shares: dict[str, str] = {}  # research_id -> share_id
        self._load()

    def _load(self):
        """加载分享数据"""
        if self._shares_file.exists():
            try:
                with open(self._shares_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for share_data in data.values():
                    self._shares[share_data["id"]] = ShareLink(**share_data)
            except (json.JSONDecodeError, KeyError):
                self._shares = {}

        if self._research_file.exists():
            try:
                with open(self._research_file, "r", encoding="utf-8") as f:
                    self._research_shares = json.load(f)
            except json.JSONDecodeError:
                self._research_shares = {}

    def _save(self):
        """保存分享数据"""
        data = {share_id: share.to_dict() for share_id, share in self._shares.items()}
        temp_file = self._shares_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._shares_file)

        temp_file = self._research_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._research_shares, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._research_file)

    def create(
        self,
        research_id: str,
        password: str = "",
        expires_in_hours: int = 168,  # 默认7天
        max_views: int = 0,
    ) -> ShareLink:
        """创建分享链接

        Args:
            research_id: 研究结果ID
            password: 可选密码保护
            expires_in_hours: 过期时间（小时）
            max_views: 最大查看次数，0表示不限

        Returns:
            分享链接
        """
        # 生成分享链接
        share = ShareLink(
            research_id=research_id,
            password=hashlib.sha256(password.encode()).hexdigest() if password else "",
            expires_at=(datetime.now() + timedelta(hours=expires_in_hours)).isoformat(),
            max_views=max_views,
        )

        self._shares[share.id] = share
        self._research_shares[research_id] = share.id
        self._save()
        return share

    def get(self, share_id: str) -> Optional[ShareLink]:
        """获取分享链接"""
        return self._shares.get(share_id)

    def get_by_token(self, token: str) -> Optional[ShareLink]:
        """通过token获取分享链接"""
        for share in self._shares.values():
            if share.token == token:
                return share
        return None

    def get_by_research_id(self, research_id: str) -> Optional[ShareLink]:
        """获取研究结果的分享链接"""
        share_id = self._research_shares.get(research_id)
        if share_id:
            return self._shares.get(share_id)
        return None

    def verify_password(self, share: ShareLink, password: str) -> bool:
        """验证密码"""
        if not share.password:
            return True
        return share.password == hashlib.sha256(password.encode()).hexdigest()

    def record_view(self, share_id: str) -> bool:
        """记录一次访问"""
        share = self._shares.get(share_id)
        if not share or not share.can_access():
            return False

        share.view_count += 1
        share.last_accessed = datetime.now().isoformat()
        self._save()
        return True

    def revoke(self, share_id: str) -> bool:
        """撤销分享链接"""
        if share_id in self._shares:
            share = self._shares[share_id]
            if share.research_id in self._research_shares:
                del self._research_shares[share.research_id]
            del self._shares[share_id]
            self._save()
            return True
        return False

    def list_by_research(self, research_id: str) -> list[ShareLink]:
        """列出某个研究结果的所有分享链接"""
        shares = []
        for share in self._shares.values():
            if share.research_id == research_id:
                shares.append(share)
        return shares

    def cleanup_expired(self):
        """清理过期链接"""
        expired = [
            share_id
            for share_id, share in self._shares.items()
            if share.is_expired()
        ]
        for share_id in expired:
            share = self._shares[share_id]
            if share.research_id in self._research_shares:
                del self._research_shares[share.research_id]
            del self._shares[share_id]
        if expired:
            self._save()
        return len(expired)


# 全局实例
_share_manager: Optional[ShareManager] = None


def get_share_manager() -> ShareManager:
    """获取全局分享管理器"""
    global _share_manager
    if _share_manager is None:
        _share_manager = ShareManager()
    return _share_manager
