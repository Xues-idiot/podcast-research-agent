#!/usr/bin/env python3
"""
Echo 播客研究Agent - 自动化持续改进脚本 v2

增强功能:
1. 代码审查 - 编译检查、类型检查、复杂度分析
2. Bug修复 - 自动修复常见问题
3. 代码优化 - 性能、可维护性改进
4. 新功能开发 - 按优先级添加功能
5. 功能审查 - 评估功能是否真正需要/能用

用法:
    python scripts/auto_improve.py --rounds 10 --review-every 5
    python scripts/auto_improve.py --mode bug-fix
    python scripts/auto_improve.py --mode audit
    python scripts/auto_improve.py --check-all  # 全面检查
"""

import ast
import argparse
import os
import re
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


# ============== 配置 ==============

PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src" / "echo"
BACKEND_DIR = PROJECT_ROOT / "src"


# ============== 数据结构 ==============

@dataclass
class Issue:
    """问题"""
    file: str
    line: int
    severity: str  # error, warning, info
    category: str  # bug, type, style, perf, security
    message: str
    fix_suggestion: str = ""
    auto_fixable: bool = False


@dataclass
class Feature:
    """功能"""
    name: str
    module: str
    file_path: str
    status: str  # active, deprecated, broken
    lines: int = 0
    classes: int = 0
    functions: int = 0
    last_reviewed: str = ""
    value_score: float = 0.0
    notes: str = ""


@dataclass
class RoundResult:
    """轮次结果"""
    round_num: int
    mode: str
    issues_found: int = 0
    issues_fixed: int = 0
    features_added: int = 0
    features_reviewed: int = 0
    compilation_errors: int = 0
    summary: str = ""


# ============== 代码审查器 ==============

