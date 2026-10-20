# 开发场景配方

以下是本库整理的设计建议，不是对参考游戏实现方式的断言。

## 雨夜赛博朋克探索

分类：landscapes / cities / weather / retro

检索词：neon, rain, night, matrix

作品 / 工具：[cogmind](../resources/cogmind.md), [asciicker](../resources/asciicker.md)

先确定远景、地面、雨三层；让角色所在区域保持较低字符密度。

- [Neon Harbour Ferry](https://www.ascii-magic.com/ascii/harbour-neon-skyline) · `harbour-neon-skyline` · [源码](../vendor/ascii-magic-art/pieces/harbour-neon-skyline.js)

- [Neon City Rain](https://www.ascii-magic.com/ascii/neon-city-rain) · `neon-city-rain` · [源码](../vendor/ascii-magic-art/pieces/neon-city-rain.js)

- [Rainforest Falls Mist](https://www.ascii-magic.com/ascii/rainforest-falls-mist) · `rainforest-falls-mist` · [源码](../vendor/ascii-magic-art/pieces/rainforest-falls-mist.js)

- [Cliff Lighthouse Night](https://www.ascii-magic.com/ascii/cliff-lighthouse-night) · `cliff-lighthouse-night` · [源码](../vendor/ascii-magic-art/pieces/cliff-lighthouse-night.js)

- [City Skyline Night](https://www.ascii-magic.com/ascii/nyc-skyline-night) · `nyc-skyline-night` · [源码](../vendor/ascii-magic-art/pieces/nyc-skyline-night.js)

## 横版动作与 Boss

分类：animals / mascots / weather

检索词：fire, smoke, robot, dragon

作品 / 工具：[stone-story-rpg](../resources/stone-story-rpg.md), [ascii-patrol](../resources/ascii-patrol.md)

分别做待机、前摇、攻击、受击四个状态；角色轮廓和攻击方向要能快速读懂。

- [Campfire Under Stars](https://www.ascii-magic.com/ascii/campfire-under-stars) · `campfire-under-stars` · [源码](../vendor/ascii-magic-art/pieces/campfire-under-stars.js)

- [Campfire](https://www.ascii-magic.com/ascii/campfire) · `campfire` · [源码](../vendor/ascii-magic-art/pieces/campfire.js)

- [Rising Smoke](https://www.ascii-magic.com/ascii/fluid-smoke) · `fluid-smoke` · [源码](../vendor/ascii-magic-art/pieces/fluid-smoke.js)

- [Rising Smoke Rings](https://www.ascii-magic.com/ascii/smoke-rings) · `smoke-rings` · [源码](../vendor/ascii-magic-art/pieces/smoke-rings.js)

- [Drone Sign Crew](https://www.ascii-magic.com/ascii/robot-sign-crew) · `robot-sign-crew` · [源码](../vendor/ascii-magic-art/pieces/robot-sign-crew.js)

## 字符地牢与地图

分类：algorithms / screens / frames

检索词：maze, map, radar, dungeon

作品 / 工具：[brogue-ce](../resources/brogue-ce.md), [cogmind](../resources/cogmind.md)

先定义地形字符表、视野和物件优先级；环境动画避免覆盖可交互单位。

- [Maze Builder](https://www.ascii-magic.com/ascii/maze-builder) · `maze-builder` · [源码](../vendor/ascii-magic-art/pieces/maze-builder.js)

- [Maze Chase](https://www.ascii-magic.com/ascii/maze-chase) · `maze-chase` · [源码](../vendor/ascii-magic-art/pieces/maze-chase.js)

- [Autumn Pagoda Maples](https://www.ascii-magic.com/ascii/autumn-pagoda-maples) · `autumn-pagoda-maples` · [源码](../vendor/ascii-magic-art/pieces/autumn-pagoda-maples.js)

- [Heap Allocator Map](https://www.ascii-magic.com/ascii/heap-map) · `heap-map` · [源码](../vendor/ascii-magic-art/pieces/heap-map.js)

- [Radar Skill Profile](https://www.ascii-magic.com/ascii/radar-chart-morph) · `radar-chart-morph` · [源码](../vendor/ascii-magic-art/pieces/radar-chart-morph.js)

## 太空飞行与射击

分类：cosmos / demoscene / solids

检索词：star, space, tunnel, asteroid

作品 / 工具：[ascii-patrol](../resources/ascii-patrol.md), [donut-c](../resources/donut-c.md)

先用星场表达速度，再加入弹道与目标；保持背景、子弹、敌人三个亮度层次。

- [Campfire Under Stars](https://www.ascii-magic.com/ascii/campfire-under-stars) · `campfire-under-stars` · [源码](../vendor/ascii-magic-art/pieces/campfire-under-stars.js)

- [Starry Ridge](https://www.ascii-magic.com/ascii/starry-ridge) · `starry-ridge` · [源码](../vendor/ascii-magic-art/pieces/starry-ridge.js)

- [Hyperspace Jump](https://www.ascii-magic.com/ascii/hyperspace-jump) · `hyperspace-jump` · [源码](../vendor/ascii-magic-art/pieces/hyperspace-jump.js)

- [Vector Space Duel](https://www.ascii-magic.com/ascii/vector-space-duel) · `vector-space-duel` · [源码](../vendor/ascii-magic-art/pieces/vector-space-duel.js)

- [Texture Tunnel](https://www.ascii-magic.com/ascii/tunnel) · `tunnel` · [源码](../vendor/ascii-magic-art/pieces/tunnel.js)

## 标题、对话与转场

分类：lettering / empty-states / frames

检索词：typewriter, glitch, title, loader

作品 / 工具：[terminaltexteffects](../resources/terminaltexteffects.md), [candy-box-2](../resources/candy-box-2.md)

把动画时序和可交互状态分开；支持跳过、快速显示和减少动态效果。

- [Typewriter](https://www.ascii-magic.com/ascii/typewriter) · `typewriter` · [源码](../vendor/ascii-magic-art/pieces/typewriter.js)

- [Glitch Title Settle](https://www.ascii-magic.com/ascii/glitch-title-settle) · `glitch-title-settle` · [源码](../vendor/ascii-magic-art/pieces/glitch-title-settle.js)

- [Burning Title](https://www.ascii-magic.com/ascii/burning-title) · `burning-title` · [源码](../vendor/ascii-magic-art/pieces/burning-title.js)

- [Silent Film Title Card](https://www.ascii-magic.com/ascii/cinema-title-card) · `cinema-title-card` · [源码](../vendor/ascii-magic-art/pieces/cinema-title-card.js)

- [Progress Loader](https://www.ascii-magic.com/ascii/progress-loader) · `progress-loader` · [源码](../vendor/ascii-magic-art/pieces/progress-loader.js)

## 营地、经营与舒适场景

分类：landscapes / food / things / animals

检索词：campfire, garden, cat, food

作品 / 工具：[rexpaint](../resources/rexpaint.md), [ascii-splash](../resources/ascii-splash.md)

选择一个主要循环动作，配少量次要动态；先测小网格、少色板的可读性。

- [Campfire Under Stars](https://www.ascii-magic.com/ascii/campfire-under-stars) · `campfire-under-stars` · [源码](../vendor/ascii-magic-art/pieces/campfire-under-stars.js)

- [Campfire](https://www.ascii-magic.com/ascii/campfire) · `campfire` · [源码](../vendor/ascii-magic-art/pieces/campfire.js)

- [Scatter Plot](https://www.ascii-magic.com/ascii/scatter-plot) · `scatter-plot` · [源码](../vendor/ascii-magic-art/pieces/scatter-plot.js)

- [Primary Replica Sync](https://www.ascii-magic.com/ascii/db-replication) · `db-replication` · [源码](../vendor/ascii-magic-art/pieces/db-replication.js)
