# ASCII 游戏素材与灵感库

> 面向 AI 辅助游戏开发：按中文需求查参考、按英文 slug 取源码。

收录 **12 个资源入口、734 项 ASCII Magic 动画、24 个分类**；附 **634 项动画的源码快照**。核对日期：2026-10-20。

**AI 固定入口：[https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/llms.txt](https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/llms.txt)**

把下面这段发给未来的开发 AI：

```text
请先读取 https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main/START_HERE.md
这是我的 ASCII 游戏素材与灵感库。先按需求检索，再选 3–5 个参考，
列出原始链接、可借鉴点、源码位置和授权状态。需要实现时读取对应源文件，
只把来源已确认的可复用代码或素材纳入项目。
```

## 如何使用

- 项目讨论存档：[设定与设计灵感](ideas/README.md)。包含万物皆鱼世界观、能力组合、巨鱼拖船提案、作品借鉴和脑洞方法；可用 `python scripts/search.py 天空鱼 --kind design_idea` 检索。
- 新增：[60 种鱼设定](ideas/fish-codex.md) · [15 套三鱼组合与 24 条关系](ideas/fish-combinations.md)。可以检索 `python scripts/search.py 遗忘鱼 --kind fish_design` 或 `python scripts/search.py 镜鱼 --kind fish_combo`；这些条目是原创候选规则，不是已实现素材。

- 浏览入口：[资源卡片](resources/) · [游戏开发场景配方](docs/recipes.md) · [AI 检索说明](START_HERE.md)。

- AI 按需读取：[分类目录](catalog/categories.json) → `catalog/ascii-magic/<分类>.json` → 对应源文件。

- 程序读取：[总 JSON](catalog/catalog.json) · [动画 JSONL](catalog/ascii-magic.jsonl) · [紧凑全文索引](llms-full.txt)。

- 克隆后本地搜索（Python 3.10+，仅标准库）：

```sh
git clone https://github.com/Yihancheng0/ascii-game-library.git
cd ascii-game-library
python scripts/search.py 雨夜 霓虹 --limit 8
python scripts/search.py 火焰 --source-only --json
python scripts/search.py --category mascots --limit 8
python scripts/search.py --kind game
python scripts/validate.py
```

关键词默认按 OR 排序；使用 `--all` 要求每个输入词都命中；`--source-only` 只返回本地有源码快照的动画。中文词由分类与关键词规则补充，不是逐项人工翻译。

## 游戏、工具与合集

| 资源 | 用途 | 复用状态 |
|---|---|---|
| [Stone Story RPG](resources/stone-story-rpg.md) | 横版 ASCII RPG，以角色、怪物与场景动画为重点的作品参考。 | `reference_only` |
| [ASCII Patrol](resources/ascii-patrol.md) | 受 Moon Patrol 启发的字符横版街机游戏，提供浏览器版本和 C++ 源码。 | `copyleft_review_required` |
| [Cogmind](resources/cogmind.md) | 科幻机器人 Roguelike，适合借鉴终端界面、粒子效果和高密度战斗反馈。 | `reference_only` |
| [Brogue CE](resources/brogue-ce.md) | 开源地牢 Roguelike，可作为字符地图、地形和视野系统的实现参考。 | `copyleft_review_required` |
| [Candy Box 2](resources/candy-box-2.md) | 浏览器文字与 ASCII 探索游戏，可研究逐步展开的玩法和场景组织。 | `copyleft_review_required` |
| [Asciicker](resources/asciicker.md) | 浏览器三维字符世界演示，适合研究镜头、空间和地形表现。 | `reference_only` |
| [ASCII Art Archive · Animations](resources/asciiart-animations.md) | 可直接在网页查看火焰、星空、隧道、数字雨等字符动画。 | `reference_only` |
| [TerminalTextEffects](resources/terminaltexteffects.md) | Python 终端字符特效引擎，支持运动路径、颜色变化和场景动画。 | `permissive_with_notice` |
| [donut.c / Donut math](resources/donut-c.md) | 作者提供旋转字符圆环的动画、代码和数学推导。 | `reference_only` |
| [ascii-splash](resources/ascii-splash.md) | TypeScript 终端动画项目，含波浪、粒子和自然场景等程序动画。 | `permissive_with_notice` |
| [REXPaint](resources/rexpaint.md) | 免费的 Windows 字符画编辑器，支持图层、前景色、背景色和多种导出。 | `reference_only` |
| [ASCII Magic Art Library](resources/ascii-magic.md) | 大型字符动画库，提供单项 ES 模块、网页播放器和终端播放工具。 | `per_item_license` |