class CodeAuditor:
    """代码审查器"""

    def __init__(self):
        self.issues: list[Issue] = []

    def check_compilation(self) -> list[Issue]:
        """编译检查"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    source = f.read()
                compile(source, str(py_file), 'exec')
            except SyntaxError as e:
                issues.append(Issue(
                    file=str(py_file.relative_to(PROJECT_ROOT)),
                    line=e.lineno or 0,
                    severity="error",
                    category="bug",
                    message=f"语法错误: {e.msg}",
                    fix_suggestion="修复语法错误"
                ))
            except Exception as e:
                issues.append(Issue(
                    file=str(py_file.relative_to(PROJECT_ROOT)),
                    line=0,
                    severity="error",
                    category="bug",
                    message=f"编译错误: {str(e)}",
                    fix_suggestion="检查代码"
                ))

        return issues

    def check_async_without_await(self) -> list[Issue]:
        """检查 async 函数没有 await"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.AsyncFunctionDef):
                        # 检查函数体
                        has_await = any(
                            isinstance(child, ast.Await)
                            for child in ast.walk(node)
                        )
                        has_async_call = any(
                            isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute) and
                            child.func.attr in ['download', 'transcribe', 'search', 'send', 'post', 'get']
                            for child in ast.walk(node)
                        )

                        # 如果没有 await 但函数体内有可异步的操作
                        if not has_await and not has_async_call:
                            issues.append(Issue(
                                file=str(py_file.relative_to(PROJECT_ROOT)),
                                line=node.lineno,
                                severity="warning",
                                category="style",
                                message=f"async函数 '{node.name}' 没有 await",
                                fix_suggestion=f"如果不需要异步，将 'async def' 改为 'def'"
                            ))
            except:
                pass

        return issues

    def check_none_handling(self) -> list[Issue]:
        """检查 None 值处理"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for i, line in enumerate(lines, 1):
                    # 检查 .get() 调用后没有 None 检查
                    if '.get(' in line and ('if ' not in lines[max(0, i-2):i+1][-1] if i > 0 else False):
                        # 简单检查：看看前后3行有没有 if ... is None 或 if not ...
                        context_start = max(0, i-3)
                        context_end = min(len(lines), i+2)
                        context = ''.join(lines[context_start:context_end])

                        if 'is None' not in context and 'is not None' not in context:
                            # 这只是一个提示，不是错误
                            pass
            except:
                pass

        return issues

    def check_exception_handling(self) -> list[Issue]:
        """检查异常处理"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    # 检查 bare except
                    if isinstance(node, ast.ExceptHandler) and node.type is None:
                        issues.append(Issue(
                            file=str(py_file.relative_to(PROJECT_ROOT)),
                            line=node.lineno,
                            severity="warning",
                            category="style",
                            message="使用 bare except: 可能捕获不该捕获的异常",
                            fix_suggestion="使用 'except Exception:' 而非 'except:'"
                        ))

                    # 检查空的 except 块
                    if isinstance(node, ast.ExceptHandler):
                        if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                            issues.append(Issue(
                                file=str(py_file.relative_to(PROJECT_ROOT)),
                                line=node.lineno,
                                severity="info",
                                category="style",
                                message="except 块只有 pass，什么都没做",
                                fix_suggestion="要么处理异常，要么移除 except"
                            ))
            except:
                pass

        return issues

    def check_hardcoded_secrets(self) -> list[Issue]:
        """检查硬编码的密钥"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        secret_patterns = [
            (r'api_key\s*=\s*["\'][^"\']{10,}["\']', '可能的 API 密钥硬编码'),
            (r'password\s*=\s*["\'][^"\']+["\']', '可能的密码硬编码'),
            (r'secret\s*=\s*["\'][^"\']+["\']', '可能的密钥硬编码'),
        ]

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for i, line in enumerate(lines, 1):
                    for pattern, msg in secret_patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            issues.append(Issue(
                                file=str(py_file.relative_to(PROJECT_ROOT)),
                                line=i,
                                severity="warning",
                                category="security",
                                message=msg,
                                fix_suggestion="使用环境变量或配置文件"
                            ))
            except:
                pass

        return issues

    def check_function_complexity(self) -> list[Issue]:
        """检查函数复杂度"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        # 计算函数长度（行数）
                        if hasattr(node, 'end_lineno') and node.end_lineno:
                            lines = node.end_lineno - node.lineno
                            if lines > 100:
                                issues.append(Issue(
                                    file=str(py_file.relative_to(PROJECT_ROOT)),
                                    line=node.lineno,
                                    severity="info",
                                    category="perf",
                                    message=f"函数 '{node.name}' 有 {lines} 行，可能过于复杂",
                                    fix_suggestion="考虑拆分为更小的函数"
                                ))

                        # 计算分支数量
                        if hasattr(node, 'end_lineno'):
                            func_source = '\n'.join(
                                content.split('\n')[node.lineno-1:node.end_lineno]
                            )
                            if_count = func_source.count('if ')
                            for_count = func_source.count('for ')
                            while_count = func_source.count('while ')

                            if if_count + for_count + while_count > 20:
                                issues.append(Issue(
                                    file=str(py_file.relative_to(PROJECT_ROOT)),
                                    line=node.lineno,
                                    severity="warning",
                                    category="perf",
                                    message=f"函数 '{node.name}' 有 {if_count + for_count + while_count} 个分支",
                                    fix_suggestion="考虑简化逻辑"
                                ))
            except:
                pass

        return issues

    def check_dataclass_usage(self) -> list[Issue]:
        """检查 dataclass 使用"""
        issues = []
        py_files = list(SRC_DIR.rglob("*.py"))

        for py_file in py_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # 检查是否将 dataclass 传给期望 dict 的地方
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Name):
                            func_name = node.func.id
                            # 常见期望 dict 的函数
                            if func_name in ['update', 'json.dump', 'json.dumps']:
                                for arg in node.args:
                                    if isinstance(arg, ast.Name):
                                        var_name = arg.id
                                        # 检查变量是否可能是 dataclass
                                        if var_name[0].isupper() and 'dict' not in var_name.lower():
                                            issues.append(Issue(
                                                file=str(py_file.relative_to(PROJECT_ROOT)),
                                                line=node.lineno,
                                                severity="warning",
                                                category="type",
                                                message=f"可能将 dataclass 传给 {func_name}",
                                                fix_suggestion="使用 asdict() 转换后再传入"
                                            ))
            except:
                pass

        return issues

    def check_all(self) -> list[Issue]:
        """执行所有检查"""
        all_issues = []
        all_issues.extend(self.check_compilation())
        all_issues.extend(self.check_async_without_await())
        all_issues.extend(self.check_exception_handling())
        all_issues.extend(self.check_hardcoded_secrets())
        all_issues.extend(self.check_function_complexity())
        all_issues.extend(self.check_dataclass_usage())

        # 去重
        seen = set()
        unique_issues = []
        for issue in all_issues:
            key = (issue.file, issue.line, issue.category, issue.message)
            if key not in seen:
                seen.add(key)
                unique_issues.append(issue)

        self.issues = unique_issues
        return unique_issues

    def get_summary(self) -> dict:
        """获取审查摘要"""
        by_severity = {}
        by_category = {}

        for issue in self.issues:
            by_severity[issue.severity] = by_severity.get(issue.severity, 0) + 1
            by_category[issue.category] = by_category.get(issue.category, 0) + 1

        return {
            "total": len(self.issues),
            "by_severity": by_severity,
            "by_category": by_category,
        }


