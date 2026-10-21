# 游戏设定与设计灵感 / Design notebook

[一起看：作者审阅导览](tidebound-human-review.md) 将整体框架整理成八个体验主题；给作者看画面、动作和交互，机器规则留在制作侧。

当前制作规范：[借潮而行整体框架 1.0.0-draft.1](tidebound-framework/README.md)。13 章、48 条规则索引、对象卡、动画/交互模板与验收场景；先保留原鱼气质，再通过结构与样片约束环境。它是规范草案，不是新游戏版本。

这里保存讨论中的设定、作品启发、玩法候选和取舍，方便以后查询。记录日期：2026-10-20。

**状态约定：** `approved_experiment` 表示用户同意尝试；`user_proposed` 表示用户提出的世界设定；`candidate` 表示待比较建议。它们都不自动等于已实现。实际完成情况以游戏工程和验收为准。

| 文档 | 查询内容 |
|---|---|
| [万物皆鱼：世界规则与能力组合](fish-world.md) | 天空鱼、昼夜翻身、海鱼、岛鱼、船鱼；只有鱼能对抗鱼；条件、代价与组合 |
| [玩法提案与本轮选择](ocean-proposals.md) | A 巨鱼拖船（同意试验）、B 倒影垂钓、C 迁徙岛鱼；捕鱼闭环、生态收藏、海图寻秘 |
| [作品启发对照](game-references.md) | 泰拉瑞亚、饥荒、重生细胞、GRIS、空洞骑士、武士零、小小梦魇2、渔力全开，以及前序参考 |
| [如何产生并筛选奇特玩法](creative-method.md) | 翻转常识、角色视角、规则组合、反复游玩的检验与最小原型 |
| [六十种鱼设定集](fish-codex.md) | 60 种鱼的能力、条件、代价、克制、外形与现实灵感来源 |
| [带着三种鱼会发生什么](fish-combinations.md) | 15 套三鱼组合、24 条配合与互克，包括危险共生、失败场景与最小验证 |

机器索引：[catalog/design-ideas.json](../catalog/design-ideas.json)。例如：

```sh
python scripts/search.py 天空鱼 --kind design_idea
python scripts/search.py 拖船 --kind design_idea --json
python scripts/search.py 能力 组合 --kind design_idea --all
python scripts/search.py 空洞骑士 --kind design_idea
python scripts/search.py 遗忘鱼 --kind fish_design --json
python scripts/search.py 三鱼组合 --kind fish_combo --limit 15
python scripts/search.py 镜鱼 --kind fish_combo
```

这是本项目的设计笔记，不是被引用游戏的源码或美术授权；`reference_only` 的作品保持原有权利归属。设定的原创扩展与用户原话摘要分开标注，避免把编辑建议写成已确认需求。

## 借潮而行 · 可玩版本对接

[六章剧情与伙伴安置](tidebound-story.md) · [美术与天气适配](tidebound-art.md) · [代码版本、审查与交接](../projects/tidebound/README.md)。这些笔记保留设计边界，实际代码与演示见私有开发版本。

[港湾开场制作标准与未验收项](tidebound-opening-standard.md)（v0.5 开发预览，后续六章未整体重制）。

- [v0.6 港湾严格制作门槛](tidebound-production-gates.md)：原鱼不变、全身避岸、实体器官交互与分开验收。
