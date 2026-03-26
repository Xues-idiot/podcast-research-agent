"""Audio Overview模块 - 生成播客风格的AI讨论

基于研究结果生成类似Google NotebookLM Audio Overview的播客风格讨论。

功能:
- 根据播客内容生成双人对讨论脚本
- 支持多种讨论风格 (深入讨论、简短总结、评论、辩论)
- TTS语音合成生成音频（可选）

参考: notebooklm-py Audio Overview实现
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, AsyncIterator
import base64
import hashlib

import asyncio
from pathlib import Path


class AudioStyle(Enum):
    """讨论风格"""
    DEEP_DIVE = "deep_dive"  # 深入讨论
    BRIEF = "brief"  # 简短总结
    CRITIQUE = "critique"  # 评论分析
    DEBATE = "debate"  # 辩论讨论


class AudioLength(Enum):
    """音频长度"""
    SHORT = "short"  # 1-2分钟
    DEFAULT = "default"  # 3-5分钟
    LONG = "long"  # 6-10分钟


class AudioVoice(Enum):
    """语音选项"""
    MALE_HOST_A = "male-qnq"  # 男声-主机A
    FEMALE_HOST_A = "female-qnq"  # 女声-主机A
    MALE_HOST_B = "male-tian"  # 男声-主机B
    FEMALE_HOST_B = "female-tian"  # 女声-主机B


@dataclass
class AudioOverviewScript:
    """Audio Overview脚本"""
    title: str
    hosts: list[str]  # 主持人列表
    segments: list["ScriptSegment"]
    total_duration_seconds: int
    style: AudioStyle
    language: str = "zh-CN"


@dataclass
class ScriptSegment:
    """脚本片段"""
    speaker: str  # 发言人
    content: str  # 内容
    duration_seconds: int  # 预估时长


@dataclass
class AudioOverviewResult:
    """Audio Overview结果（包含脚本和音频）"""
    script: AudioOverviewScript
    audio_data: Optional[bytes] = None  # MP3音频数据
    audio_url: Optional[str] = None  # 音频URL（如果已保存）


class AudioOverviewGenerator:
    """Audio Overview生成器

    基于播客研究结果生成播客风格的AI讨论脚本。
    """

    def __init__(self, llm_config: dict):
        """初始化生成器

        Args:
            llm_config: LLM配置 (包含 api_key, base_url, model等)
        """
        self.llm_config = llm_config
        self._client = None

    async def _get_client(self):
        """获取LLM客户端"""
        if self._client is None:
            from openai import AsyncOpenAI
            self._client = AsyncOpenAI(
                api_key=self.llm_config.get("api_key"),
                base_url=self.llm_config.get("base_url", "https://api.minimaxi.com/anthropic"),
            )
        return self._client

    async def synthesize_speech(
        self,
        text: str,
        voice: str = "male-qnq",
        speed: float = 1.0,
        output_path: Optional[str] = None,
    ) -> bytes:
        """将文本转换为语音

        Args:
            text: 要转换的文本
            voice: 语音选项 (male-qnq, female-qnq, male-tian, female-tian)
            speed: 语速 (0.5-2.0)
            output_path: 可选的输出路径

        Returns:
            bytes: MP3音频数据
        """
        import requests

        url = f"{self.llm_config.get('base_url', 'https://api.minimaxi.com').replace('/anthropic', '')}/v1/t2a_speech"

        headers = {
            "Authorization": f"Bearer {self.llm_config.get('api_key')}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "speech-01",
            "text": text,
            "voice_setting": {
                "voice_id": voice,
                "speed": speed,
            },
            "output_format": {
                "format": "mp3",
            },
        }

        import httpx
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"TTS synthesis failed: {response.status_code} - {response.text}")

        if output_path:
            Path(output_path).write_bytes(response.content)

        return response.content

    async def synthesize_script(
        self,
        script: AudioOverviewScript,
        host_a_voice: str = "male-qnq",
        host_b_voice: str = "female-tian",
        output_dir: Optional[str] = None,
    ) -> AudioOverviewResult:
        """为脚本生成TTS语音

        Args:
            script: 音频脚本
            host_a_voice: 主机A的语音
            host_b_voice: 主机B的语音
            output_dir: 可选的输出目录

        Returns:
            AudioOverviewResult: 包含脚本和音频数据的结果
        """
        all_audio = []
        audio_segments = []

        for i, segment in enumerate(script.segments):
            voice = host_a_voice if segment.speaker == "Host A" else host_b_voice

            try:
                audio_data = await self.synthesize_speech(
                    text=segment.content,
                    voice=voice,
                    speed=1.0,
                )
                all_audio.append(audio_data)
                audio_segments.append({
                    "index": i,
                    "speaker": segment.speaker,
                    "audio_length": len(audio_data),
                    "duration_seconds": segment.duration_seconds,
                })
            except Exception as e:
                print(f"Warning: Failed to synthesize segment {i}: {e}")

        # 合并所有音频片段
        if all_audio:
            combined_audio = b"".join(all_audio)
        else:
            combined_audio = None

        # 如果有输出目录，保存文件
        audio_url = None
        if output_dir and combined_audio:
            output_path = Path(output_dir) / f"audio_overview_{script.title[:20]}.mp3"
            output_path.write_bytes(combined_audio)
            audio_url = str(output_path)

        return AudioOverviewResult(
            script=script,
            audio_data=combined_audio,
            audio_url=audio_url,
        )

    async def generate(
        self,
        transcript: dict,
        summary: dict,
        keypoints: list,
        style: AudioStyle = AudioStyle.DEEP_DIVE,
        length: AudioLength = AudioLength.DEFAULT,
        language: str = "zh-CN",
        instructions: Optional[str] = None,
    ) -> AudioOverviewScript:
        """生成Audio Overview脚本

        Args:
            transcript: 转录文本
            summary: 摘要结果
            keypoints: 要点列表
            style: 讨论风格
            length: 音频长度
            language: 语言
            instructions: 自定义指令

        Returns:
            AudioOverviewScript
        """
        # 构建提示词
        prompt = self._build_prompt(transcript, summary, keypoints, style, length, language, instructions)

        # 调用LLM生成脚本
        client = await self._get_client()
        response = await client.chat.completions.create(
            model=self.llm_config.get("model", "MiniMax-M2.7"),
            messages=[
                {"role": "system", "content": self._get_system_prompt(style, language)},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=4000,
        )

        script_text = response.choices[0].message.content or ""

        # 解析脚本
        script = self._parse_script(script_text, style, language)

        return script

    def _build_prompt(
        self,
        transcript: dict,
        summary: dict,
        keypoints: list,
        style: AudioStyle,
        length: AudioLength,
        language: str,
        instructions: Optional[str],
    ) -> str:
        """构建生成提示词"""
        # 提取文本内容
        transcript_text = transcript.get("text", "")
        if len(transcript_text) > 3000:
            transcript_text = transcript_text[:3000] + "..."

        summary_text = summary.get("summary", "")
        if isinstance(summary, dict):
            summary_text = summary.get("title", "") + "\n\n" + summary.get("content", "")

        keypoints_text = "\n".join([f"- {kp.get('content', kp) if isinstance(kp, dict) else kp}" for kp in keypoints[:5]])

        # 长度对应的token估算
        length_map = {
            AudioLength.SHORT: "1-2分钟 (约150-300字)",
            AudioLength.DEFAULT: "3-5分钟 (约450-750字)",
            AudioLength.LONG: "6-10分钟 (约900-1500字)",
        }

        style_map = {
            AudioStyle.DEEP_DIVE: "深入讨论",
            AudioStyle.BRIEF: "简短总结",
            AudioStyle.CRITIQUE: "评论分析",
            AudioStyle.DEBATE: "辩论讨论",
        }

        prompt = f"""请根据以下播客内容，生成一段{style_map[style]}风格的{length_map[length]}AI播客讨论脚本。

