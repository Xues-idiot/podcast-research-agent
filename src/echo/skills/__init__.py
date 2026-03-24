# Skills 模块

本模块定义了 Echo 的技能系统。

## 内置技能

技能定义在 `echo/skills/` 目录中。

### 加载技能

```python
from echo.skills import load_builtin_skills, SkillRegistry

# 加载内置技能
registry = load_builtin_skills()

# 查找最佳匹配
skill = registry.find_best_match("生成播客")
```
