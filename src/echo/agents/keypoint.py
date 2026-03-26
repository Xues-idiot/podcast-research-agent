"""要点生成Agent - 提取关键要点"""

from typing import List, Optional
import re

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
5. 标注每个要点在原文中的位置（用于跳转时间戳）

输出格式：
每个要点格式：###KEYPOINT###|序号|内容|重要性|应用场景|原文位置描述
例如：###KEYPOINT###|1|AI将改变教育方式|高|在线教育产品设计|第三章讨论教育创新的部分

位置描述用于帮助定位时间戳，描述要简洁（如：开头介绍、第三章教育讨论、结尾总结等）
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def generate(
        self,
        transcript: dict,
        num: int = 5,
        segments: Optional[List[dict]] = None,
    ) -> List[dict]:
        """
        生成要点列表

        Args:
            transcript: 转录结果
            num: 要点数量
            segments: 可选的转录片段列表，用于时间戳匹配

        Returns:
            要点列表，每项包含 content, importance, applications, timestamp
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

        content = response.choices[0].message.content or ""

        keypoints = self._parse_keypoints(content, num)

        # 如果有segments，尝试匹配时间戳
        if segments and keypoints:
            keypoints = self._match_timestamps(keypoints, segments)

        return keypoints

    def _parse_keypoints(self, content: str, num: int) -> List[dict]:
        """解析LLM输出为要点列表"""
        keypoints = []

        # 优先尝试 JSON 解析
        try:
            import json, re
            # 尝试提取 JSON
            json_match = re.search(r'\{[\s\S]*\}', content)
            if json_match:
                data = json.loads(json_match.group())
                kp_list = data.get("keypoints", data.get("要点", []))
                if isinstance(kp_list, list):
                    for kp in kp_list:
                        keypoints.append({
                            "id": len(keypoints) + 1,
                            "content": kp.get("content", kp.get("内容", "")),
                            "importance": kp.get("importance", kp.get("重要性", "medium")),
                            "applications": kp.get("applications", kp.get("应用场景", [])),
                            "location": kp.get("location", kp.get("位置描述", "")),
                            "timestamp": None,
                        })
                    if keypoints:
                        return keypoints[:num]
        except (json.JSONDecodeError, re.error):
            pass

        # 按 ###KEYPOINT### 分隔
        parts = content.split("###KEYPOINT###")

        for part in parts[1:]:  # 跳过第一个空部分
            part = part.strip()
            if not part:
                continue

            # 解析格式：|序号|内容|重要性|应用场景|位置描述
            match = re.match(r'\|(\d+)\|(.+?)\|(\w+)\|(.+?)\|(.*)', part, re.DOTALL)
            if match:
                id_, content_text, importance, apps, location = match.groups()
                keypoints.append({
                    "id": int(id_),
                    "content": content_text.strip(),
                    "importance": importance.lower() if importance.lower() in ["高", "中", "低"] else "medium",
                    "applications": apps.strip(),
                    "location": location.strip(),
                    "timestamp": None,  # 稍后填充
                })

        # 如果解析失败，尝试简单解析
        if not keypoints:
            lines = content.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line and line[0].isdigit() and ". " in line:
                    parts = line.split(". ", 1)
                    if len(parts) == 2:
                        keypoints.append({
                            "id": len(keypoints) + 1,
                            "content": parts[1],
                            "importance": "medium",
                            "applications": [],
                            "location": "",
                            "timestamp": None,
                        })

        return keypoints[:num]

    def _match_timestamps(
        self,
        keypoints: List[dict],
        segments: List[dict],
    ) -> List[dict]:
        """根据位置描述匹配时间戳"""
        if not segments:
            return keypoints

        for kp in keypoints:
            location = kp.get("location", "").lower()
            timestamp = self._find_best_timestamp(location, segments)
            kp["timestamp"] = timestamp

        return keypoints

    def _find_best_timestamp(
        self,
        location: str,
        segments: List[dict],
    ) -> Optional[float]:
        """根据位置描述找到最匹配的时间戳"""
        if not location or not segments:
            return None

        location_keywords = {
            "开头": 0,
            "开始": 0,
            "介绍": 0,
            "intro": 0,
            "结尾": -1,
            "总结": -1,
            "结语": -1,
            "outro": -1,
            "中间": len(segments) // 2,
            "中段": len(segments) // 2,
        }

        # 检查关键词
        for keyword, preferred_idx in location_keywords.items():
            if keyword in location:
                if preferred_idx < 0:
                    preferred_idx = len(segments) + preferred_idx
                if 0 <= preferred_idx < len(segments):
                    return segments[preferred_idx].get("start")

        # 计算文字相似度
        location_words = set(location.split())
        best_idx = 0
        best_score = 0

        for i, seg in enumerate(segments):
            seg_text = seg.get("text", "").lower()
            seg_words = set(seg_text.split())
            overlap = len(location_words & seg_words)
            if overlap > best_score:
                best_score = overlap
                best_idx = i

        if best_score > 0 and best_idx < len(segments):
            return segments[best_idx].get("start")

        return None

    def score(self, keypoints: List[dict]) -> List[dict]:
        """
        按重要性排序要点

        Args:
            keypoints: 要点列表

        Returns:
            排序后的要点列表
        """
        # 可以调用LLM重新评估重要性
        return sorted(keypoints, key=lambda x: x.get("importance", "medium"), reverse=True)
