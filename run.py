#!/usr/bin/env python3
"""Echo CLI 入口脚本"""

import sys
from pathlib import Path

# 确保项目根目录在Python路径中
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from echo_cli import main

if __name__ == "__main__":
    main()
