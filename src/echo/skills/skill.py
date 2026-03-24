"""技能定义和注册

参考 deer-flow 的 Skills 系统，使用 Markdown 格式定义技能。
"""

import re
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Skill:
    """技能定义

    Attributes:
        name: 技能名称 (唯一标识)
        description: 技能描述 (用于匹配)
        overview: 技能概述
        when_to_use: 使用场景
        workflow: 工作流步骤
        metadata: 其他元数据
        source_file: 源文件路径
        content: 原始内容
    """
    name: str
    description: str
    overview: str = ""
    when_to_use: str = ""
    workflow: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    source_file: str = ""
    content: str = ""

    @classmethod
    def from_markdown(cls, markdown_content: str, source_file: str = "") -> "Skill":
        """从Markdown内容解析技能

        Args:
            markdown_content: Markdown格式的技能定义
            source_file: 源文件路径

        Returns:
            Skill 实例
        """
        # 解析 YAML frontmatter
        frontmatter = {}
        content = markdown_content

        if markdown_content.startswith("---"):
            parts = markdown_content[3:].split("---", 1)
            if len(parts) == 2:
                try:
                    frontmatter = yaml.safe_load(parts[0]) or {}
                    content = parts[1].strip()
                except yaml.YAMLError:
                    content = markdown_content

        # 提取基本信息
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        # 解析 Markdown 内容
        overview = ""
        when_to_use = ""
        workflow = []

        lines = content.split("\n")
        current_section = ""
        current_content = []

        for line in lines:
            line = line.rstrip()

            # 检测章节标题
            if line.startswith("# ") and not line.startswith("## "):
                # 跳过主标题
                continue
            elif line.startswith("## "):
                # 保存上一个章节
                section_content = "\n".join(current_content).strip()
                if current_section == "Overview" or current_section == "概述":
                    overview = section_content
                elif current_section == "When to Use" or current_section == "使用场景":
                    when_to_use = section_content
                elif current_section == "Workflow" or current_section == "工作流":
                    workflow = [l.strip() for l in current_content if l.strip()]

                # 开始新章节
                current_section = line[3:].strip()
                current_content = []
            else:
                current_content.append(line)

        # 保存最后一个章节
        section_content = "\n".join(current_content).strip()
        if current_section == "Overview" or current_section == "概述":
            overview = section_content
        elif current_section == "When to Use" or current_section == "使用场景":
            when_to_use = section_content
        elif current_section == "Workflow" or current_section == "工作流":
            workflow = [l.strip() for l in current_content if l.strip()]

        return cls(
            name=name,
            description=description,
            overview=overview,
            when_to_use=when_to_use,
            workflow=workflow,
            metadata=frontmatter,
            source_file=source_file,
            content=markdown_content,
        )

    def matches_query(self, query: str) -> float:
        """检查技能是否匹配查询

        Args:
            query: 用户查询

        Returns:
            匹配分数 (0-1)
        """
        query_lower = query.lower()
        score = 0.0

        # 检查名称
        if query_lower in self.name.lower():
            score += 0.5

        # 检查描述关键词
        desc_lower = self.description.lower()
        query_words = query_lower.split()

        # 完整查询匹配
        if query_lower in desc_lower:
            score += 0.3

        # 单词匹配
        matched_words = sum(1 for word in query_words if word in desc_lower)
        if query_words:
            score += 0.2 * (matched_words / len(query_words))

        return min(score, 1.0)

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "name": self.name,
            "description": self.description,
            "overview": self.overview,
            "when_to_use": self.when_to_use,
            "workflow": self.workflow,
            "metadata": self.metadata,
            "source_file": self.source_file,
        }


class SkillRegistry:
    """技能注册表

    管理技能的加载、存储和匹配。
    """

    def __init__(self):
        """初始化注册表"""
        self._skills: dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        """注册技能

        Args:
            skill: 技能实例
        """
        if not skill.name:
            raise ValueError("Skill must have a name")
        self._skills[skill.name] = skill

    def get(self, name: str) -> Optional[Skill]:
        """获取技能

        Args:
            name: 技能名称

        Returns:
            技能实例或 None
        """
        return self._skills.get(name)

    def list_skills(self) -> list[Skill]:
        """列出所有技能"""
        return list(self._skills.values())

    def find_best_match(self, query: str, min_score: float = 0.1) -> Optional[Skill]:
        """找到最佳匹配的技能

        Args:
            query: 用户查询
            min_score: 最小匹配分数

        Returns:
            最佳匹配的技能或 None
        """
        best_skill = None
        best_score = 0.0

        for skill in self._skills.values():
            score = skill.matches_query(query)
            if score > best_score:
                best_score = score
                best_skill = skill

        if best_score >= min_score:
            return best_skill
        return None

    def find_all_matches(self, query: str, min_score: float = 0.1) -> list[tuple[Skill, float]]:
        """找到所有匹配的技能

        Args:
            query: 用户查询
            min_score: 最小匹配分数

        Returns:
            (技能, 分数) 列表，按分数降序排列
        """
        matches = []
        for skill in self._skills.values():
            score = skill.matches_query(query)
            if score >= min_score:
                matches.append((skill, score))

        matches.sort(key=lambda x: x[1], reverse=True)
        return matches

    def clear(self) -> None:
        """清除所有技能"""
        self._skills.clear()


def load_skills_from_directory(directory: str) -> SkillRegistry:
    """从目录加载所有技能

    Args:
        directory: 技能文件目录

    Returns:
        填充好的 SkillRegistry
    """
    registry = SkillRegistry()
    dir_path = Path(directory)

    if not dir_path.exists():
        return registry

    # 递归查找所有 SKILL.md 文件
    for skill_file in dir_path.rglob("SKILL.md"):
        try:
            content = skill_file.read_text(encoding="utf-8")
            skill = Skill.from_markdown(content, source_file=str(skill_file))
            if skill.name:
                registry.register(skill)
        except Exception as e:
            print(f"Failed to load skill from {skill_file}: {e}")

    return registry


def load_builtin_skills() -> SkillRegistry:
    """加载内置技能

    内置技能在 echo/skills/ 目录中定义。
    """
    import echo
    skills_dir = Path(echo.__file__).parent / "skills"
    return load_skills_from_directory(str(skills_dir))
