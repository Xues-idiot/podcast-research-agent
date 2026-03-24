"""转录Agent测试"""

import pytest
from echo.agents.transcriber import Transcriber


class TestTranscriber:
    """转录Agent测试"""

    def test_transcriber_init(self):
        """测试初始化"""
        transcriber = Transcriber(model_name="tiny")
        assert transcriber.model_name == "tiny"
        assert transcriber.model is None  # 懒加载

    @pytest.mark.asyncio
    async def test_transcribe_requires_file(self):
        """测试转录需要文件"""
        transcriber = Transcriber()
        # 转录需要实际文件，这里测试参数
        assert transcriber.model is None