## ASCII Magic 分类

| 分类 | 条目 | 开发用途 |
|---|---:|---|
| [场景与地形 / Landscapes](docs/categories/landscapes.md) | 89 | 关卡背景、营地、探索地图 |
| [界面与终端 / UI](docs/categories/screens.md) | 79 | 游戏菜单、终端交互、任务面板 |
| [数据与仪表 / Live Data](docs/categories/live-data.md) | 29 | 属性面板、排行榜、战斗仪表 |
| [流程与图解 / Explainers](docs/categories/explainers.md) | 36 | 教程、任务树、系统关系图 |
| [标题与文字动画 / Lettering](docs/categories/lettering.md) | 49 | 标题、字幕、解密文字、片尾 |
| [三维形体 / Solids](docs/categories/solids.md) | 25 | 道具展示、立体徽标、旋转拾取物 |
| [宇宙与星空 / Cosmos](docs/categories/cosmos.md) | 18 | 太空背景、星图、飞行场景 |
| [运动与模拟 / Motion Lab](docs/categories/motion-lab.md) | 18 | 弹道、波动、运动规律参考 |
| [天气与自然 / Weather & Wild](docs/categories/weather.md) | 16 | 雨雪、火焰、水面、植物动态 |
| [动物 / Animals](docs/categories/animals.md) | 20 | 生物外观、待机循环、生态场景 |
| [物件 / Things](docs/categories/things.md) | 23 | 交互物件、装置、道具图标 |
| [算法与生成 / Algorithms](docs/categories/algorithms.md) | 25 | 程序背景、分形、细胞自动机 |
| [演示场景与特效 / Demoscene](docs/categories/demoscene.md) | 24 | 技能背景、传送、火焰、隧道 |
| [街机演示 / Arcade](docs/categories/arcade.md) | 18 | 观察规则与节奏；自动播放动画不代表可操作游戏 |
| [边框与分隔 / Rules & Frames](docs/categories/frames.md) | 12 | 对话框、面板、界面分隔 |
| [节庆与庆祝 / Occasions](docs/categories/occasions.md) | 16 | 通关、奖励、庆典 |
| [城市与建筑 / Cities of the World](docs/categories/cities.md) | 54 | 城市关卡、地标、环境气氛 |
| [角色与吉祥物 / Mascots & Characters](docs/categories/mascots.md) | 22 | 角色设计、待机、情绪表达 |
| [状态与反馈 / Empty States & Feedback](docs/categories/empty-states.md) | 22 | 成功、失败、离线、加载反馈 |
| [复古计算机 / Retro Computing](docs/categories/retro.md) | 22 | 开机、黑客关卡、电脑交互 |
| [科学与教学 / Science & Learning](docs/categories/science.md) | 22 | 机制教学、科学题材、可视化 |
| [音乐与声音 / Music & Sound](docs/categories/music.md) | 22 | 节奏游戏、音频可视化、乐器 |
| [食物与饮料 / Food & Drink](docs/categories/food.md) | 22 | 烹饪、商店、经营场景 |
| [印度主题场景 / India](docs/categories/india.md) | 51 | 地域题材环境与节庆气氛 |

## 快照与边界

- 上游固定提交：`de88962156057cbef583bd265bf55e23d6c5e30d`。网站 734 项，仓库 634 项；100 项仅有网页索引，字段明确标识。

- 源码在 `vendor/ascii-magic-art/`，保留原始 LICENSE / NOTICE；两项照片数据有单独说明。

- Arcade 分类是自动播放的小游戏演示；不能把它们直接视为有输入、碰撞、存档的完整游戏。

- 作品参考与可复用代码分开记录；其他作品的美术没有被本库重新授权。

- [更新方法](docs/maintenance.md) · [数据字段](docs/data-model.md) · [复用说明](docs/reuse-guide.md)。

- 这是有日期的整理快照；不包含定时抓取或自动更新任务。
