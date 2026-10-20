# 给开发 AI 的入口

固定入口：https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/llms.txt
仓库：https://github.com/Yihancheng0/ascii-game-library

1. 确认需求：玩法参考 / 背景 / 角色 / 技能特效 / 标题转场 / UI / 3D。
2. 先读 `https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/catalog/resources.json` 和 `https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/catalog/categories.json`。
3. 只取相关分片，例如 `https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/catalog/ascii-magic/weather.json`；避免一开始载入全部源码或总 JSON。
4. 用 `name`、`tags`、`aliases_zh`、`description`、`search_text` 搜索；中文需求同时匹配英文近义词。标签来自规则，有误差。
5. 从 3–5 项候选给出：preview_url、想借鉴的点、source_status、license 与修改方案。
6. 对 `vendored_at_pinned_commit`，可直接读 `raw_source_url`；也可克隆后读 `local_source_path`。保留源码所引用的 lib/runtime 和授权声明。
7. `website_only_not_in_pinned_repository` 表示尚未收集该项源码；`website_source_candidate_url` 未验证，不能声称它一定可用。先打开网页再决定是否另行取源。
8. `reference_only` 项目用于研究表现与设计；不要把链接当成可复制美术的授权。
9. 字符模块生成的是 `draw(t)` 帧。要做游戏，需要另外设计输入、角色状态、地图、碰撞、胜负与存档；自动播放的 Arcade 动画不等于完整玩法。
10. 优先按项目需求选普通 ASCII 或 Unicode 字符集，核对字体、字符单元比例、色板和刷新性能；查看模块 `meta` 里的实际参数。
11. 用户询问本项目世界观、玩法与前序讨论时，读取 `https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/catalog/design-ideas.json`，按 `document_path` 只取相关笔记。入口见 [设定与灵感](ideas/README.md)。保留用户提案、候选和同意试验的状态，不把笔记视为已实现功能。
12. 查询具体能力鱼与三鱼组合时，使用 `catalog/fish-species.json`（60 种）、`catalog/fish-combinations.json`（15 套三鱼组合）、`catalog/fish-interactions.json`（24 条关系）。每种鱼有稳定 ID、条件、代价、克制和关联组合；详见 [鱼设定集](ideas/fish-codex.md) 与 [组合推演](ideas/fish-combinations.md)。均为原创候选设计，未实现与未平衡；现实生物来源只说明启发，不证明虚构技能。

## 提示词示例

```text
从此库选 5 个“雨夜霓虹城市”的背景参考。读取 landscapes、cities、weather 分片，
同时检索 neon / rain / night。给出单项预览、源码链接、推荐改法和授权证据。
```

```text
为字符地牢做战斗反馈设计：参考 Cogmind 的表现，再找 3 个有源码的火焰/烟雾/粒子动画。
区分作品参考与可复用代码；提出低密度、不会遮住敌人的效果方案。
```

```text
为单色终端游戏找角色待机、标题出现、场景切换参考。输出可实施的小方案，
包括字符网格、时长、调色板、输入与动画状态关系，不直接假定原动画已有游戏逻辑。
```

## 本地检索

Python 3.10+；`python scripts/search.py --help`。查询结果包含链接和授权状态，`--json` 可供下一步程序读取。

仅下载 llms.txt 不会让所有 AI 自动记住此库；后续会话请提供本页 URL，或把本仓库加入该项目的上下文。
