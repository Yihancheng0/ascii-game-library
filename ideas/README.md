# 游戏设定与设计灵感 / Design notebook

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
