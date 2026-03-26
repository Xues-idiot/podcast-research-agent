"""国际化支持 - 多语言翻译"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Translation:
    """翻译条目"""
    key: str
    zh: str  # 中文
    en: str  # 英文
    ja: str = ""  # 日文
    ko: str = ""  # 韩文
    es: str = ""  # 西班牙文
    fr: str = ""  # 法文


@dataclass
class Language:
    """语言配置"""
    code: str  # 如 "zh", "en"
    name: str  # 如 "中文", "English"
    native_name: str  # 如 "中文", "English"
    flag: str  # 如 "🇨🇳", "🇺🇸"


class I18nManager:
    """国际化管理器"""

    SUPPORTED_LANGUAGES = {
        "zh": Language("zh", "中文", "中文", "🇨🇳"),
        "en": Language("en", "English", "English", "🇺🇸"),
        "ja": Language("ja", "Japanese", "日本語", "🇯🇵"),
        "ko": Language("ko", "Korean", "한국어", "🇰🇷"),
        "es": Language("es", "Spanish", "Español", "🇪🇸"),
        "fr": Language("fr", "French", "Français", "🇫🇷"),
    }

    def __init__(self, storage_path: Optional[str] = None):
        """初始化国际化管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "i18n"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._translations_file = self.storage_path / "translations.json"
        self._user_translations_file = self.storage_path / "user_translations.json"
        self._translations: dict[str, dict] = {}  # key -> {lang: text}
        self._user_translations: dict[str, dict] = {}
        self._default_lang = "zh"
        self._current_lang = "zh"
        self._load()

    def _load(self):
        """加载翻译数据"""
        # 加载内置翻译
        if self._translations_file.exists():
            try:
                with open(self._translations_file, "r", encoding="utf-8") as f:
                    self._translations = json.load(f)
            except json.JSONDecodeError:
                self._translations = self._get_default_translations()
        else:
            self._translations = self._get_default_translations()

        # 加载用户翻译
        if self._user_translations_file.exists():
            try:
                with open(self._user_translations_file, "r", encoding="utf-8") as f:
                    self._user_translations = json.load(f)
            except json.JSONDecodeError:
                self._user_translations = {}

    def _get_default_translations(self) -> dict:
        """获取默认翻译"""
        translations = {}

        default_items = [
            # 通用
            ("common.save", {"zh": "保存", "en": "Save", "ja": "保存", "ko": "저장", "es": "Guardar", "fr": "Enregistrer"}),
            ("common.cancel", {"zh": "取消", "en": "Cancel", "ja": "キャンセル", "ko": "취소", "es": "Cancelar", "fr": "Annuler"}),
            ("common.delete", {"zh": "删除", "en": "Delete", "ja": "削除", "ko": "삭제", "es": "Eliminar", "fr": "Supprimer"}),
            ("common.edit", {"zh": "编辑", "en": "Edit", "ja": "編集", "ko": "편집", "es": "Editar", "fr": "Modifier"}),
            ("common.search", {"zh": "搜索", "en": "Search", "ja": "検索", "ko": "검색", "es": "Buscar", "fr": "Rechercher"}),
            ("common.loading", {"zh": "加载中...", "en": "Loading...", "ja": "読み込み中...", "ko": "로딩 중...", "es": "Cargando...", "fr": "Chargement..."}),
            ("common.error", {"zh": "错误", "en": "Error", "ja": "エラー", "ko": "오류", "es": "Error", "fr": "Erreur"}),
            ("common.success", {"zh": "成功", "en": "Success", "ja": "成功", "ko": "성공", "es": "Éxito", "fr": "Succès"}),

            # 研究
            ("research.title", {"zh": "播客研究", "en": "Podcast Research", "ja": "ポッドキャスト研究", "ko": "팟캐스트 연구", "es": "Investigación de Podcast", "fr": "Recherche de Podcast"}),
            ("research.start", {"zh": "开始研究", "en": "Start Research", "ja": "研究を開始", "ko": "연구 시작", "es": "Iniciar Investigación", "fr": "Démarrer la Recherche"}),
            ("research.progress", {"zh": "研究进度", "en": "Research Progress", "ja": "研究の進捗", "ko": "연구 진행률", "es": "Progreso de Investigación", "fr": "Progression de la Recherche"}),
            ("research.completed", {"zh": "研究完成", "en": "Research Completed", "ja": "研究完了", "ko": "연구 완료", "es": "Investigación Completada", "fr": "Recherche Terminée"}),

            # 要点
            ("keypoint.title", {"zh": "要点", "en": "Key Points", "ja": "重要ポイント", "ko": "핵심 포인트", "es": "Puntos Clave", "fr": "Points Clés"}),
            ("keypoint.importance", {"zh": "重要性", "en": "Importance", "ja": "重要度", "ko": "중요도", "es": "Importancia", "fr": "Importance"}),
            ("keypoint.high", {"zh": "高", "en": "High", "ja": "高", "ko": "높음", "es": "Alto", "fr": "Élevé"}),
            ("keypoint.medium", {"zh": "中", "en": "Medium", "ja": "中", "ko": "보통", "es": "Medio", "fr": "Moyen"}),
            ("keypoint.low", {"zh": "低", "en": "Low", "ja": "低", "ko": "낮음", "es": "Bajo", "fr": "Faible"}),

            # 摘要
            ("summary.title", {"zh": "摘要", "en": "Summary", "ja": "要約", "ko": "요약", "es": "Resumen", "fr": "Résumé"}),
            ("summary.generate", {"zh": "生成摘要", "en": "Generate Summary", "ja": "要約を生成", "ko": "요약 생성", "es": "Generar Resumen", "fr": "Générer le Résumé"}),

            # 导出
            ("export.title", {"zh": "导出", "en": "Export", "ja": "エクスポート", "ko": "내보내기", "es": "Exportar", "fr": "Exporter"}),
            ("export.format", {"zh": "导出格式", "en": "Export Format", "ja": "エクスポート形式", "ko": "내보내기 형식", "es": "Formato de Exportación", "fr": "Format d'Exportation"}),
            ("export.json", {"zh": "JSON", "en": "JSON", "ja": "JSON", "ko": "JSON", "es": "JSON", "fr": "JSON"}),
            ("export.markdown", {"zh": "Markdown", "en": "Markdown", "ja": "Markdown", "ko": "마크다운", "es": "Markdown", "fr": "Markdown"}),
            ("export.html", {"zh": "HTML", "en": "HTML", "ja": "HTML", "ko": "HTML", "es": "HTML", "fr": "HTML"}),

            # 导航
            ("nav.home", {"zh": "首页", "en": "Home", "ja": "ホーム", "ko": "홈", "es": "Inicio", "fr": "Accueil"}),
            ("nav.research", {"zh": "研究", "en": "Research", "ja": "研究", "ko": "연구", "es": "Investigación", "fr": "Recherche"}),
            ("nav.history", {"zh": "历史", "en": "History", "ja": "履歴", "ko": "기록", "es": "Historial", "fr": "Historique"}),
            ("nav.knowledge", {"zh": "知识库", "en": "Knowledge", "ja": "ナレッジ", "ko": "지식", "es": "Conocimiento", "fr": "Connaissance"}),
            ("nav.settings", {"zh": "设置", "en": "Settings", "ja": "設定", "ko": "설정", "es": "Configuración", "fr": "Paramètres"}),
        ]

        for key, texts in default_items:
            translations[key] = texts

        return translations

    def _save(self):
        """保存翻译数据"""
        temp_file = self._user_translations_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._user_translations, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._user_translations_file)

    def set_language(self, lang: str) -> bool:
        """设置当前语言

        Args:
            lang: 语言代码

        Returns:
            是否成功
        """
        if lang in self.SUPPORTED_LANGUAGES:
            self._current_lang = lang
            return True
        return False

    def get_language(self) -> str:
        """获取当前语言"""
        return self._current_lang

    def get_languages(self) -> list[dict]:
        """获取支持的语言列表"""
        return [
            {
                "code": code,
                "name": lang.name,
                "native_name": lang.native_name,
                "flag": lang.flag,
            }
            for code, lang in self.SUPPORTED_LANGUAGES.items()
        ]

    def t(self, key: str, lang: str = None) -> str:
        """翻译

        Args:
            key: 翻译键
            lang: 目标语言

        Returns:
            翻译文本
        """
        lang = lang or self._current_lang

        # 先检查用户翻译
        if key in self._user_translations:
            user_texts = self._user_translations[key]
            if lang in user_texts:
                return user_texts[lang]

        # 再检查内置翻译
        if key in self._translations:
            texts = self._translations[key]
            if lang in texts:
                return texts[lang]
            # 尝试英文作为后备
            if "en" in texts:
                return texts["en"]
            # 返回中文作为最后后备
            if "zh" in texts:
                return texts["zh"]

        # 返回键名
        return key

    def tpl(self, key: str, params: dict = None, lang: str = None) -> str:
        """带参数的翻译

        Args:
            key: 翻译键
            params: 参数
            lang: 目标语言

        Returns:
            翻译文本
        """
        text = self.t(key, lang)
        if params:
            for k, v in params.items():
                text = text.replace(f"{{{k}}}", str(v))
        return text

    def add_translation(self, key: str, lang: str, text: str):
        """添加用户翻译

        Args:
            key: 翻译键
            lang: 语言
            text: 翻译文本
        """
        if key not in self._user_translations:
            self._user_translations[key] = {}
        self._user_translations[key][lang] = text
        self._save()

    def remove_translation(self, key: str, lang: str = None):
        """移除用户翻译

        Args:
            key: 翻译键
            lang: 语言，为空则移除整个键
        """
        if key in self._user_translations:
            if lang:
                if lang in self._user_translations[key]:
                    del self._user_translations[key][lang]
            else:
                del self._user_translations[key]
            self._save()

    def get_all_translations(self, lang: str = None) -> dict:
        """获取所有翻译

        Args:
            lang: 语言筛选

        Returns:
            翻译字典
        """
        lang = lang or self._current_lang
        result = {}

        all_keys = set(self._translations.keys()) | set(self._user_translations.keys())
        for key in all_keys:
            result[key] = self.t(key, lang)

        return result


# 全局实例
_i18n_manager: Optional[I18nManager] = None


def get_i18n_manager() -> I18nManager:
    """获取全局国际化管理器"""
    global _i18n_manager
    if _i18n_manager is None:
        _i18n_manager = I18nManager()
    return _i18n_manager