## 转录文本
{transcript_text}

## 摘要
{summary_text}

## 关键要点
{keypoints_text}

{f"## 自定义指令\n{instructions}" if instructions else ""}

## 要求
1. 脚本需要两位主持人 (Host A 和 Host B) 之间的对话形式
2. 使用自然的对话语言，避免过于书面化
3. 包含适当的过渡词和互动 (如"我觉得"、"你同意吗"、"等等"等)
4. 涵盖内容的主要亮点和重要细节
5. 结尾需要有自然的收尾

请按以下格式输出：
---
标题: [讨论标题]
时长: [预估时长]

[Host A]: [内容]
[Host B]: [内容]
[Host A]: [内容]
...
---"""
        return prompt

    def _get_system_prompt(self, style: AudioStyle, language: str) -> str:
        """获取系统提示词"""
        style_map = {
            AudioStyle.DEEP_DIVE: "你是一位专业的播客主持人擅长深入探讨话题。你会用有趣的方式解释复杂概念，并与另一位主持人进行深入讨论。",
            AudioStyle.BRIEF: "你是一位简洁干练的播客主持人。你擅长用简短精炼的方式总结核心内容，让听众快速了解要点。",
            AudioStyle.CRITIQUE: "你是一位敏锐的评论员，擅长分析评价内容。你会指出内容的亮点和不足，并提供深入见解。",
            AudioStyle.DEBATE: "你是一位辩论高手，擅长从不同角度分析问题。你会提出不同观点，与对方进行建设性辩论。",
        }

        return f"""你是一位专业的AI播客主持人，擅长生成播客风格的讨论脚本。

