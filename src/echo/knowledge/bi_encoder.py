"""Bi-encoder 检索模块

基于向量的语义检索，支持：
- 文本嵌入生成
- 余弦相似度计算
- Top-K 相似度检索
"""

import numpy as np
from typing import Optional

from echo.knowledge.entry import Entry


class BiEncoder:
    """Bi-encoder 检索器

    使用双编码器架构：
    - Query encoder: 将用户查询编码为向量
    - Doc encoder: 将文档/Entry编码为向量

    支持：
    - 本地 SentenceTransformer 模型
    - API 远程编码（待集成 MiniMax）
    """

    def __init__(
        self,
        model_name: str = "thenlper/gte-small",
        use_local: bool = True,
        device: str = "cpu",
    ):
        """初始化 Bi-encoder

        Args:
            model_name: 模型名称
            use_local: 是否使用本地模型
            device: 设备 ("cpu" 或 "cuda")
        """
        self.model_name = model_name
        self.use_local = use_local
        self.device = device
        self._model = None

    def _load_model(self):
        """延迟加载模型"""
        if self._model is not None:
            return

        if self.use_local:
            try:
                from sentence_transformers import SentenceTransformer
                self._model = SentenceTransformer(self.model_name, device=self.device)
            except ImportError:
                raise ImportError(
                    "sentence-transformers not installed. "
                    "Install with: pip install sentence-transformers"
                )
        else:
            # TODO: 集成 MiniMax API
            raise NotImplementedError("API remote encoding not yet implemented")

    def encode_query(self, query: str) -> np.ndarray:
        """编码用户查询

        Args:
            query: 查询文本

        Returns:
            查询向量 (1D numpy array)
        """
        self._load_model()

        if self.use_local:
            embedding = self._model.encode(query, normalize_embeddings=True)
            return embedding
        else:
            raise NotImplementedError

    def encode_documents(self, texts: list[str]) -> np.ndarray:
        """批量编码文档

        Args:
            texts: 文档文本列表

        Returns:
            文档向量矩阵 (2D numpy array, shape: [n_docs, embedding_dim])
        """
        self._load_model()

        if self.use_local:
            embeddings = self._model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
            return embeddings
        else:
            raise NotImplementedError

    def compute_similarity(self, query_vec: np.ndarray, doc_vecs: np.ndarray) -> np.ndarray:
        """计算查询与文档的余弦相似度

        Args:
            query_vec: 查询向量 (1D)
            doc_vecs: 文档向量矩阵 (2D)

        Returns:
            相似度分数 (1D)
        """
        # 归一化后直接点积即余弦相似度
        return np.dot(doc_vecs, query_vec)

    def search(
        self,
        query: str,
        entries: list[Entry],
        top_k: int = 5,
        min_score: float = 0.0,
    ) -> list[tuple[Entry, float]]:
        """向量相似度检索

        Args:
            query: 用户查询
            entries: 待检索的Entry列表
            top_k: 返回数量
            min_score: 最小相似度阈值

        Returns:
            [(Entry, score), ...] 按相似度降序排列
        """
        if not entries:
            return []

        # 编码查询和文档
        query_vec = self.encode_query(query)
        doc_texts = [e.compiled for e in entries]
        doc_vecs = self.encode_documents(doc_texts)

        # 计算相似度
        scores = self.compute_similarity(query_vec, doc_vecs)

        # 排序并返回 Top-K
        ranked = sorted(zip(entries, scores), key=lambda x: x[1], reverse=True)

        # 过滤并返回
        results = [(e, s) for e, s in ranked if s >= min_score][:top_k]

        return results


class EmbeddingStore:
    """嵌入向量存储

    管理 Entry 的向量嵌入，支持：
    - 增量添加嵌入
    - 持久化存储
    - 快速相似度检索
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化嵌入存储

        Args:
            storage_path: 存储路径，默认为 ~/.echo/embeddings/
        """
        from pathlib import Path

        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "embeddings"

        self.storage_path.mkdir(parents=True, exist_ok=True)

        # 内存索引: podcast_id -> {entry_id: embedding}
        self._embeddings: dict[str, dict[str, np.ndarray]] = {}

    def add_embedding(self, podcast_id: str, entry_id: str, embedding: np.ndarray):
        """添加嵌入向量

        Args:
            podcast_id: 播客ID
            entry_id: Entry ID
            embedding: 嵌入向量
        """
        if podcast_id not in self._embeddings:
            self._embeddings[podcast_id] = {}

        self._embeddings[podcast_id][entry_id] = embedding
        self._save(podcast_id)

    def get_embeddings(self, podcast_id: str) -> dict[str, np.ndarray]:
        """获取播客的所有嵌入向量"""
        if podcast_id not in self._embeddings:
            self._load(podcast_id)

        return self._embeddings.get(podcast_id, {})

    def search_by_vector(
        self,
        podcast_id: str,
        query_vec: np.ndarray,
        top_k: int = 5,
    ) -> list[tuple[str, float]]:
        """通过向量检索

        Args:
            podcast_id: 播客ID
            query_vec: 查询向量
            top_k: 返回数量

        Returns:
            [(entry_id, score), ...]
        """
        embeddings = self.get_embeddings(podcast_id)

        if not embeddings:
            return []

        # 批量计算相似度
        entry_ids = list(embeddings.keys())
        doc_vecs = np.array([embeddings[eid] for eid in entry_ids])
        scores = self._compute_similarity(query_vec, doc_vecs)

        # 排序
        ranked = sorted(zip(entry_ids, scores), key=lambda x: x[1], reverse=True)

        return ranked[:top_k]

    def _compute_similarity(
        self,
        query_vec: np.ndarray,
        doc_vecs: np.ndarray,
    ) -> np.ndarray:
        """计算余弦相似度"""
        # 假设向量已经归一化
        return np.dot(doc_vecs, query_vec)

    def _save(self, podcast_id: str):
        """保存到文件"""
        import json

        file_path = self.storage_path / f"{podcast_id}.npz"

        if podcast_id not in self._embeddings:
            return

        entry_ids = list(self._embeddings[podcast_id].keys())
        embeddings_array = np.array([
            self._embeddings[podcast_id][eid]
            for eid in entry_ids
        ])

        np.savez_compressed(
            file_path,
            entry_ids=np.array(entry_ids),
            embeddings=embeddings_array,
        )

    def _load(self, podcast_id: str):
        """从文件加载"""
        file_path = self.storage_path / f"{podcast_id}.npz"

        if not file_path.exists():
            self._embeddings[podcast_id] = {}
            return

        try:
            data = np.load(file_path, allow_pickle=True)
            entry_ids = data["entry_ids"]
            embeddings = data["embeddings"]

            self._embeddings[podcast_id] = {
                eid: emb for eid, emb in zip(entry_ids, embeddings)
            }
        except (OSError, IOError, KeyError):
            self._embeddings[podcast_id] = {}

    def delete(self, podcast_id: str):
        """删除播客的嵌入"""
        import os

        if podcast_id in self._embeddings:
            del self._embeddings[podcast_id]

        file_path = self.storage_path / f"{podcast_id}.npz"
        if file_path.exists():
            os.remove(file_path)
