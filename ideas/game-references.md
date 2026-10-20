# 作品启发对照 / Game reference notes

日期：2026-10-20。下列借鉴点是本项目的设计判断，不是原作者对创作过程的陈述。

## 用户点名的七款游戏

| 作品与官方资料 | 对本项目的启发 | 适合先做的小验证 |
|---|---|---|
| [泰拉瑞亚 Terraria](https://www.terraria.org/support) | 探索、收获和新能力相互推动；物品有后续用途 | 一种鱼带来新航行能力，让旧海域出现新路线 |
| [饥荒 Don't Starve](https://www.klei.com/games/dont-starve/) | 环境、生物与资源的关系产生事件；《海难》是群岛方向的参考 | 灯吸引小鱼，小鱼引来捕食者，玩家利用这条关系 |
| [重生细胞 Dead Cells](https://deadcells.com/) | 装备带来不同操作；动作、节奏与反馈清楚 | 验证一种轻快操作与一种有重量的操作，暂不铺大量装备 |
| [GRIS](https://www.devolverdigital.com/games/gris) | 色彩、构图、音乐、留白和动作共同组织情绪 | 一片海域的统一色板，一次有明确节奏的巨鱼揭示 |
| [空洞骑士 Hollow Knight](https://www.hollowknight.com/) | 区域身份、连接、阻隔、重访与秘密 | 先看到进不去的海洞，获得能力后从另一岸穿出 |
| [武士零 Katana ZERO](https://www.devolverdigital.com/games/katana-zero) | 少数动作在经过设计的情境中产生密集决策，时间变化加强表现 | 把一段巨鱼搏斗做成观察—诱导—避障—收线的短过程 |
| [小小梦魇2 Little Nightmares II](https://www.bandainamcoent.com/games/little-nightmares-2) | 尺度、遮挡和信息不完整带来震撼；原作使用三维场景 | 巨影、局部鱼鳍、缓慢移动的岛轮廓，分阶段揭示全貌 |

上述作品在本库均作为 `reference_only` 的设计研究，不表示取得源码、美术、音乐或角色的复制授权。

## 渔力全开 How to Fish

[官方页面](https://store.steampowered.com/app/4001890/How_to_Fish/?l=schinese)。用户最初称“鱼力全开”，作为检索别名保留。

官方介绍包含物理交互、钓鱼卖鱼、装备、首领、岛屿和多人合作。对本项目的启发是用熟悉入口建立预期，再以一条可反复产生后果的规则改变预期。没有找到作者对最初创意过程的直接说明，不把推测写成作者事实。状态：`reference_only`。

## 前序参考

| 参考 | 借鉴点 | 源码与授权状态 |
|---|---|---|
| [Sea of Stars 星之海](https://sabotagestudio.com/presskits/sea-of-stars/) / [钓鱼说明](https://playdigious.helpshift.com/hc/en/37-sea-of-stars/faq/732-how-to-fish/) | 安静水面、明暗岸线、方向控制的钓鱼 | 完整作品 `reference_only` |
| [Eastward 风来之国](https://chucklefish.org/blog/eastward-winter-development-update/) | 聚落空间关系、疏密、建筑身份与生活痕迹 | `reference_only` |
| [Spiritfarer](https://thunderlotusgames.com/games/spiritfarer/) | 人物姿态、船上生活、捕鱼与烹饪照顾的联系 | `reference_only` |
| [Fishing Paradiso](https://store.steampowered.com/app/1781030/) | 捕鱼推动新环境、人物与故事目标 | `reference_only` |
| [Necesse](https://store.steampowered.com/app/1169040/) | 二维持续生成世界、生态区、聚落与探索 | `reference_only`；无限世界仍需要有意义的地点 |
| [DREDGE](https://www.dredge.game/) | 鱼获用途、远航、返港与船升级 | 原作三维，借鉴循环与表现；`reference_only` |
| [Swaggerfall](https://holonaut64.itch.io/swaggerfall) | 统一尺度、模型到字符、镜头、光照、帆船与世界交互 | 可访问网页与运行包不等于源码或美术可复用授权；`reference_only` |
| [ascii-sharks](https://github.com/stackedlol/ascii-sharks)（当前工程底层参考） | 连续游动、银光、尾迹、留白、干净界面 | 已核对仓库入口；当前工程记录基于提交 `c521e24a787e6d4cc460d4cf2b9815f25e4fe453`。本轮未确认明确的复用许可，实际复用需核对原始声明 |

## 本轮选出的三段可读源码动画

| 素材 / 预览 | 本项目用途 | 源码 |
|---|---|---|
| [Cliff Lighthouse Night](https://www.ascii-magic.com/ascii/cliff-lighthouse-night) | 夜海分层、稳定地形与局部扫光 | [cliff-lighthouse-night.js](../vendor/ascii-magic-art/pieces/cliff-lighthouse-night.js) |
| [Stilt Village Sunset](https://www.ascii-magic.com/ascii/stilt-village-sunset) | 渔村、船体、撑船、尾流与炊烟 | [stilt-village-sunset.js](../vendor/ascii-magic-art/pieces/stilt-village-sunset.js) |
| [Koi Pond Ripples](https://www.ascii-magic.com/ascii/koi-pond-ripples) | 俯视鱼、荷叶遮挡、涟漪与层次 | [koi-pond-ripples.js](../vendor/ascii-magic-art/pieces/koi-pond-ripples.js) |

三项均是 `vendored_at_pinned_commit`；授权以 [LICENSE](../vendor/ascii-magic-art/LICENSE) 和 [NOTICE](../vendor/ascii-magic-art/NOTICE) 为准。前两项采用 192×108 方形单元、点阵式表现，鱼塘采用 92×34 字符网格。需要适配字符比例与色板，固定画幅动画不直接等于可移动游戏世界。

另两项作品参考：[Stone Story RPG](https://stonestoryrpg.com/) 用于人物与装备动作，`reference_only`；[Candy Box 2](https://candybox2.github.io/) 用于逐步展开的资源与探索，[代码](https://github.com/candybox2/candybox2.github.io/tree/master/code/main) 为 GPL-3.0-or-later，[字符美术](https://candybox2.github.io/ascii_art.html) 单独采用 CC BY-SA 3.0。