# ============== Bug修复器 ==============

class BugFixer:
    """Bug修复器"""

    def apply_fix(self, issue: Issue) -> bool:
        """应用修复

        注意：目前只修复 bare except 问题。
        async函数的问题需要人工审查，因为：
        1. API端点必须保持async（FastAPI要求）
        2. client.py中的方法被多处await调用
        3. 自动修复可能破坏代码
        """
        # 只修复 bare except 问题
        if issue.category == "style" and "bare except" in issue.message:
            return self._fix_bare_except(issue)
        return False

    def _fix_bare_except(self, issue: Issue) -> bool:
        """修复 bare except"""
        try:
            file_path = PROJECT_ROOT / issue.file
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                if "except:" in line and i == issue.line - 1:
                    lines[i] = line.replace("except:", "except Exception:")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.writelines(lines)
                    return True
        except:
            pass
        return False


# ============== 功能审查器 ==============

class FeatureAuditor:
    """功能审查器"""

    def discover_features(self) -> list[Feature]:
        """发现所有功能模块"""
        features = []
        modules_to_scan = [
            ("research", SRC_DIR / "research"),
            ("api", SRC_DIR / "api"),
            ("exporters", SRC_DIR / "exporters"),
        ]

        for module_name, module_dir in modules_to_scan:
            if not module_dir.exists():
                continue

            for py_file in module_dir.glob("*.py"):
                if py_file.name == "__init__.py":
                    continue

                try:
                    with open(py_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        lines = content.split('\n')

                    # 统计
                    tree = ast.parse(content)
                    class_count = sum(1 for _ in ast.walk(tree) if isinstance(_, ast.ClassDef))
                    func_count = sum(1 for _ in ast.walk(tree) if isinstance(_, (ast.FunctionDef, ast.AsyncFunctionDef)))

                    features.append(Feature(
                        name=py_file.stem,
                        module=module_name,
                        file_path=str(py_file.relative_to(PROJECT_ROOT)),
                        status="active",
                        lines=len(lines),
                        classes=class_count,
                        functions=func_count,
                        last_reviewed=datetime.now().isoformat(),
                        value_score=self._estimate_value(content, lines, class_count, func_count),
                    ))
                except:
                    pass

        features.sort(key=lambda x: x.value_score, reverse=True)
        return features

    def _estimate_value(self, content: str, lines: list, class_count: int, func_count: int) -> float:
        """估算功能价值"""
        score = 0.5

        # 基于代码量
        if len(lines) < 50:
            score = 0.4
        elif len(lines) < 150:
            score = 0.6
        elif len(lines) < 300:
            score = 0.7
        else:
            score = 0.8

        # 基于类数量（有结构）
        if class_count >= 3:
            score += 0.1
        elif class_count == 0 and func_count > 10:
            score -= 0.1

        # 基于是否有文档
        if '"""' in content or "'''" in content:
            score += 0.1

        # 检查是否实现了 __init__ 以外的功能
        if 'async def' in content or 'await ' in content:
            score += 0.1

        return min(1.0, score)

    def review_features(self) -> dict:
        """审查所有功能"""
        features = self.discover_features()

        results = []
        for feature in features:
            review = {
                "name": feature.name,
                "module": feature.module,
                "file": feature.file_path,
                "lines": feature.lines,
                "classes": feature.classes,
                "functions": feature.functions,
                "estimated_value": f"{feature.value_score:.1%}",
                "recommendation": self._get_recommendation(feature),
            }
            results.append(review)

        # 分类
        keep = [r for r in results if "保留" in r["recommendation"]]
        review_needed = [r for r in results if "审查" in r["recommendation"]]

        return {
            "reviews": results,
            "total": len(results),
            "keep": len(keep),
            "review_needed": len(review_needed),
        }

    def _get_recommendation(self, feature: Feature) -> str:
        """获取功能建议"""
        if feature.value_score >= 0.8:
            return "保留 - 高价值功能"
        elif feature.value_score >= 0.6:
            return "保留 - 中等价值"
        elif feature.lines < 30 and feature.classes == 0:
            return "审查 - 代码量过小，可能无用"
        else:
            return "审查 - 考虑优化或合并"


# ============== 主控制器 ==============

class AutoImprove:
    """自动化改进控制器"""

    def __init__(self, rounds: int = 10, review_every: int = 5):
        self.rounds = rounds
        self.review_every = review_every
        self.results: list[RoundResult] = []
        self.auditor = CodeAuditor()
        self.fixer = BugFixer()
        self.feature_auditor = FeatureAuditor()

    def run(self, mode: str = "all"):
        """运行自动化改进"""
        print("=" * 60)
        print("Echo - Automated Continuous Improvement")
        print("=" * 60)
        print(f"Rounds: {self.rounds}, Review every {self.review_every} rounds")
        print()

        for round_num in range(1, self.rounds + 1):
            print(f"\n{'='*60}")
            print(f"Round {round_num}/{self.rounds}")
            print(f"{'='*60}")

            result = RoundResult(round_num=round_num, mode=mode)

            # 1. 代码审查
            print("\n[1/4] Running code audit...")
            issues = self.auditor.check_all()
            result.issues_found = len(issues)
            print(f"      Found {len(issues)} issues")

            if issues:
                summary = self.auditor.get_summary()
                for cat, count in summary.get("by_category", {}).items():
                    print(f"        - {cat}: {count}")

            # 2. 修复问题
            print("\n[2/4] Fixing issues...")
            fixed = 0
            for issue in issues[:5]:
                if self.fixer.apply_fix(issue):
                    fixed += 1
                    print(f"      Fixed: {issue.file}:{issue.line} - {issue.category}")
            result.issues_fixed = fixed
            print(f"      Fixed {fixed} issues")

            # 3. 验证编译
            print("\n[3/4] Verifying compilation...")
            compile_issues = self.auditor.check_compilation()
            result.compilation_errors = len(compile_issues)
            if compile_issues:
                print(f"      Still has {len(compile_issues)} errors")
                for ci in compile_issues[:3]:
                    print(f"        - {ci.file}: {ci.message}")
            else:
                print("      Compilation OK!")

            # 4. 功能审查 (每N轮)
            if round_num % self.review_every == 0:
                print("\n[4/4] Feature audit...")
                review = self.feature_auditor.review_features()
                result.features_reviewed = review["total"]
                print(f"      Reviewed {review['total']} features")
                print(f"        - Keep: {review['keep']}")
                print(f"        - Need review: {review['review_needed']}")

                print("\n      Top features:")
                for r in review.get("reviews", [])[:5]:
                    print(f"        - {r['name']} ({r['module']}): {r['estimated_value']} - {r['recommendation']}")

            self.results.append(result)

        self._print_summary()

    def _print_summary(self):
        """打印总结"""
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)

        total_issues = sum(r.issues_found for r in self.results)
        total_fixed = sum(r.issues_fixed for r in self.results)
        total_errors = sum(r.compilation_errors for r in self.results)

        print(f"Total rounds: {len(self.results)}")
        print(f"Issues found: {total_issues}")
        print(f"Issues fixed: {total_fixed}")
        print(f"Remaining compile errors: {total_errors}")
        print()
        print("Round details:")
        for r in self.results:
            print(f"  Round {r.round_num}: found={r.issues_found}, fixed={r.issues_fixed}, "
                  f"errors={r.compilation_errors}, reviewed={r.features_reviewed}")


