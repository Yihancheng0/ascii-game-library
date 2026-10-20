# 借潮而行 · 美术与动作约束

## 先保留什么

保留原鱼的字符轮廓、低明度银灰体积、稀疏彩色微光、尾部水迹和负空间。新增对象采用同一类稳定字符采样，不能把鱼放进更亮、更密的装饰背景里。世界只在一次短暂揭示时让尺度压过小船；常态依然安静。

## 五条制作规则

1. 一个场景只突出一件事：初潮湾的灯，沉船的银丝，帆海的薄鳍，夜市的暖窗，雨岛的水线。
2. 先画可识别的形，再转字符。灯鱼有透明腹腔、内灯、眼睛、胸鳍和柔尾；针尾鱼是细长身体与尾丝；纱鳍鱼有不对称长膜；回声鱼腹腔宽、鳃褶清楚。
3. 器官解释能力。禁止以全屏粒子替代能力的可读性。针尾鱼的进度表现为接上的银线，回声表现为低密度环纹，呼吸表现为水线与鳃口的周期。
4. 大岛用连续空间、远近遮挡、几段可以走到的目的地建立尺度。常态镜头不一次摆出全岛。码头、小屋、断桥、石盆、池塘和南侧鳃沟必须能在世界中定位。
5. 安置的鱼不能一直表演。待机只保留摆鳍和呼吸，天气与玩家的动作再触发变化。暖色集中在少数窗口和灯器官，绿植保持灰绿。

## 动作修正

伏礁鱼的头部前三节保持低弯折，各节长度恒定，中后段逐渐放松。转弯速率受限，急转时降低推进速度。嘴眼跟随实际第一段脊线；嘴采用贴在头部的短弧线，不再以黑色矩形切割颈部。测试覆盖持续反转时的长度、关节角和面部朝向。

## 呼吸与天气

岛背、树木和建筑缓慢同步起伏，海岸浅滩出现相应涨落水线。鳃湾的实际交互有可等待的吸气窗口。雷雨只在对应剧情阶段出现；扫光缓慢经过雨线，闪电只短暂增加局部亮度，不使用全屏纯白爆闪。J 旅记可关闭闪光，保留雨与扫光。

## 素材适配来源

| 预览 | 固定源码 | 借鉴及修改 | 状态 |
|---|---|---|---|
| [Lighthouse Storm](https://www.ascii-magic.com/ascii/lighthouse-storm) | [lighthouse-storm.js](https://github.com/kailashsr38/ascii-magic-art/blob/de88962156057cbef583bd265bf55e23d6c5e30d/pieces/lighthouse-storm.js) | 扫光中雨线更清楚；改为初潮岛石灯标、慢扫、稀疏点线与暖灰光 | 固定版本有源码，MIT |
| [Lightning Storm](https://www.ascii-magic.com/ascii/lightning-storm) | [lightning-storm.js](https://github.com/kailashsr38/ascii-magic-art/blob/de88962156057cbef583bd265bf55e23d6c5e30d/pieces/lightning-storm.js) | 确定性折线和分枝；改成低频、低亮度、局部水面反光 | 固定版本有源码，MIT |
| [Lighthouse Lamp Room](https://www.ascii-magic.com/ascii/lighthouse-beam) | [lighthouse-beam.js](https://github.com/kailashsr38/ascii-magic-art/blob/de88962156057cbef583bd265bf55e23d6c5e30d/pieces/lighthouse-beam.js) | 光束侧向展开和距离衰减；改为俯视世界空间连续扫光 | 固定版本有源码，MIT |
| [Rain Shower](https://www.ascii-magic.com/ascii/rain-shower) | [rain-shower.js](https://github.com/kailashsr38/ascii-magic-art/blob/de88962156057cbef583bd265bf55e23d6c5e30d/pieces/rain-shower.js) | 分层雨速、落水点；改为更少的银青雨线，与家园雨水石盆关联 | 固定版本有源码，MIT |

授权全文见 `licenses/ASCII-Magic-MIT.txt`。网页截图只用于识别参考，实际依据是素材库固定源码及 LICENSE/NOTICE。
