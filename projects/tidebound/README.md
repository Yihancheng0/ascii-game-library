# 借潮而行 · 代码、剧情与版本入口

游戏代码：[Yihancheng0/tidebound-ascii](https://github.com/Yihancheng0/tidebound-ascii)（私有，需要仓库权限）。

当前开发预览为 [v0.5.1 港湾开场重做](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.5.1)，先读 [开场制作标准](../../ideas/tidebound-opening-standard.md)。下面的六章是 v0.4 历史实现，不代表已按新版美术标准重制。

原鱼基于 ascii-sharks，上游没有识别到明确许可证，因此不把游戏代码按本素材库的 MIT 授权公开。新增天气研究 ASCII Magic 的四个 MIT 模块，保留授权；详见美术笔记。

## 本次新增与边界

六章小体量迁徙事件、十二目标、六种伙伴、家园安置、灯光/缝合/回声配合、活帆推进、雨与扫光、岛鱼启程。更多鱼、居民日程、分支结局、经济、真实流场、基因与繁殖尚未实现。

- [完整剧情与规则](../../ideas/tidebound-story.md)
- [美术约束、四个参考的预览/源码/授权](../../ideas/tidebound-art.md)
- [机器可读版本索引](versions.json)
- [v0.4.0 代码](https://github.com/Yihancheng0/tidebound-ascii/tree/v0.4.0)
- [v0.4.0 发布包与演示](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.4.0)
- [审查记录](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.4.0/docs/REVIEW-v0.4.md)
- [实现索引](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.4.0/docs/IMPLEMENTATION.md)

## 后续开发怎么衔接

先看对应 tag 的 README、STORY_BIBLE、ART_DIRECTION、IMPLEMENTATION 和 REVIEW。确认真实完成范围，再修改。每次更新保留 commit/tag、剧情变化、未实现边界、来源授权、检查范围和对应演示。代码与故事各有一个权威来源，不要只保存聊天摘要。

`v0.3.0` 是之前“借光出湾”的原样归档，含当时的动作缺陷。`v0.4.0` 是本次迁徙扩展。查历史请使用 tag，不要把旧预览当成最新画面。

## v0.5 当前开发预览

[代码与发布包](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.5.1) · [开场制作标准](../../ideas/tidebound-opening-standard.md) · [本版自查](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.5.1/docs/REVIEW-v0.5.md)

用户认为 v0.4 看不懂、镜头跳动、灯鱼僵硬、上岛卡住、环境像贴图。本次收敛到港湾开场：解救灯鱼、点空灯、借光过礁口、回望、雨中返港、上岸读航图。改镜头连续合成、灯鱼转向/盘游/避岸、上下文 E、桥面遮挡与通行、暂停/重开，保留原鱼材质。新旧存档隔离。

这是开发预览，尚未得到用户的新美术确认。规则与离线实际引擎流程已检查，浏览器窗口因 URL 识别限制无法操作；不能声称完成真人/设备/排版验收，也不能把自动演示时长当成“五分钟真人玩法”。后续六章仍是旧版事件原型，没有整体重制。

无参数与 `?harbor=1` 进入新版独立档；`?harborDemo=1` 临时演示；`?legacy=1` 恢复旧档。`v0.3.0` / `v0.4.0` 标签保留。故事和风格笔记随当前开发版本更新，历史以对应代码 tag 的文档为准。
