"""记忆更新器 - LLM驱动的记忆提取和更新

参考 deer-flow 的 memory updater 实现，
从对话中提取和更新用户记忆。
"""

from typing import Optional
from dataclasses import dataclass

from echo.memory import MemoryStore, Fact


# 记忆更新提示词
MEMORY_UPDATE_PROMPT = """你是一个用户记忆管理助手。从以下对话中提取用户的相关信息，更新记忆。

## 当前记忆
{current_memory}

## 对话历史
{conversation}

## 任务
1. 提取对话中用户的：
   - 工作相关：研究领域、职业、常用术语
   - 偏好相关：喜欢的播客类型、导出格式、交互方式
   - 上下文：当前在做什么、关心什么话题
   - 行为模式：使用习惯、时间偏好

2. 更新记忆字段：
   - work_context: 工作上下文
   - personal_context: 个人上下文
   - top_of_mind: 当前最关注的

3. 提取具体事实（如有）：
   - preference: 偏好
   - knowledge: 知识
   - context: 上下文
   - behavior: 行为
   - goal: 目标

请用JSON格式回复：
{{
    "work_context": "更新的工作上下文或空字符串",
    "personal_context": "更新的个人上下文或空字符串",
    "top_of_mind": "更新的当前关注或空字符串",
    "new_facts": [
        {{"content": "事实内容", "category": "preference/knowledge/context/behavior/goal", "confidence": 0.7}}
    ]
}}
"""

# 事实提取提示词
FACT_EXTRACTION_PROMPT = """从以下文本中提取用户相关的事实。

文本：
{text}

提取与用户相关的具体事实，如偏好、知识、上下文、行为或目标。
每个事实应该是简洁的陈述句。

用JSON数组格式回复：
{{"facts": [{{"content": "事实内容", "category": "类型", "confidence": 0.7}}]}}
"""


@dataclass
class MemoryUpdate:
    """记忆更新结果"""
    work_context: str = ""
    personal_context: str = ""
    top_of_mind: str = ""
    new_facts: list[dict] = None

    def __post_init__(self):
        if self.new_facts is None:
            self.new_facts = []


class MemoryUpdater:
    """记忆更新器

    从对话中提取和更新用户记忆。
    """

    def __init__(self, memory_store: Optional[MemoryStore] = None):
        """初始化更新器

        Args:
            memory_store: 记忆存储实例
        """
        self.memory_store = memory_store or MemoryStore()

    async def update_from_conversation(
        self,
        user_id: str,
        conversation: str,
        current_memory: Optional[str] = None
    ) -> MemoryUpdate:
        """从对话更新记忆

        Args:
            user_id: 用户ID
            conversation: 对话文本
            current_memory: 当前记忆文本（可选）

        Returns:
            MemoryUpdate 更新结果
        """
        if current_memory is None:
            memory = self.memory_store.get_memory(user_id)
            current_memory = self.memory_store.inject_into_context(user_id)

        # TODO: 调用 LLM 进行记忆更新
        # 目前先返回空更新，实际使用时需要接入 MiniMax API
        return MemoryUpdate()

    def extract_facts_from_text(self, text: str) -> list[Fact]:
        """从文本中提取事实

        Args:
            text: 文本内容

        Returns:
            提取的事实列表
        """
        # TODO: 调用 LLM 进行事实提取
        # 目前先返回空列表
        return []

    def learn_podcast_preference(
        self,
        user_id: str,
        podcast_info: dict
    ):
        """学习播客偏好

        从播客信息中学习用户偏好。

        Args:
            user_id: 用户ID
            podcast_info: 播客信息，包含 title, platform, duration 等
        """
        title = podcast_info.get("title", "")
        platform = podcast_info.get("platform", "")
        duration = podcast_info.get("duration", 0)

        facts = []

        # 平台偏好
        if platform:
            facts.append(Fact(
                content=f"常使用{platform}平台",
                category="preference",
                confidence=0.6,
                source="podcast_usage"
            ))

        # 时长偏好
        if duration > 0:
            if duration < 1800:  # < 30分钟
                facts.append(Fact(
                    content="偏好短时长播客",
                    category="preference",
                    confidence=0.5,
                    source="podcast_usage"
                ))
            elif duration > 3600:  # > 60分钟
                facts.append(Fact(
                    content="偏好长时长播客",
                    category="preference",
                    confidence=0.5,
                    source="podcast_usage"
                ))

        # 标题关键词（简化处理）
        if title:
            keywords = []
            tech_keywords = ["AI", "LLM", "机器学习", "深度学习"]
            business_keywords = ["商业", "创业", "投资", "产品"]

            for kw in tech_keywords:
                if kw in title:
                    keywords.append(f"关注{kw}领域")
            for kw in business_keywords:
                if kw in title:
                    keywords.append(f"关注{kw}领域")

            for kw_content in keywords:
                facts.append(Fact(
                    content=kw_content,
                    category="knowledge",
                    confidence=0.4,
                    source="podcast_title"
                ))

        # 添加事实
        for fact in facts:
            self.memory_store.add_fact(
                user_id=user_id,
                content=fact.content,
                category=fact.category,
                confidence=fact.confidence,
                source=fact.source
            )

    def learn_export_preference(
        self,
        user_id: str,
        export_format: str
    ):
        """学习导出偏好

        Args:
            user_id: 用户ID
            export_format: 导出格式 (json, markdown, html, pdf)
        """
        self.memory_store.add_fact(
            user_id=user_id,
            content=f"偏好{export_format.upper()}格式导出",
            category="preference",
            confidence=0.7,
            source="export_usage"
        )

    def learn_research_topic(
        self,
        user_id: str,
        topic: str
    ):
        """学习研究主题

        Args:
            user_id: 用户ID
            topic: 研究主题
        """
        self.memory_store.update_memory(
            user_id=user_id,
            top_of_mind=f"正在研究{topic}"
        )

        self.memory_store.add_fact(
            user_id=user_id,
            content=f"研究{topic}相关内容",
            category="context",
            confidence=0.6,
            source="research_topic"
        )

    def get_personalized_context(self, user_id: str = "default") -> str:
        """获取个性化上下文

        用于注入到研究流程中。

        Args:
            user_id: 用户ID

        Returns:
            个性化上下文文本
        """
        return self.memory_store.inject_into_context(user_id)
