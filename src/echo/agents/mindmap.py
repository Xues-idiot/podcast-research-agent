"""思维导图生成Agent"""

from typing import List

from openai import AsyncOpenAI

from echo.config import MiniMaxConfig


class MindMapGenerator:
    """
    思维导图生成Agent - 从要点生成思维导图结构
    """

    SYSTEM_PROMPT = """你是一个专业的知识结构化专家。
你的任务是将要点组织成层级结构的思维导图。

思维导图格式要求：
1. 根节点是主题
2. 每个分支代表一个主要类别或主题
3. 子节点是具体要点
4. 保持简洁，每个节点一句话

输出JSON格式：
{
    "root": "主题名称",
    "branches": [
        {
            "title": "分支1标题",
            "children": ["子节点1", "子节点2"]
        }
    ]
}
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def generate(self, keypoints: List[dict]) -> dict:
        """
        生成思维导图

        Args:
            keypoints: 要点列表

        Returns:
            思维导图结构
        """
        # 提取要点内容
        kp_text = "\n".join([
            f"{i+1}. {kp.get('content', '')}"
            for i, kp in enumerate(keypoints)
        ])

        user_prompt = f"""请将以下要点组织成思维导图：

{kp_text}
"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.5,
        )

        content = response.choices[0].message.content or ""

        return self._parse_mindmap(content)

    def _parse_mindmap(self, content: str, keypoints: list = None) -> dict:
        """解析思维导图JSON"""
        import json
        import re

        # 尝试提取JSON
        json_match = re.search(r'\{[\s\S]*\}', content)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        # 降级：简单解析
        return {
            "root": "播客要点",
            "branches": [],
            "raw": content,
        }

    def export_json(self, mindmap: dict) -> str:
        """导出为JSON字符串"""
        import json
        return json.dumps(mindmap, ensure_ascii=False, indent=2)
