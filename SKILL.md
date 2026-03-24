---
name: echo-podcast-research
description: Use when researching podcasts or videos to extract key points, summaries, and knowledge. Activates on requests like "research this podcast", "summarize this video", "extract key points from audio", or "analyze this episode"
---

# Echo Podcast Research Agent

Echo helps you extract valuable knowledge from podcasts and videos by automatically transcribing, summarizing, and identifying key points.

## When This Skill Activates

**Explicit:** User says "use echo", "research with echo", or mentions "podcast research"

**Intent detection:** Recognize requests like:
- "Research this podcast/video"
- "Summarize this episode"
- "Extract key points from this audio"
- "Analyze this video content"
- "What is this podcast about?"
- "Create a mind map of this episode"

## Installation

**From PyPI:**
```bash
pip install echo-podcast-research
```

**From source:**
```bash
pip install -e .
```

## Prerequisites

Before using, configure API keys in `.env`:

```bash
MINIMAX_API_KEY=your_minimax_api_key
TAVILY_API_KEY=your_tavily_api_key  # Optional, for knowledge linking
```

## Quick Start

### Python API

```python
import asyncio
from echo import EchoClient

async def main():
    async with EchoClient() as client:
        result = await client.research(
            url="https://b23.tv/xxx",
            num_keypoints=5
        )
        print(result["summary"])
        print(result["keypoints"])

asyncio.run(main())
```

### CLI

```bash
# Check configuration
echo status

# Research a video/podcast
echo research "https://b23.tv/xxx" --keypoints 5 --output ./output

# Get video info (without downloading)
echo info "https://youtube.com/watch?v=xxx"
```

## Command Reference

| Task | Command |
|------|---------|
| Research | `echo research <URL> [--keypoints N] [--output DIR]` |
| Status | `echo status` |
| Info | `echo info <URL>` |

### Supported URLs

- **Bilibili**: `bilibili.com/video/BVxxx`, `b23.tv/xxx`
- **YouTube**: `youtube.com/watch?v=xxx`, `youtu.be/xxx`
- **Podcast RSS**: Any standard RSS 2.0 feed

## Output Structure

```python
{
    "transcript": {
        "text": "...",           # Full transcript
        "segments": [...],        # Timestamped segments
        "language": "zh"          # Detected language
    },
    "summary": {
        "title": "...",          # Content title
        "summary": "...",        # 2-3 paragraph summary
        "highlights": [...]      # Key highlights
    },
    "keypoints": [
        {"id": 1, "content": "...", "importance": "high"},
        ...
    ],
    "mindmap": {
        "root": "主题",
        "branches": [
            {"title": "分支1", "children": ["子节点1", "子节点2"]}
        ]
    },
    "knowledge_cards": [
        {
            "keypoint": "...",
            "related": [{"title": "...", "url": "..."}],
            "confidence": 0.8
        }
    ],
    "report": {
        "content": "...",
        "title": "..."
    }
}
```

## Output Formats

### JSON Output

```bash
echo research <URL> --format json
```

### Markdown Output

```bash
echo research <URL> --format markdown
```

### Both

```bash
echo research <URL> --format both
```

## Autonomy Rules

**Run automatically (no confirmation):**
- `echo status` - check configuration
- `echo research <URL>` - research tasks
- `echo info <URL>` - get video info

**Ask before running:**
- Research on multiple URLs in sequence
- Any operation that writes to filesystem (uses `--output` flag)

## Processing Times

| Step | Typical Time |
|------|--------------|
| Download | 30s - 5 min |
| Transcription | 1-10 min |
| Summary | 10-30s |
| Keypoints | 10-30s |
| Mindmap | 10-30s |
| Knowledge Link | 30-60s |

**Total: ~5-20 minutes depending on video length**

## Error Handling

| Error | Cause | Action |
|-------|-------|--------|
| Download failed | Network or unsupported URL | Check URL format |
| Transcription failed | Audio quality issues | Try with different source |
| API error | Rate limit or invalid key | Check API keys |

## Known Limitations

- Requires FFmpeg for audio extraction
- Whisper transcription quality depends on audio clarity
- Tavily API optional (for knowledge linking feature)
