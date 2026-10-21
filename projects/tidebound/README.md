# 借潮而行 · 代码、剧情与版本入口

**当前规范：** [整体制作框架 1.0.0-draft.1](../../ideas/tidebound-framework/README.md)。先读角色阅读路线，再取本任务所需规则、对象卡和场景。[决策与待定项](../../ideas/tidebound-framework/12-DECISIONS.md) 记录最新用户选择；[现状与迁移](../../ideas/tidebound-framework/11-MIGRATION.md) 区分现有代码与目标契约。此更新只改文档，游戏运行版本仍为 v0.6.1。

游戏代码：[Yihancheng0/tidebound-ascii](https://github.com/Yihancheng0/tidebound-ascii)（私有，需要仓库权限）。

当前开发样片为 [v0.6.1 港湾遮挡与动作可读性](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.6.1)。先读 [严格制作门槛](../../ideas/tidebound-production-gates.md)、[本版自查](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.6.1/docs/REVIEW-v0.6.1.md)。新增几何港湾、连续小船、全身避岸和灯鱼/针尾配合解除一只锁鳞。没有自动接回旧六章；浏览器设备和用户美术验收待完成。

原鱼基于 ascii-sharks，上游没有识别到明确许可证，因此不把游戏代码按本素材库的 MIT 授权公开。新增天气研究 ASCII Magic 的四个 MIT 模块，保留授权；详见美术笔记。

## 历史 v0.4 内容与边界

六章小体量迁徙事件、十二目标、六种伙伴、家园安置、灯光/缝合/回声配合、活帆推进、雨与扫光、岛鱼启程。更多鱼、居民日程、分支结局、经济、真实流场、基因与繁殖尚未实现。

- [完整剧情与规则](../../ideas/tidebound-story.md)
- [美术约束、四个参考的预览/源码/授权](../../ideas/tidebound-art.md)
- [机器可读版本索引](versions.json)
- [v0.4.0 代码](https://github.com/Yihancheng0/tidebound-ascii/tree/v0.4.0)
- [v0.4.0 发布包与演示](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.4.0)
- [审查记录](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.4.0/docs/REVIEW-v0.4.md)
- [实现索引](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.4.0/docs/IMPLEMENTATION.md)

## 后续开发怎么衔接

先读整体框架的任务路线，再看对应 tag 的实现与审查记录；剧情和旧美术笔记按本次任务需要读取。确认真实完成范围，再修改。每次更新保留 commit/tag、剧情变化、未实现边界、来源授权、检查范围和对应演示。代码与规范各有一个权威来源，不要只保存聊天摘要。

`v0.3.0` 是之前“借光出湾”的原样归档，含当时的动作缺陷。`v0.4.0` 是本次迁徙扩展。查历史请使用 tag，不要把旧预览当成最新画面。

## 历史 v0.5 开发预览

[代码与发布包](https://github.com/Yihancheng0/tidebound-ascii/releases/tag/v0.5.1) · [开场制作标准](../../ideas/tidebound-opening-standard.md) · [本版自查](https://github.com/Yihancheng0/tidebound-ascii/blob/v0.5.1/docs/REVIEW-v0.5.md)

用户认为 v0.4 看不懂、镜头跳动、灯鱼僵硬、上岛卡住、环境像贴图。本次收敛到港湾开场：解救灯鱼、点空灯、借光过礁口、回望、雨中返港、上岸读航图。改镜头连续合成、灯鱼转向/盘游/避岸、上下文 E、桥面遮挡与通行、暂停/重开，保留原鱼材质。新旧存档隔离。

这是开发预览，尚未得到用户的新美术确认。规则与离线实际引擎流程已检查，浏览器窗口因 URL 识别限制无法操作；不能声称完成真人/设备/排版验收，也不能把自动演示时长当成“五分钟真人玩法”。后续六章仍是旧版事件原型，没有整体重制。

无参数与 `?harbor=1` 进入新版独立档；`?harborDemo=1` 临时演示；`?legacy=1` 恢复旧档。`v0.3.0` / `v0.4.0` 标签保留。故事和风格笔记随当前开发版本更新，历史以对应代码 tag 的文档为准。

## v0.6 当前入口与玩法

无参数 / `?harbor=1`：救灯鱼→点亮实体航灯→引开巨鱼→返港上岸读图→邀请针尾→灯鱼引锁鳞抬颌→针尾缝合→鳃流恢复。结束后回港可点击实体灯架安置/接回灯鱼；E 上下船，H 海图与柔和天气。

新版使用独立 v2 存档，保留 v1 和历史档。`?harborDemo=1` 是实际输入演示，不写正常档。主画面删除浮空名字、方向数字与目标圈。原鱼不改，新的港湾模型为项目程序几何，不声称导入未授权的商业游戏资产。

离线行为、完整输入流程和画布画面已自查。浏览器工具当前在应用设置中关闭；未完成最终设备帧率、DOM 布局或真人无陪同试玩。自动控制器的约 82 秒模拟流程不等于真人时长。旧六章与广阔多海域仍不是本轮精修范围。

v0.6.1 修正水下鱼覆盖船体、实体灯前后排序与安置时叠灯架。锁鳞颌部有厚度和真实开口，眼齿随动；修复缝线读档后保留。初次提示不提前消失，后续停留十二秒恢复。像素回归含旧顺序负向对照；没有把离线检查写成浏览器或用户美术验收。

## 规范发布记录

[framework-v1.0.0-draft.1 主本](https://github.com/Yihancheng0/tidebound-ascii/tree/framework-v1.0.0-draft.1/docs/framework) · 提交 2809dfe17fe419304baa17b27fed86e461dbf91a。公共镜像为原创文档逐文件同步，详细状态见版本索引；运行版本仍为 v0.6.1。
