---
name: podcast-generation
description: 当用户请求从研究结果生成播客音频时使用此技能。将研究结果转换为双人对话式播客音频格式。
---

# Podcast Generation Skill

## Overview

此技能将 Echo 的研究结果转换为播客风格的音频内容。生成双人对话脚本（男/女主持），通过 TTS 合成语音。

## When to Use

**使用此技能当：**
- 用户请求"生成播客"
- 用户想要收听研究结果的音频版本
- 用户需要将文本内容转换为语音

## Workflow

### Step 1: 理解需求

确定：
- 研究结果内容：要转换的播客研究数据
- 音频风格：Deep Dive（深入探讨）、Brief（简短总结）、Critique（评论）、Debate（辩论）
- 目标时长：短版(3-5分钟)、标准(10-15分钟)、长版(20-30分钟)

### Step 2: 生成对话脚本

使用 AudioOverviewGenerator 生成双人对话脚本：

```python
from echo.audio_overview import AudioOverviewGenerator, AudioStyle, AudioLength

generator = AudioOverviewGenerator()
script = await generator.generate_script(
    research_result=result,
    style=AudioStyle.DEEP_DIVE,
    length=AudioLength.DEFAULT
)
```

### Step 3: 生成音频

调用 TTS API 生成语音并混合为最终音频文件。

## Output Format

生成的脚本格式：

```json
{
  "title": "研究播客标题",
  "locale": "zh",
  "lines": [
    {"speaker": "male", "paragraph": "对话内容"},
    {"speaker": "female", "paragraph": "对话内容"}
  ]
}
```

## Script Guidelines

- 两个主持：male 和 female，自然交替
- 目标时长：约 10-15 分钟（约 40-60 行对话）
- 以 greeting 开始，包含 "大家好" 或类似问候语
- 讨论核心要点，避免偏离主题
- 保持对话自然流畅，避免太书面化
