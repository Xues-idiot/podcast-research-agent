"""要点生成Agent - 提取关键要点"""

from typing import List

from openai import AsyncOpenAI

from echo.config import MiniMaxConfig


class KeyPointGenerator:
    """
    要点生成Agent - 从转录中提取关键要点
    """

    SYSTEM_PROMPT = """你是一个专业的播客内容分析专家。
你的任务是从转录文本中提取最有价值的要点。

要点提取要求：
1. 选择真正有价值的洞察，而非显而易见的事实
2. 每个要点用简洁的语言描述核心观点
3. 标注每个要点的重要性（高/中/低）
4. 说明每个要点可以应用在什么场景

输出格式：
- 要点编号和内容
- 重要性等级
- 应用场景
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def generate(self, transcript: dict, num: int = 5) -> List[dict]:
        """
        生成要点列表

        Args:
            transcript: 转录结果
            num: 要点数量

        Returns:
            要点列表，每项包含 content, importance, applications
        """
        text = transcript.get("text", "")

        user_prompt = f"""请从以下转录文本中提取{num}个最重要的要点：

{text[:8000]}
"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content

        return self._parse_keypoints(content, num)

    def _parse_keypoints(self, content: str, num: int) -> List[dict]:
        """解析LLM输出为要点列表"""
        lines = content.strip().split("\n")
        keypoints = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # 匹配 "1. ..." 格式
            if line and line[0].isdigit() and ". " in line:
                parts = line.split(". ", 1)
                if len(parts) == 2:
                    keypoints.append({
                        "id": int(parts[0]),
                        "content": parts[1],
                        "importance": "medium",  # 默认值
                        "applications": [],
                    })

        return keypoints[:num]

    async def score(self, keypoints: List[dict]) -> List[dict]:
        """
        按重要性排序要点

        Args:
            keypoints: 要点列表

        Returns:
            排序后的要点列表
        """
        # 可以调用LLM重新评估重要性
        return sorted(keypoints, key=lambda x: x.get("importance", "medium"), reverse=True)
