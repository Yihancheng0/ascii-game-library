# 借潮而行 · 代码、剧情与版本入口

最新护送研究为 [岩间微光·护送一程 0.1.0](../../ideas/tidebound-cove-escort.md)，私有标签 `cove-escort-v0.1.0`。旧 E1 保留；新切片的实现/离线/设备/用户验收分开记录，默认 v0.6.1 不变。

先前 E1 研究为 [岩间微光 0.1.0](../../ideas/tidebound-cove-study.md)，私有标签 `cove-study-v0.1.0`。一屏可操作浅湾，属于 E1；完整捕食护送、浏览器设备和用户艺术验收待验证。版本与证据范围见 versions.json 的 research_studies，默认游戏仍 v0.6.1。

新研究线程先读 [权威交接镜像](../../ideas/tidebound-research-handoff.md)，再取所需框架章节。首次只读之后，用户已授权制作 [借一束光 0.1.0 局部样片](../../ideas/tidebound-shore-study.md)：独立可操作入口，研究湿岩、灯鱼与共同光照；默认游戏仍为 v0.6.1，用户效果验收待定。

作者先读 [八张审阅卡](../../ideas/tidebound-human-review.md)：每次讨论一个主题，不必通读工程规范。八张卡的建议均获用户方向认可，后续直接按 D-10 执行；第 01 卡保留简单优先的疏朗取向。开放问题、具体造型和效果仍待样片，不再重复询问同一原则。

**当前规范：** [整体制作框架 1.1.0-draft.2](../../ideas/tidebound-framework/README.md)。先读角色阅读路线，再取本任务所需规则、对象卡和场景。[决策与待定项](../../ideas/tidebound-framework/12-DECISIONS.md) 记录最新用户选择；[现状与迁移](../../ideas/tidebound-framework/11-MIGRATION.md) 区分现有代码与目标契约。此更新只改文档，游戏运行版本仍为 v0.6.1。

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

离线行为、完整输入流程和画布画面已自查。该版本记录时浏览器工具在应用设置中关闭；后续独立样片检查范围见其报告，主版本仍未完成最终设备帧率、DOM 布局或真人无陪同试玩。自动控制器的约 82 秒模拟流程不等于真人时长。旧六章与广阔多海域仍不是本轮精修范围。

v0.6.1 修正水下鱼覆盖船体、实体灯前后排序与安置时叠灯架。锁鳞颌部有厚度和真实开口，眼齿随动；修复缝线读档后保留。初次提示不提前消失，后续停留十二秒恢复。像素回归含旧顺序负向对照；没有把离线检查写成浏览器或用户美术验收。

## 规范发布记录

[当前 framework-v1.1.0-draft.2 主本](https://github.com/Yihancheng0/tidebound-ascii/tree/framework-v1.1.0-draft.2/docs/framework) · 提交 398bd75b8d10f00aa05f1b7df1e6114428d98092。接收复核后统一参数 E 阶段期限与实现入口；交接 1.1.1，玩法方向与待验状态不变。


[首轮整合 framework-v1.1.0-draft.1 主本](https://github.com/Yihancheng0/tidebound-ascii/tree/framework-v1.1.0-draft.1/docs/framework) · 提交 11979c9a55feb6b6898a917acb155d36c4020f17。[护送整合说明](../../ideas/tidebound-gameplay-integration.md) 与交接 1.1 同版发布。60 条规则、25 场景、24 参数记录、7 待建立基准；新运行检查未执行。本次只更新规范，不包括已有未提交玩法小样。


[framework-v1.0.0-draft.1 历史主本](https://github.com/Yihancheng0/tidebound-ascii/tree/framework-v1.0.0-draft.1/docs/framework) · 提交 2809dfe17fe419304baa17b27fed86e461dbf91a。公共镜像为原创文档逐文件同步，详细状态见版本索引；运行版本仍为 v0.6.1。
