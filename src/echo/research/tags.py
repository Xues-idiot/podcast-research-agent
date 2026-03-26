"""自动标签系统 - 根据内容自动生成标签"""

import re
from collections import Counter
from dataclasses import dataclass
from typing import Optional


@dataclass
class Tag:
    """标签"""
    name: str
    count: int = 1
    source: str = ""  # 来源：keyword, ai, topic


class AutoTagger:
    """自动标签生成器"""

    # 预设关键词映射
    KEYWORD_TAGS = {
        "ai": ["人工智能", "AI", "大模型", "LLM", "ChatGPT", "GPT", "机器学习"],
        "tech": ["技术", "编程", "代码", "开发", "架构", "系统", "算法"],
        "business": ["商业", "创业", "投资", "融资", "上市", "市场", "营销"],
        "science": ["科学", "研究", "实验", "数据", "分析", "物理", "化学"],
        "society": ["社会", "文化", "教育", "医疗", "健康", "政治", "经济"],
        "design": ["设计", "产品", "UX", "UI", "用户体验", "界面", "创意"],
        "career": ["职业", "职场", "面试", "简历", "晋升", "加薪", "管理"],
        "finance": ["金融", "股票", "基金", "债券", "银行", "保险", "理财"],
    }

    # 话题模式
    TOPIC_PATTERNS = [
        (r"(?i)interview|访谈|对话|采访", "interview"),
        (r"(?i)news|新闻|资讯|动态", "news"),
        (r"(?i)tutorial|教程|入门|基础|教学", "tutorial"),
        (r"(?i)discussion|讨论|辩论|圆桌", "discussion"),
        (r"(?i)story|故事|案例|经历", "story"),
        (r"(?i)opinion|观点|评论|看法|见解", "opinion"),
        (r"(?i)research|研究|论文|学术", "research"),
        (r"(?i)newsletter|通讯|周刊|月刊", "newsletter"),
    ]

    def generate_tags(
        self,
        text: str,
        title: str = "",
        max_tags: int = 10,
        use_ai: bool = False,
    ) -> list[Tag]:
        """生成标签

        Args:
            text: 文本内容
            title: 标题
            max_tags: 最大标签数
            use_ai: 是否使用AI生成（预留）

        Returns:
            标签列表
        """
        tags = []

        # 1. 基于关键词提取
        tags.extend(self._extract_keyword_tags(text))

        # 2. 基于话题模式
        tags.extend(self._extract_topic_tags(text))

        # 3. 从标题提取
        if title:
            tags.extend(self._extract_title_tags(title))

        # 4. 合并去重
        tags = self._merge_tags(tags)

        # 5. 按频率排序
        tags.sort(key=lambda x: x.count, reverse=True)

        return tags[:max_tags]

    def _extract_keyword_tags(self, text: str) -> list[Tag]:
        """从关键词提取标签"""
        tags = []

        for category, keywords in self.KEYWORD_TAGS.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    tags.append(Tag(name=category, count=1, source="keyword"))

        return tags

    def _extract_topic_tags(self, text: str) -> list[Tag]:
        """从话题模式提取标签"""
        tags = []

        for pattern, topic in self.TOPIC_PATTERNS:
            if re.search(pattern, text):
                tags.append(Tag(name=topic, count=1, source="topic"))

        return tags

    def _extract_title_tags(self, title: str) -> list[Tag]:
        """从标题提取标签"""
        tags = []

        # 提取#标签
        hash_tags = re.findall(r"#(\w+)", title)
        for tag in hash_tags:
            tags.append(Tag(name=tag.lower(), count=2, source="title"))

        # 提取「」或【】中的内容
        brackets = re.findall(r"[「【](.+?)[」】]", title)
        for bracket in brackets:
            if len(bracket) <= 10:
                tags.append(Tag(name=bracket.lower(), count=2, source="title"))

        return tags

    def _merge_tags(self, tags: list[Tag]) -> list[Tag]:
        """合并重复标签"""
        merged = {}

        for tag in tags:
            key = tag.name.lower()
            if key in merged:
                merged[key].count += tag.count
            else:
                merged[key] = Tag(
                    name=tag.name,
                    count=tag.count,
                    source=tag.source,
                )

        return list(merged.values())

    def extract_entities(self, text: str) -> dict:
        """提取实体

        Args:
            text: 文本内容

        Returns:
            实体字典
        """
        entities = {
            "persons": [],
            "organizations": [],
            "locations": [],
            "technologies": [],
        }

        # 简单模式匹配
        # 人名（两个字或四字名字）
        persons = re.findall(r"(?:^|[\u4e00-\u9fa5])([A-Z][a-z]+ [A-Z][a-z]+)", text)
        entities["persons"].extend(persons)

        # 技术名称
        tech_keywords = ["Python", "JavaScript", "React", "Vue", "Angular", "Node",
                        "Go", "Rust", "Java", "C++", "C#", "Swift", "Kotlin"]
        for tech in tech_keywords:
            if tech.lower() in text.lower():
                entities["technologies"].append(tech)

        # 组织（常见结尾）
        org_patterns = [r"(\w+公司)", r"(\w+大学)", r"(\w+医院)", r"(\w+研究院)"]
        for pattern in org_patterns:
            matches = re.findall(pattern, text)
            entities["organizations"].extend(matches)

        return entities


# 全局实例
_auto_tagger: Optional[AutoTagger] = None


def get_auto_tagger() -> AutoTagger:
    """获取全局自动标签生成器"""
    global _auto_tagger
    if _auto_tagger is None:
        _auto_tagger = AutoTagger()
    return _auto_tagger
