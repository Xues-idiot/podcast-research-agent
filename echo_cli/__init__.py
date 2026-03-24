"""Echo CLI - 命令行入口"""

import asyncio
import json
import sys
from pathlib import Path

import click

from echo import __version__
from echo.client import EchoClient
from echo.config import config
from echo.exceptions import EchoError


@click.group()
@click.version_option(version=__version__)
def cli():
    """Echo - 播客研究Agent

    让知识回响，从播客/视频中提取有价值的信息。
    """
    pass


@cli.command()
@click.argument("url")
@click.option(
    "--keypoints", "-k",
    default=5,
    type=int,
    help="要点数量 (默认: 5)"
)
@click.option(
    "--output", "-o",
    default="./output",
    help="输出目录 (默认: ./output)"
)
@click.option(
    "--format", "-f",
    type=click.Choice(["json", "markdown", "both"]),
    default="both",
    help="输出格式 (默认: both)"
)
def research(url: str, keypoints: int, output: str, format: str):
    """研究播客/视频内容

    URL: 视频/播客链接，支持B站、YouTube、播客RSS
    """
    asyncio.run(_research(url, keypoints, output, format))


async def _research(url: str, keypoints: int, output: str, format: str):
    """异步研究入口"""
    click.echo(f"🎙️  Echo 开始研究...")
    click.echo(f"    URL: {url}")
    click.echo(f"    要点: {keypoints}")
    click.echo(f"    输出: {output}")
    click.echo()

    try:
        async with EchoClient() as client:
            result = await client.research(url, keypoints)

            # 创建输出目录
            output_dir = Path(output)
            output_dir.mkdir(parents=True, exist_ok=True)

            # 保存结果
            if format in ("json", "both"):
                _save_json(result, output_dir)

            if format in ("markdown", "both"):
                _save_markdown(result, output_dir)

            click.echo()
            click.echo(f"✅ 研究完成！")
            click.echo(f"    输出目录: {output_dir}")

            # 显示摘要
            summary = result.get("summary", {})
            if summary.get("title"):
                click.echo(f"    标题: {summary['title']}")
            if summary.get("highlights"):
                click.echo(f"    亮点: {len(summary['highlights'])} 个")

    except EchoError as e:
        click.echo(f"❌ 错误: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ 未知错误: {e}", err=True)
        sys.exit(1)


def _save_json(result: dict, output_dir: Path):
    """保存JSON格式"""
    # 简化结果
    simple = {
        "title": result.get("summary", {}).get("title", ""),
        "summary": result.get("summary", {}).get("summary", ""),
        "highlights": result.get("summary", {}).get("highlights", []),
        "keypoints": [
            {"id": kp.get("id"), "content": kp.get("content")}
            for kp in result.get("keypoints", [])
        ],
        "mindmap": result.get("mindmap", {}),
    }

    (output_dir / "result.json").write_text(
        json.dumps(simple, ensure_ascii=False, indent=2)
    )


def _save_markdown(result: dict, output_dir: Path):
    """保存Markdown格式"""
    lines = []

    # 标题
    title = result.get("summary", {}).get("title", "无标题")
    lines.append(f"# {title}")
    lines.append("")

    # 摘要
    summary_text = result.get("summary", {}).get("summary", "")
    if summary_text:
        lines.append("## 摘要")
        lines.append(summary_text)
        lines.append("")

    # 亮点
    highlights = result.get("summary", {}).get("highlights", [])
    if highlights:
        lines.append("## 亮点")
        for h in highlights:
            lines.append(f"- {h}")
        lines.append("")

    # 要点
    keypoints = result.get("keypoints", [])
    if keypoints:
        lines.append("## 关键要点")
        for kp in keypoints:
            lines.append(f"### {kp.get('id', 0)}. {kp.get('content', '')}")
            lines.append("")
        lines.append("")

    # 思维导图
    mindmap = result.get("mindmap", {})
    if mindmap.get("root"):
        lines.append("## 思维导图")
        lines.append(f"**主题**: {mindmap['root']}")
        lines.append("")
        for branch in mindmap.get("branches", []):
            lines.append(f"### {branch.get('title', '')}")
            for child in branch.get("children", []):
                lines.append(f"- {child}")
            lines.append("")

    (output_dir / "result.md").write_text("\n".join(lines))


@cli.command()
def status():
    """检查配置状态"""
    click.echo("📋 Echo 配置状态")
    click.echo()

    # MiniMax
    if config.minimax.api_key:
        click.echo("  ✅ MiniMax API")
        click.echo(f"     地址: {config.minimax.base_url}")
        click.echo(f"     模型: {config.minimax.model}")
    else:
        click.echo("  ❌ MiniMax API - 未配置 (设置 MINIMAX_API_KEY)")

    click.echo()

    # Tavily
    if config.tavily.api_key:
        click.echo("  ✅ Tavily API")
    else:
        click.echo("  ⚠️  Tavily API - 未配置 (设置 TAVILY_API_KEY)")
        click.echo("     知识关联功能将不可用")


@cli.command()
@click.argument("url")
async def info(url: str):
    """获取视频信息（不下载）"""
    from echo.tools.bilibili import BilibiliDownloader
    from echo.tools.youtube import YouTubeDownloader

    click.echo(f"🔍 获取信息: {url}")

    try:
        if "bilibili" in url:
            dl = BilibiliDownloader()
            info = await dl.get_video_info(url)
        elif "youtube" in url or "youtu.be" in url:
            dl = YouTubeDownloader()
            info = await dl.get_video_info(url)
        else:
            click.echo("❌ 不支持的URL类型")
            return

        click.echo(f"    标题: {info.get('title', '未知')}")
        click.echo(f"    时长: {info.get('duration', '未知')}")
        click.echo(f"    描述: {info.get('description', '')[:100]}...")

    except Exception as e:
        click.echo(f"❌ 获取失败: {e}", err=True)


def main():
    cli()


if __name__ == "__main__":
    main()