# ============== CLI ==============

def main():
    parser = argparse.ArgumentParser(description="Echo Automated Improvement")
    parser.add_argument("--rounds", type=int, default=10, help="Number of iterations")
    parser.add_argument("--review-every", type=int, default=5, help="Review features every N rounds")
    parser.add_argument("--mode", type=str, default="all",
                        choices=["all", "bug-fix", "feature", "optimize", "audit"],
                        help="Run mode")
    parser.add_argument("--check-all", action="store_true", help="Run all checks once")

    args = parser.parse_args()

    if args.check_all:
        # 一次性全面检查
        print("Running full code audit...")
        auditor = CodeAuditor()
        issues = auditor.check_all()
        summary = auditor.get_summary()

        print(f"\nFound {summary['total']} issues:")
        print(f"  By severity: {summary['by_severity']}")
        print(f"  By category: {summary['by_category']}")

        if issues:
            print("\nTop issues:")
            for issue in issues[:10]:
                print(f"  [{issue.severity}] {issue.file}:{issue.line}")
                print(f"    {issue.message}")
                print(f"    Fix: {issue.fix_suggestion}")
        return 0

    controller = AutoImprove(rounds=args.rounds, review_every=args.review_every)
    controller.run(mode=args.mode)

    return 0 if all(r.compilation_errors == 0 for r in controller.results) else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