风格要求：
{style_map.get(style, style_map[AudioStyle.DEEP_DIVE])}

输出格式：
- 以"标题: [标题]"开头
- 然后是"时长: [时长]"
- 接下来是两位主持人(Host A和Host B)的对话
- 每行格式: [Host A]: [内容]
- 对话应该自然流畅，有互动感

语言：使用{language}进行对话。"""

    def _parse_script(
        self,
        script_text: str,
        style: AudioStyle,
        language: str,
    ) -> AudioOverviewScript:
        """解析生成的脚本文本"""
        lines = script_text.strip().split("\n")

        title = "AI播客讨论"
        segments = []
        current_speaker = None
        current_content = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # 解析标题
            if line.startswith("标题:"):
                title = line[3:].strip()
                continue

            # 解析时长
            if line.startswith("时长:"):
                continue

            # 解析发言人
            if line.startswith("[Host A]:") or line.startswith("[Host B]:"):
                # 保存前一个片段
                if current_speaker and current_content:
                    content = " ".join(current_content)
                    # 估算时长 (约150字/分钟)
                    duration = max(5, len(content) // 3)
                    segments.append(ScriptSegment(
                        speaker=current_speaker,
                        content=content,
                        duration_seconds=duration,
                    ))

                current_speaker = "Host A" if "Host A" in line else "Host B"
                current_content = [line.split("]:", 1)[1].strip() if "]:" in line else line]
            elif current_speaker and line:
                current_content.append(line)

        # 保存最后一个片段
        if current_speaker and current_content:
            content = " ".join(current_content)
            duration = max(5, len(content) // 3)
            segments.append(ScriptSegment(
                speaker=current_speaker,
                content=content,
                duration_seconds=duration,
            ))

        # 计算总时长
        total_duration = sum(s.duration_seconds for s in segments)

        return AudioOverviewScript(
            title=title,
            hosts=["Host A", "Host B"],
            segments=segments,
            total_duration_seconds=total_duration,
            style=style,
            language=language,
        )

    def script_to_text(self, script: AudioOverviewScript) -> str:
        """将脚本转换为纯文本

        Args:
            script: 音频脚本

        Returns:
            格式化文本
        """
        lines = [f"# {script.title}", ""]
        lines.append(f"时长: 约{script.total_duration_seconds // 60}分钟")
        lines.append(f"风格: {script.style.value}")
        lines.append("")

        for segment in script.segments:
            lines.append(f"[{segment.speaker}]: {segment.content}")

        return "\n".join(lines)


async def generate_audio_overview(
    research_result: dict,
    style: AudioStyle = AudioStyle.DEEP_DIVE,
    length: AudioLength = AudioLength.DEFAULT,
    output_path: Optional[str] = None,
    synthesize: bool = False,
) -> AudioOverviewScript:
    """便捷函数：生成Audio Overview

    Args:
        research_result: 研究结果 (包含transcript, summary, keypoints等)
        style: 讨论风格
        length: 音频长度
        output_path: 可选的输出路径
        synthesize: 是否同时合成TTS语音

    Returns:
        AudioOverviewScript (如果synthesize=True，返回AudioOverviewResult)
    """
    from echo.config import config

    generator = AudioOverviewGenerator({
        "api_key": config.minimax.api_key,
        "base_url": config.minimax.base_url,
        "model": config.minimax.model,
    })

    transcript = research_result.get("transcript", {})
    summary = research_result.get("summary", {})
    keypoints = research_result.get("keypoints", [])

    script = await generator.generate(
        transcript=transcript,
        summary=summary,
        keypoints=keypoints,
        style=style,
        length=length,
    )

    # 如果指定了输出路径，保存脚本
    if output_path:
        text = generator.script_to_text(script)
        Path(output_path).write_text(text, encoding="utf-8")

    # 如果需要TTS合成
    if synthesize:
        output_dir = str(Path(output_path).parent) if output_path else None
        result = await generator.synthesize_script(script, output_dir=output_dir)
        return result

    return script
