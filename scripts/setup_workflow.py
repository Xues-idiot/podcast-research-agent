#!/usr/bin/env python3
"""
Echo 播客研究Agent - 定时工作流设置

这个脚本帮助设置定时任务，自动执行持续改进循环。

用法:
    python scripts/setup_workflow.py --install    # 安装定时任务
    python scripts/setup_workflow.py --uninstall  # 卸载定时任务
    python scripts/setup_workflow.py --run        # 立即运行
"""

import argparse
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def install_cron_task():
    """安装定时任务"""
    import platform

    system = platform.system()

    if system == "Windows":
        # Windows: 使用任务计划程序
        print("Windows 系统，请手动创建定时任务：")
        print("  1. 打开任务计划程序")
        print("  2. 创建基本任务")
        print(f"  3. 程序: python")
        print(f"  4. 参数: {PROJECT_ROOT / 'scripts' / 'auto_improve.py'} --rounds 5")
        print("  5. 频率: 每天或每周")
        return True

    elif system == "Linux" or system == "Darwin":
        # Unix: 使用 cron
        script_path = PROJECT_ROOT / "scripts" / "auto_improve.py"
        cron_entry = f"0 2 * * * cd {PROJECT_ROOT} && python {script_path} --rounds 5 --review-every 10 >> ~/.echo_cron.log 2>&1\n"

        crontab_file = Path.home() / ".crontab"
        existing = ""
        if crontab_file.exists():
            existing = crontab_file.read_text()

        if "auto_improve.py" in existing:
            print("定时任务已存在")
            return True

        crontab_file.write_text(existing + cron_entry)
        print(f"已安装定时任务: 每天凌晨2点运行")
        return True

    else:
        print(f"不支持的系统: {system}")
        return False


def uninstall_cron_task():
    """卸载定时任务"""
    import platform

    system = platform.system()

    if system == "Windows":
        print("Windows 系统，请手动删除定时任务")
        return True

    elif system == "Linux" or system == "Darwin":
        crontab_file = Path.home() / ".crontab"
        if crontab_file.exists():
            content = crontab_file.read_text()
            lines = [l for l in content.split("\n") if "auto_improve.py" not in l]
            crontab_file.write_text("\n".join(lines))
        print("已卸载定时任务")
        return True

    return False


def run_now():
    """立即运行"""
    import subprocess

    script_path = PROJECT_ROOT / "scripts" / "auto_improve.py"
    print("立即运行自动化改进...")
    result = subprocess.run(
        [sys.executable, str(script_path), "--rounds", "5", "--review-every", "5"],
        cwd=str(PROJECT_ROOT)
    )
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Echo 工作流设置")
    parser.add_argument("--install", action="store_true", help="安装定时任务")
    parser.add_argument("--uninstall", action="store_true", help="卸载定时任务")
    parser.add_argument("--run", action="store_true", help="立即运行")

    args = parser.parse_args()

    if args.install:
        return 0 if install_cron_task() else 1
    elif args.uninstall:
        return 0 if uninstall_cron_task() else 1
    elif args.run:
        return 0 if run_now() else 1
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
