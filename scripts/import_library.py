from pathlib import Path
import json, re, shutil, subprocess, html, hashlib
from collections import Counter
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT
UP = ROOT / 'work/ascii-magic-art'
DATE = '2026-10-20'
REPO = 'https://github.com/Yihancheng0/ascii-game-library'
RAW = 'https://raw.githubusercontent.com/Yihancheng0/ascii-game-library/main'
SHA = subprocess.check_output(['git','-C',str(UP),'rev-parse','HEAD'],text=True).strip()

def write(path, value):
    p=OUT/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(value,encoding='utf-8',newline='\n')
def dump(path, value): write(path,json.dumps(value,ensure_ascii=False,indent=2)+'\n')

CAT = {
 'landscapes':('场景与地形',['场景','背景','探索'],'关卡背景、营地、探索地图'),
 'screens':('界面与终端',['界面','UI','终端'],'游戏菜单、终端交互、任务面板'),
 'live-data':('数据与仪表',['数据','HUD','面板'],'属性面板、排行榜、战斗仪表'),
 'explainers':('流程与图解',['流程','教学','图解'],'教程、任务树、系统关系图'),
 'lettering':('标题与文字动画',['文字','标题','转场'],'标题、字幕、解密文字、片尾'),
 'solids':('三维形体',['三维','3D','旋转'],'道具展示、立体徽标、旋转拾取物'),
 'cosmos':('宇宙与星空',['太空','宇宙','星空'],'太空背景、星图、飞行场景'),
 'motion-lab':('运动与模拟',['运动','物理','粒子'],'弹道、波动、运动规律参考'),
 'weather':('天气与自然',['天气','自然','环境'],'雨雪、火焰、水面、植物动态'),
 'animals':('动物',['动物','生物','角色'],'生物外观、待机循环、生态场景'),
 'things':('物件',['物件','道具'],'交互物件、装置、道具图标'),
 'algorithms':('算法与生成',['算法','程序生成','数学'],'程序背景、分形、细胞自动机'),
 'demoscene':('演示场景与特效',['特效','背景','演示'],'技能背景、传送、火焰、隧道'),
 'arcade':('街机演示',['街机','玩法参考','自动演示'],'观察规则与节奏；自动播放动画不代表可操作游戏'),
 'frames':('边框与分隔',['边框','UI','界面'],'对话框、面板、界面分隔'),
 'occasions':('节庆与庆祝',['庆祝','节庆'],'通关、奖励、庆典'),
 'cities':('城市与建筑',['城市','建筑','场景'],'城市关卡、地标、环境气氛'),
 'mascots':('角色与吉祥物',['角色','吉祥物','待机'],'角色设计、待机、情绪表达'),
 'empty-states':('状态与反馈',['状态','反馈','界面'],'成功、失败、离线、加载反馈'),
 'retro':('复古计算机',['复古','终端','科幻'],'开机、黑客关卡、电脑交互'),
 'science':('科学与教学',['科学','教学','模拟'],'机制教学、科学题材、可视化'),
 'music':('音乐与声音',['音乐','声音','节奏'],'节奏游戏、音频可视化、乐器'),
 'food':('食物与饮料',['食物','饮料','道具'],'烹饪、商店、经营场景'),
 'india':('印度主题场景',['印度','文化','场景'],'地域题材环境与节庆气氛'),
}
WORDS = {
 'rain':['雨','下雨','雨夜'], 'snow':['雪','下雪'], 'fire':['火','火焰'],
 'smoke':['烟','烟雾'], 'spark':['火花'], 'explosion':['爆炸'], 'firework':['烟花'],
 'neon':['霓虹','赛博朋克'], 'hacker':['黑客','赛博朋克'], 'matrix':['数字雨','黑客'],
 'night':['夜晚','夜景'], 'forest':['森林'], 'tree':['树木'], 'mountain':['山','山脉'],
 'ocean':['海洋'], 'sea':['海','海洋'], 'water':['水'], 'river':['河流'], 'wave':['波浪'],
 'desert':['沙漠'], 'castle':['城堡'], 'dungeon':['地牢'], 'cave':['洞穴'],
 'space':['太空'], 'star':['星星','星空'], 'galaxy':['星系'], 'planet':['行星'],
 'robot':['机器人'], 'cat':['猫'], 'dog':['狗'], 'dragon':['龙'], 'ghost':['幽灵'],
 'coin':['金币','拾取物'], 'heart':['爱心','生命'], 'sword':['剑','武器'],
 'portal':['传送门'], 'tunnel':['隧道'], 'plasma':['等离子'], 'particle':['粒子'],
 'load':['加载'], 'spinner':['加载'], 'progress':['进度'], 'success':['成功'],
 'error':['错误','失败'], 'glitch':['故障','闪烁'], 'typewriter':['打字机','对话'],
 'text':['文字'], 'title':['标题'], 'credit':['片尾'], 'boot':['开机'],
 'maze':['迷宫'], 'snake':['贪吃蛇'], 'pong':['乒乓'], 'tetris':['俄罗斯方块'],
 'breakout':['打砖块'], 'invader':['太空入侵者'], 'chess':['象棋'],
 'sand':['沙','沙粒'], 'waterfall':['瀑布'], 'campfire':['篝火','营地'],
 'lightning':['闪电'], 'aurora':['极光'], 'sunset':['日落'], 'moon':['月亮'],
 'lava':['熔岩'], 'volcano':['火山'], 'city':['城市'], 'village':['村庄'],
 'train':['火车'], 'ship':['船'], 'fish':['鱼'], 'bird':['鸟'], 'butterfly':['蝴蝶'],
 'flower':['花'], 'garden':['花园'], 'wind':['风'], 'cloud':['云'],
 'rotate':['旋转'], 'cube':['立方体'], 'torus':['圆环','甜甜圈'], 'sphere':['球体'],
 'battle':['战斗'], 'laser':['激光'], 'radar':['雷达'], 'map':['地图'], 'inventory':['背包'],
}

def resource(id,name,kind,url,summary,tags,study,source=None,demo=None,license_id='unknown',license_url=None,reuse='reference_only',tech=None):
    return dict(id=id,name=name,kind=kind,url=url,source_url=source,demo_url=demo,
                summary_zh=summary,tags=tags,study_points=study,technology=tech or [],
                reuse=reuse,license=dict(id=license_id,evidence_url=license_url,
                scope='上游代码/素材的具体适用范围以原始授权文件为准；这里的分类不是授权替代品。'),
                checked_on=DATE,verification='official_page_or_repository_read; interaction_not_tested')

RES = [
resource('stone-story-rpg','Stone Story RPG','game','https://stonestoryrpg.com/','横版 ASCII RPG，以角色、怪物与场景动画为重点的作品参考。',['角色','怪物','Boss','横版','逐帧动画','RPG'],['轮廓在动作中的可读性','攻击前摇与命中反馈','背景与角色的字符密度分配'],demo='https://stonestoryrpg.com/',tech=['Unity','C#'],license_url='https://stonestoryrpg.com/faq.html'),
resource('ascii-patrol','ASCII Patrol','game','https://ascii-patrol.com/','受 Moon Patrol 启发的字符横版街机游戏，提供浏览器版本和 C++ 源码。',['横版','动作','射击','跳跃','滚屏','街机'],['滚屏速度与角色定位','跳跃、障碍、弹道的可读性','素材编辑到代码的工作流'],source='https://github.com/msokalski/ascii-patrol',demo='https://ascii-patrol.com/area53/ascii-patrol-html5.html',license_id='GPL-3.0 (repository reported)',license_url='https://github.com/msokalski/ascii-patrol/blob/master/LICENSE',reuse='copyleft_review_required',tech=['C++','Emscripten','REXPaint']),
resource('cogmind','Cogmind','game','https://www.gridsagegames.com/cogmind/','科幻机器人 Roguelike，适合借鉴终端界面、粒子效果和高密度战斗反馈。',['科幻','机器人','地牢','Roguelike','UI','粒子','战斗'],['信息层级与操作反馈','粒子如何引导注意力','爆炸与可破坏环境的表达'],demo='https://www.gridsagegames.com/cogmind/'),
resource('brogue-ce','Brogue CE','game','https://github.com/tmewett/BrogueCE','开源地牢 Roguelike，可作为字符地图、地形和视野系统的实现参考。',['地牢','地图','视野','Roguelike','探索'],['用颜色和字符区分地形','地图生成与视野系统','字符与图块表现之间的切换'],source='https://github.com/tmewett/BrogueCE',license_id='AGPL-3.0 (repository reported)',license_url='https://github.com/tmewett/BrogueCE/blob/master/LICENSE.txt',reuse='copyleft_review_required',tech=['C','SDL2']),
resource('candy-box-2','Candy Box 2','game','https://candybox2.github.io/','浏览器文字与 ASCII 探索游戏，可研究逐步展开的玩法和场景组织。',['文字','探索','增量','RPG','界面','浏览器'],['从极简界面逐步引入系统','文本、场景和操作的组织','低素材成本的探索体验'],source='https://github.com/candybox2/candybox2.github.io',demo='https://candybox2.github.io/',license_id='GPL-3.0-or-later (JavaScript code notice)',license_url='https://github.com/candybox2/candybox2.github.io/blob/master/candybox2_sourceCodeLicense.txt',reuse='copyleft_review_required',tech=['TypeScript','JavaScript']),
resource('asciicker','Asciicker','game','https://asciicker.com/','浏览器三维字符世界演示，适合研究镜头、空间和地形表现。',['三维','3D','探索','地形','镜头'],['镜头运动时的字符稳定性','地形遮挡与角色辨识','立体空间的明暗和配色'],demo='https://asciicker.com/y9/'),
resource('asciiart-animations','ASCII Art Archive · Animations','animation_collection','https://www.asciiart.eu/animations','可直接在网页查看火焰、星空、隧道、数字雨等字符动画。',['特效','火焰','星空','数字雨','隧道','天气'],['比较不同字符密度','环境循环与特效参数','寻找同一题材的视觉变体'],demo='https://www.asciiart.eu/animations',license_url='https://www.asciiart.eu/animations'),
resource('terminaltexteffects','TerminalTextEffects','animation_engine','https://github.com/ChrisBuilds/terminaltexteffects','Python 终端字符特效引擎，支持运动路径、颜色变化和场景动画。',['文字','标题','转场','粒子','路径','终端'],['文字聚合和消散','运动轨迹与缓动','动画和状态事件的组织'],source='https://github.com/ChrisBuilds/terminaltexteffects',license_id='MIT',license_url='https://github.com/ChrisBuilds/terminaltexteffects/blob/main/LICENSE',reuse='permissive_with_notice',tech=['Python','ANSI']),
resource('donut-c','donut.c / Donut math','technical_demo','https://www.a1k0n.net/2011/07/20/donut-math.html','作者提供旋转字符圆环的动画、代码和数学推导。',['三维','3D','明暗','投影','圆环','甜甜圈'],['透视投影','深度缓冲与遮挡','表面亮度映射到字符'],demo='https://www.a1k0n.net/2011/07/20/donut-math.html',tech=['C','JavaScript']),
resource('ascii-splash','ascii-splash','animation_engine','https://github.com/reowens/ascii-splash','TypeScript 终端动画项目，含波浪、粒子和自然场景等程序动画。',['背景','天气','粒子','波浪','终端','程序生成'],['动画模式与预设组织','色板复用','动态背景的参数化'],source='https://github.com/reowens/ascii-splash',license_id='MIT',license_url='https://github.com/reowens/ascii-splash/blob/main/LICENSE',reuse='permissive_with_notice',tech=['TypeScript','Node.js']),
resource('rexpaint','REXPaint','authoring_tool','https://www.gridsagegames.com/rexpaint/','免费的 Windows 字符画编辑器，支持图层、前景色、背景色和多种导出。',['编辑器','素材制作','图层','地图','UI','角色'],['先在网格中绘制角色和界面','调色板与图层规划','导出到游戏资源流程'],license_id='freeware; source/art reuse not implied',license_url='https://www.gridsagegames.com/rexpaint/'),
resource('ascii-magic','ASCII Magic Art Library','asset_library','https://www.ascii-magic.com/ascii','大型字符动画库，提供单项 ES 模块、网页播放器和终端播放工具。',['素材库','场景','角色','特效','UI','三维','程序生成'],['直接按主题检索单项动画','通过 draw(t) 生成时间驱动的帧','将装饰动画与游戏逻辑分离'],source='https://github.com/kailashsr38/ascii-magic-art',demo='https://www.ascii-magic.com/ascii',license_id='MIT; two photo data exceptions',license_url='https://github.com/kailashsr38/ascii-magic-art/blob/'+SHA+'/NOTICE',reuse='per_item_license',tech=['JavaScript','ES modules','Canvas','Node.js']),
]

def parse_meta(text):
    match=re.search(r'export const meta\s*=\s*\{([\s\S]*?)\};',text)
    if not match: raise ValueError('Unrecognized metadata block')
    block=match.group(1); data={}
    for key in ('slug','name','category','note','cell'):
        m=re.search(r'\b'+key+r'"?\s*:\s*("(?:\\.|[^"\\])*")',block)
        if m:data[key]=json.loads(m.group(1))
    m=re.search(r'\btags"?\s*:\s*(\[[^\]]*\])',block)
    data['tags']=json.loads(m.group(1)) if m else []
    for key in ('cols','rows','fps'):
        m=re.search(r'\b'+key+r'"?\s*:\s*(\d+|[A-Z]+)',block)
        value=m.group(1) if m else ''
        if value and not value.isdigit():
            const=re.search(r'\b'+value+r'\s*=\s*(\d+)',text)
            value=const.group(1) if const else ''
        data[key]=int(value) if value else None
    for key in ('slug','name','category','note','cols','rows','fps'):
        if key not in data or data[key] is None:raise ValueError('Missing '+key)
    return data

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    for folder in ('pieces','lib','runtime','bin'):
        shutil.copytree(UP/folder,OUT/'vendor/ascii-magic-art'/folder,dirs_exist_ok=True)
    for fn in ('categories.json','package.json','LICENSE','NOTICE','README.md'):
        shutil.copy2(UP/fn,OUT/'vendor/ascii-magic-art'/fn)
    hashes={}
    for p in sorted((OUT/'vendor/ascii-magic-art').rglob('*')):
        if p.is_file() and p.name!='UPSTREAM.md':
            relative=p.relative_to(OUT/'vendor/ascii-magic-art').as_posix()
            assert p.read_bytes()==(UP/relative).read_bytes(),relative
            hashes[p.relative_to(OUT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    dump('catalog/provenance.json',dict(upstream_commit=SHA,algorithm='sha256',files=hashes))
    write('vendor/ascii-magic-art/UPSTREAM.md',f'# Upstream snapshot\n\nSource: https://github.com/kailashsr38/ascii-magic-art\n\nCommit: `{SHA}`\n\nCollected: {DATE}\n\n634 piece modules and required runtime/toolkit files copied unchanged. This is a source snapshot, not a claim to authorship. See LICENSE and NOTICE. The website listed 734 entries at collection; the other 100 are indexed but not vendored.\n')
    metas={}
    for p in sorted((UP/'pieces').glob('*.js')):
        m=parse_meta(p.read_text(encoding='utf-8'));assert m['slug']==p.stem
        metas[p.stem]=m
    source_html=(ROOT/'work/ascii-magic-library.html').read_text(encoding='utf-8')
    cards=[]
    for match in re.finditer(r'<a\b([^>]*\bclass="ap-card"[^>]*)>([\s\S]*?)</a>',source_html):
        attrs=dict((k,html.unescape(v)) for k,v in re.findall(r'([\w-]+)="([^"]*)"',match.group(1)))
        name=re.search(r'class="ap-card__name">([^<]+)',match.group(2))
        cards.append(dict(slug=attrs['data-slug'],name=html.unescape(name.group(1)),category=attrs['data-cat'],search_text=attrs.get('data-hay','')))
    assert len(cards)==len({x['slug'] for x in cards})==734
    assert set(metas)<=set(x['slug'] for x in cards)
    pieces=[]
    for c in cards:
        slug=c['slug'];m=metas.get(slug);cat=c['category'];cn,tags,uses=CAT[cat]
        hay=(c['search_text']+' '+slug).lower()
        aliases=set(tags)
        for en,zh in WORDS.items():
            if re.search(r'(?<![a-z])'+en+r'[a-z]*(?![a-z])',hay):aliases.update(zh)
        is_photo=slug in ('ocean-sunset','starry-ridge')
        pieces.append(dict(
            id='ascii-magic:'+slug,slug=slug,name=c['name'],provider='ascii-magic',
            category=cat,category_zh=cn,description=m['note'] if m else None,
            tags=m['tags'] if m else [],aliases_zh=sorted(aliases),
            search_text=c['search_text'],suggested_game_uses_zh=uses,
            annotation_origin='category and keyword rules; suggestions are editorial, not tested gameplay',
            preview_url='https://www.ascii-magic.com/ascii/'+slug,
            source_status='vendored_at_pinned_commit' if m else 'website_only_not_in_pinned_repository',
            source_url='https://raw.githubusercontent.com/kailashsr38/ascii-magic-art/'+SHA+'/pieces/'+slug+'.js' if m else None,
            website_source_candidate_url=None if m else 'https://www.ascii-magic.com/ascii/pieces/'+slug+'.js',
            website_source_candidate_verified=False if not m else None,
            local_source_path='vendor/ascii-magic-art/pieces/'+slug+'.js' if m else None,
            raw_source_url=RAW+'/vendor/ascii-magic-art/pieces/'+slug+'.js' if m else None,
            cols=m['cols'] if m else None,rows=m['rows'] if m else None,fps=m['fps'] if m else None,
            cell=m.get('cell') if m else None,
            license=dict(id='MIT code; Unsplash photo data' if is_photo else 'MIT',
                evidence_url='https://github.com/kailashsr38/ascii-magic-art/blob/'+SHA+('/NOTICE' if is_photo else '/LICENSE'),
                evidence_basis='pinned_repository_notice' if m else 'website_library_docs_claim; per-file not checked',
                reuse='review_photo_notice' if is_photo else 'preserve_MIT_notice'),
            checked_on=DATE,source_commit=SHA if m else None))
    categories=json.loads((UP/'categories.json').read_text(encoding='utf-8'))
    counts=Counter(p['category'] for p in pieces)
    for c in categories:
        c.update(name_zh=CAT[c['id']][0],game_uses_zh=CAT[c['id']][2],count=counts[c['id']],
                 index_path='catalog/ascii-magic/'+c['id']+'.json')
        dump('catalog/ascii-magic/'+c['id']+'.json',[p for p in pieces if p['category']==c['id']])
        human=[f"# {c['name_zh']} / {c['name']}",f"{c['count']} 项。开发用途建议：{c['game_uses_zh']}。",f"[机器索引](../../{c['index_path']}) · [全部分类](../../README.md)"]
        for p in pieces:
            if p['category']!=c['id']:continue
            src=f"[源码](../../{p['local_source_path']})" if p['local_source_path'] else '仅网页索引；本快照未收集源码'
            human.extend([f"## {p['name']} · `{p['slug']}`",f"[原始预览]({p['preview_url']}) · {src}",p['description'] or '此条来自网站目录；详细参数尚未从固定版本源码确认。',f"关键词：{' / '.join(p['aliases_zh'])}。授权记录：{p['license']['id']}。"])
        write('docs/categories/'+c['id']+'.md','\n\n'.join(human)+'\n')
    meta=dict(schema_version='1.0.0',updated_on=DATE,repository=REPO,resource_count=len(RES),
              piece_count=len(pieces),vendored_piece_count=len(metas),website_only_piece_count=len(pieces)-len(metas),
              upstream_commit=SHA,upstream_repository='https://github.com/kailashsr38/ascii-magic-art',
              source_observation='Website has 734 entries; pinned repository contains 634 piece files. No source files invented for missing entries.')
    dump('catalog/resources.json',RES);dump('catalog/ascii-magic.json',pieces);dump('catalog/categories.json',categories)
    dump('catalog/manifest.json',meta)
    write('catalog/ascii-magic.jsonl',''.join(json.dumps(p,ensure_ascii=False)+'\n' for p in pieces))
    dump('catalog/catalog.json',dict(metadata=meta,resources=RES,pieces=pieces,categories=categories))
    write('THIRD_PARTY_NOTICES.md','# Third-party notices\n\nASCII Magic source files and source metadata are from ASCII Magic, Copyright (c) 2026 ASCII Magic. They are reproduced under the MIT license in [vendor/ascii-magic-art/LICENSE](vendor/ascii-magic-art/LICENSE).\n\nThe image data in ocean-sunset.js and starry-ridge.js remains under its original photo license; see [NOTICE](vendor/ascii-magic-art/NOTICE).\n\nOther games and websites are linked and described for reference. Their code, art, names and screenshots have not been relicensed by this catalog. The MIT license at the root covers original catalog tooling and editorial text only, not third-party works.\n')
    write('LICENSE',(UP/'LICENSE').read_text(encoding='utf-8').replace('2026 ASCII Magic (ascii-magic.com)','2026 Yihancheng0 (original catalog text and tooling only; third-party works excluded)'))
    write('.gitignore','__pycache__/\n*.pyc\n.DS_Store\nwork/\n')
    write('.gitattributes','* text eol=lf\n')
    write('README.md',readme(meta,categories))
    write('START_HERE.md',start_here())
    write('AGENTS.md',agents())
    write('docs/recipes.md',recipes(pieces))
    write('docs/data-model.md',data_model())
    write('docs/maintenance.md',maintenance())
    write('docs/reuse-guide.md',reuse_guide())
    write('llms.txt',f'''# ASCII 游戏素材与灵感库 / ASCII Game Library
> 中文开发参考、双语标签、可读源码、逐项授权来源。Updated: {DATE}.

- [Start here]({RAW}/START_HERE.md): AI retrieval procedure and examples.
- [Resource catalog]({RAW}/catalog/resources.json): 12 games, tools, libraries and collections.
- [Category index]({RAW}/catalog/categories.json): 24 categories; fetch one shard after choosing a category.
- [Manifest]({RAW}/catalog/manifest.json): source revision and coverage.
- [All animation metadata]({RAW}/catalog/ascii-magic.json): 734 entries; prefer category shards to save context.
- [Full combined JSON]({RAW}/catalog/catalog.json): all machine-readable metadata.
- [Text digest]({RAW}/llms-full.txt): compact one-line-per-piece text index.
- [Recipes]({RAW}/docs/recipes.md): game-oriented search routes and design prompts.
- [Reuse]({RAW}/docs/reuse-guide.md): distinguish inspiration, code and reusable art.
- [Source snapshot]({REPO}/tree/main/vendor/ascii-magic-art): 634 pinned modules, runtime and toolkit with notices.
''')
    digest=['# ASCII Game Library — complete text digest',f'Updated: {DATE}; repository: {REPO}',f'734 indexed pieces; 634 vendored; upstream commit: {SHA}',
            'Source and license status are available in JSON. Source snapshot is optional game art/code reference, not a game engine.', '\n## Resources']
    for r in RES:digest.append(f"{r['id']} | {r['name']} | {r['kind']} | {r['summary_zh']} | {r['url']} | reuse={r['reuse']} | tags={','.join(r['tags'])}")
    digest.append('\n## ASCII Magic pieces')
    for p in pieces:digest.append(f"{p['slug']} | {p['name']} | {p['category_zh']} | {','.join(p['aliases_zh'])} | {p['description'] or 'Website-indexed; metadata not in pinned source'} | {p['preview_url']} | source={p['source_status']} | license={p['license']['id']}")
    write('llms-full.txt','\n'.join(digest)+'\n')
    for r in RES:
        text=[f"# {r['name']}",r['summary_zh'],f"类型：{r['kind']} · 标签：{', '.join(r['tags'])}", '\n## 入口']
        for k in ('url','source_url','demo_url'):
            if r[k]:text.append(f"- {k}: {r[k]}")
        text+=['\n## 可研究的问题']+['- '+s for s in r['study_points']]
        text+=['\n## 复用状态',f"`{r['reuse']}` · `{r['license']['id']}`",r['license']['evidence_url'] or '没有确认可复用授权，作为作品参考。',
               f"\n检查日期：{DATE}。已读取官方网页/仓库；没有在本次整理中实际试玩所有游戏。"]
        write('resources/'+r['id']+'.md','\n\n'.join(text)+'\n')
    write('scripts/search.py',SEARCH)
    write('scripts/validate.py',VALIDATE)
    importer=Path(__file__).read_text(encoding='utf-8').replace("OUT = ROOT",'OUT = ROOT')
    write('scripts/import_library.py',importer)
    print(json.dumps(meta,ensure_ascii=False))

def readme(meta,categories):
    lines=[
 '# ASCII 游戏素材与灵感库',
 '> 面向 AI 辅助游戏开发：按中文需求查参考、按英文 slug 取源码。',
 f'收录 **12 个资源入口、734 项 ASCII Magic 动画、24 个分类**；附 **634 项动画的源码快照**。核对日期：{DATE}。',
 f'**AI 固定入口：[{RAW}/llms.txt]({RAW}/llms.txt)**',
 '把下面这段发给未来的开发 AI：',
 f'```text\n请先读取 {RAW}/START_HERE.md\n这是我的 ASCII 游戏素材与灵感库。先按需求检索，再选 3–5 个参考，\n列出原始链接、可借鉴点、源码位置和授权状态。需要实现时读取对应源文件，\n只把来源已确认的可复用代码或素材纳入项目。\n```',
 '## 如何使用',
 '- 浏览入口：[资源卡片](resources/) · [游戏开发场景配方](docs/recipes.md) · [AI 检索说明](START_HERE.md)。',
 '- AI 按需读取：[分类目录](catalog/categories.json) → `catalog/ascii-magic/<分类>.json` → 对应源文件。',
 '- 程序读取：[总 JSON](catalog/catalog.json) · [动画 JSONL](catalog/ascii-magic.jsonl) · [紧凑全文索引](llms-full.txt)。',
 '- 克隆后本地搜索（Python 3.10+，仅标准库）：',
 '```sh\ngit clone https://github.com/Yihancheng0/ascii-game-library.git\ncd ascii-game-library\npython scripts/search.py 雨夜 霓虹 --limit 8\npython scripts/search.py 火焰 --source-only --json\npython scripts/search.py --category mascots --limit 8\npython scripts/search.py --kind game\npython scripts/validate.py\n```',
 '关键词默认按 OR 排序；使用 `--all` 要求每个输入词都命中；`--source-only` 只返回本地有源码快照的动画。中文词由分类与关键词规则补充，不是逐项人工翻译。',
 '## 游戏、工具与合集',
 '| 资源 | 用途 | 复用状态 |\n|---|---|---|']
    for r in RES:lines.append(f"| [{r['name']}](resources/{r['id']}.md) | {r['summary_zh']} | `{r['reuse']}` |")
    lines+=['## ASCII Magic 分类','| 分类 | 条目 | 开发用途 |\n|---|---:|---|']
    for c in categories:lines.append(f"| [{c['name_zh']} / {c['name']}](docs/categories/{c['id']}.md) | {c['count']} | {c['game_uses_zh']} |")
    lines+=['## 快照与边界',
            f'- 上游固定提交：`{SHA}`。网站 734 项，仓库 634 项；100 项仅有网页索引，字段明确标识。',
            '- 源码在 `vendor/ascii-magic-art/`，保留原始 LICENSE / NOTICE；两项照片数据有单独说明。',
            '- Arcade 分类是自动播放的小游戏演示；不能把它们直接视为有输入、碰撞、存档的完整游戏。',
            '- 作品参考与可复用代码分开记录；其他作品的美术没有被本库重新授权。',
            '- [更新方法](docs/maintenance.md) · [数据字段](docs/data-model.md) · [复用说明](docs/reuse-guide.md)。',
            '- 这是有日期的整理快照；不包含定时抓取或自动更新任务。']
    result='\n\n'.join(lines)+'\n'
    while re.search(r'(?m)(\|[^\n]*\|)\n\n(?=\|)',result):
        result=re.sub(r'(?m)(\|[^\n]*\|)\n\n(?=\|)',r'\1\n',result)
    return result

def start_here():return f'''# 给开发 AI 的入口

固定入口：{RAW}/llms.txt
仓库：{REPO}

1. 确认需求：玩法参考 / 背景 / 角色 / 技能特效 / 标题转场 / UI / 3D。
2. 先读 `{RAW}/catalog/resources.json` 和 `{RAW}/catalog/categories.json`。
3. 只取相关分片，例如 `{RAW}/catalog/ascii-magic/weather.json`；避免一开始载入全部源码或总 JSON。
4. 用 `name`、`tags`、`aliases_zh`、`description`、`search_text` 搜索；中文需求同时匹配英文近义词。标签来自规则，有误差。
5. 从 3–5 项候选给出：preview_url、想借鉴的点、source_status、license 与修改方案。
6. 对 `vendored_at_pinned_commit`，可直接读 `raw_source_url`；也可克隆后读 `local_source_path`。保留源码所引用的 lib/runtime 和授权声明。
7. `website_only_not_in_pinned_repository` 表示尚未收集该项源码；`website_source_candidate_url` 未验证，不能声称它一定可用。先打开网页再决定是否另行取源。
8. `reference_only` 项目用于研究表现与设计；不要把链接当成可复制美术的授权。
9. 字符模块生成的是 `draw(t)` 帧。要做游戏，需要另外设计输入、角色状态、地图、碰撞、胜负与存档；自动播放的 Arcade 动画不等于完整玩法。
10. 优先按项目需求选普通 ASCII 或 Unicode 字符集，核对字体、字符单元比例、色板和刷新性能；查看模块 `meta` 里的实际参数。

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
'''

def agents():return '''# Working with this library

Read START_HERE.md first. catalog/ is UTF-8 JSON and Markdown is bilingual where useful.
Prefer category shards over the full catalog. Keep stable IDs and original source URLs.
Distinguish reference_only / copyleft_review_required / permissive_with_notice / per_item_license.
The 634 vendored ASCII Magic modules are unchanged upstream source; preserve LICENSE and NOTICE.
Do not treat automatically playing Arcade animations as interactive games.
Do not invent source links or dimensions for the 100 website-only entries.
Editorial tags and game uses are suggestions, not verified original author claims.
Run python scripts/validate.py after catalog edits. See docs/maintenance.md for import and rebuild.
This repository contains no private user data or credentials; do not add any.
'''

def recipes(pieces):
    recipes=[
        ('雨夜赛博朋克探索','landscapes / cities / weather / retro',['neon','rain','night','matrix'],['cogmind','asciicker'],'先确定远景、地面、雨三层；让角色所在区域保持较低字符密度。'),
        ('横版动作与 Boss','animals / mascots / weather',['fire','smoke','robot','dragon'],['stone-story-rpg','ascii-patrol'],'分别做待机、前摇、攻击、受击四个状态；角色轮廓和攻击方向要能快速读懂。'),
        ('字符地牢与地图','algorithms / screens / frames',['maze','map','radar','dungeon'],['brogue-ce','cogmind'],'先定义地形字符表、视野和物件优先级；环境动画避免覆盖可交互单位。'),
        ('太空飞行与射击','cosmos / demoscene / solids',['star','space','tunnel','asteroid'],['ascii-patrol','donut-c'],'先用星场表达速度，再加入弹道与目标；保持背景、子弹、敌人三个亮度层次。'),
        ('标题、对话与转场','lettering / empty-states / frames',['typewriter','glitch','title','loader'],['terminaltexteffects','candy-box-2'],'把动画时序和可交互状态分开；支持跳过、快速显示和减少动态效果。'),
        ('营地、经营与舒适场景','landscapes / food / things / animals',['campfire','garden','cat','food'],['rexpaint','ascii-splash'],'选择一个主要循环动作，配少量次要动态；先测小网格、少色板的可读性。'),
    ]
    lines=['# 开发场景配方','以下是本库整理的设计建议，不是对参考游戏实现方式的断言。']
    for title,cats,keywords,refs,advice in recipes:
        matches=[]
        for key in keywords:
            hits=[p for p in pieces if key in p['slug'] and p['local_source_path']]
            for p in hits[:2]:
                if p not in matches:matches.append(p)
        lines += ['## '+title,'分类：'+cats,'检索词：'+', '.join(keywords),'作品 / 工具：'+', '.join(f'[{r}](../resources/{r}.md)' for r in refs),advice]
        for p in matches[:5]:lines.append(f"- [{p['name']}]({p['preview_url']}) · `{p['slug']}` · [源码](../{p['local_source_path']})")
    return '\n\n'.join(lines)+'\n'

def data_model():return '''# 数据字段与文件约定

全部文本 UTF-8；日期用 YYYY-MM-DD；schema_version 为 1.0.0。

| 文件 | 内容 |
|---|---|
| catalog/manifest.json | 数量、日期、固定上游提交 |
| catalog/resources.json | 12 个作品/工具/合集入口 |
| catalog/categories.json | 分类 ID、中文用途、分片路径 |
| catalog/ascii-magic.json | 全部单项元数据 |
| catalog/ascii-magic/<category>.json | 一类动画；与总索引中的记录完全相同 |
| catalog/ascii-magic.jsonl | 每行一个单项，适合流式读取与导入检索工具 |
| catalog/catalog.json | 上述元数据的组合视图 |
| resources/<id>.md | 资源卡片 |
| vendor/ascii-magic-art/ | 634 个固定版本源码、依赖工具和声明 |

单项稳定 ID 为 `ascii-magic:<slug>`。`preview_url` 是原始网页；`raw_source_url` 是本库可直接读的源码链接；`source_url` 指向上游固定提交；`local_source_path` 是仓库相对路径。三个 source 字段对未收集源码的条目为 null，不能把空值视为可用源码。

`source_status` 为 `vendored_at_pinned_commit` 或 `website_only_not_in_pinned_repository`。后者的 `website_source_candidate_url` 是按官方播放器的路径规则生成的候选值，**尚未请求验证**。

`cols`、`rows`、`fps` 来自源码 meta；没有确认的数据用 null。`cell` 未声明时为 null，不推断它是正方形或矩形。

`description` / `tags` 为上游元数据；`search_text` 来自公开网站检索属性；`aliases_zh` 与 `suggested_game_uses_zh` 是本库按分类和关键词生成的建议。中文检索不是完整语义搜索，可同时给英文同义词。

`license.id`、`license.evidence_url`、`license.evidence_basis` 记录观察到的授权和证据。作品级代码授权不自动覆盖所有外部图片、音乐、商标等。

资源类型 kind：game / animation_collection / animation_engine / technical_demo / authoring_tool / asset_library。

资源复用状态 reuse：reference_only（作品参考）；copyleft_review_required（需按上游 copyleft 授权处理代码）；permissive_with_notice（保留声明）；per_item_license（看每项记录）。这些字段是检索辅助，不替代原始许可。
'''

def maintenance():return f'''# 更新与维护

这份库是 {DATE} 的快照。网站 734 条、上游源码 634 条的差异已保留。

## 日常使用

1. 手动向 catalog/resources.json 添加资源时，保留原始链接、用途、核对日期和授权证据。
2. 更完整的再导入应使用仓库中的 `scripts/import_library.py`，它重新生成 JSON、分片、卡片与文档。修改生成内容前优先修改导入器，避免下次覆盖。
3. 导入器最上方的 ROOT / UP / OUT 可通过脚本所在位置推导；在本仓库运行时，克隆上游到 `work/ascii-magic-art`，保存网页到 `work/ascii-magic-library.html`。
4. `work/` 已被 .gitignore 排除；导入前核对 Git 差异，尤其关注上游新 LICENSE / NOTICE、新增依赖和源文件数量。脚本包含 734 条的网站断言，新版数量变化时需人工核对并更新断言和说明。
5. 运行 `python scripts/import_library.py`，再运行 `python scripts/validate.py`；检查中文与英文搜索结果，再提交并 push。
6. 本版导入器对首次快照直接使用已核对的资源说明；更新后应同步 checked_on 和来源证据，不能只改日期。

## 拉取资料（示例）

```sh
git -c core.autocrlf=false clone --depth 1 https://github.com/kailashsr38/ascii-magic-art.git work/ascii-magic-art
python -c "import urllib.request,pathlib; pathlib.Path('work/ascii-magic-library.html').write_bytes(urllib.request.urlopen('https://www.ascii-magic.com/ascii',timeout=45).read())"
python scripts/import_library.py
python scripts/validate.py
```

源码快照固定到提交 {SHA}。后续导入的源文件与当前版本可能不同，应以各次提交的 manifest 和差异为准。生成器不会自动删除旧 vendor 文件；如果上游删除或更名，更新时需明确处理旧文件并核对数量。

暂无定时任务、远程执行、账号令牌或依赖安装步骤。通过 Python 标准库可离线检索；播放源码需 Node.js 或浏览器。
'''

def reuse_guide():return '''# 复用与出处

本库提供两类价值：研究作品的视觉与交互设计，以及在授权明确时读取/修改上游代码。每项记录均附来源。

- ASCII Magic：保留复制源码中的 MIT 声明。`ocean-sunset` 和 `starry-ridge` 的照片数据仍有原始照片许可，先看 vendor/ascii-magic-art/NOTICE。本库镜像保留原始声明。
- TerminalTextEffects、ascii-splash：仓库标示 MIT；实际引入文件时仍核对相关声明和依赖。
- ASCII Patrol、Brogue CE、Candy Box 2：记录各仓库或文件的 GPL / AGPL 证据；引用代码时需按实际许可处理。不要把“开源”当成没有条件。
- Stone Story RPG、Cogmind、Asciicker、donut.c 网页：本次没有确认能用于复制其美术或源码的完整授权，先作为作品或技术参考。
- ASCII Art Archive：站点聚集不同作者作品；查看、学习并不自动取得每件美术的复用许可。
- REXPaint：免费编辑工具；工具免费与第三方素材授权是不同信息。

根目录 MIT 仅涵盖本库原创的整理文本和工具，不改变被链接作品或镜像文件的授权。
'''

SEARCH = r'''"""Search local ASCII reference metadata. Python 3.10+, standard library only."""
import argparse, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query',nargs='*',help='Chinese or English keywords; OR by default')
    parser.add_argument('--category',help='ASCII Magic category ID, e.g. weather / mascots')
    parser.add_argument('--kind',help='Resource kind, or piece for animations')
    parser.add_argument('--source-only',action='store_true',help='Only locally vendored animation modules')
    parser.add_argument('--all',action='store_true',help='Require every query token')
    parser.add_argument('--limit',type=int,default=10)
    parser.add_argument('--json',action='store_true',help='Print full matching records as JSON')
    args=parser.parse_args()
    if args.limit<1:parser.error('--limit must be positive')
    categories=json.loads((ROOT/'catalog/categories.json').read_text(encoding='utf-8'))
    if args.category and args.category not in {c['id'] for c in categories}:
        parser.error('Unknown category; read catalog/categories.json')
    records=json.loads((ROOT/'catalog/resources.json').read_text(encoding='utf-8'))
    records+=json.loads((ROOT/'catalog/ascii-magic.json').read_text(encoding='utf-8'))
    terms=[s.casefold() for q in args.query for s in q.split() if s]
    found=[]
    for record in records:
        is_piece='slug' in record
        if args.category and (not is_piece or record['category']!=args.category):continue
        if args.kind and ('piece' if is_piece else record['kind'])!=args.kind:continue
        if args.source_only and not record.get('local_source_path'):continue
        fields=[record.get(k) for k in ('name','slug','summary_zh','description','tags','aliases_zh','search_text','study_points','category_zh','technology')]
        hay=json.dumps(fields,ensure_ascii=False).casefold()
        hits=[t in hay for t in terms]
        if terms and not (all(hits) if args.all else any(hits)):continue
        score=sum(10+5*(t in record.get('slug',''))+5*(t in record['name'].casefold()) for t,h in zip(terms,hits) if h)
        found.append((score,record))
    found.sort(key=lambda item:(-item[0],item[1].get('slug',item[1]['id'])))
    selected=[r for _,r in found[:args.limit]]
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    if args.json:print(json.dumps({'total_matches':len(found),'results':selected},ensure_ascii=False,indent=2))
    else:
        print(f'{len(found)} matches; showing {len(selected)}')
        for r in selected:
            print(f"\n{r['id']} | {r['name']}")
            print(r.get('description') or r.get('summary_zh') or r.get('search_text'))
            print('Preview:',r.get('preview_url') or r['url'])
            print('Source:',r.get('local_source_path') or r.get('source_url') or 'not collected / reference only')
            print('License:',r['license']['id'])
    return 0

if __name__=='__main__':raise SystemExit(main())
'''

VALIDATE=r'''"""Validate cross-file catalog integrity and mirrored source provenance."""
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
    resources=read('catalog/resources.json');pieces=read('catalog/ascii-magic.json')
    manifest=read('catalog/manifest.json');categories=read('catalog/categories.json')
    assert len(resources)==manifest['resource_count']
    assert len(pieces)==manifest['piece_count']
    assert len({p['id'] for p in pieces})==len(pieces)
    assert len({p['slug'] for p in pieces})==len(pieces)
    assert len({r['id'] for r in resources})==len(resources)
    assert {p['category'] for p in pieces}=={c['id'] for c in categories}
    shards=[]
    for c in categories:
        shard=read(c['index_path']); assert len(shard)==c['count']
        assert shard==[p for p in pieces if p['category']==c['id']]
        shards+=shard
    assert sorted(p['id'] for p in shards)==sorted(p['id'] for p in pieces)
    assert [json.loads(line) for line in (ROOT/'catalog/ascii-magic.jsonl').read_text(encoding='utf-8').splitlines()]==pieces
    combined=read('catalog/catalog.json')
    assert combined==dict(metadata=manifest,resources=resources,pieces=pieces,categories=categories)
    mirrored=0
    for p in pieces:
        assert p['preview_url'].startswith('https://www.ascii-magic.com/ascii/')
        if p['local_source_path']:
            mirrored+=1;source=ROOT/p['local_source_path'];assert source.is_file()
            assert p['source_commit']==manifest['upstream_commit']
            assert p['source_status']=='vendored_at_pinned_commit'
            assert p['cols']>0 and p['rows']>0 and p['fps']>0
            text=source.read_text(encoding='utf-8')
            assert re.search(r'slug"?\s*:\s*"'+re.escape(p['slug'])+'"',text)
        else:
            assert p['source_url'] is None and p['raw_source_url'] is None
            assert p['source_status']=='website_only_not_in_pinned_repository'
            assert p['cols'] is None and p['fps'] is None
    assert mirrored==manifest['vendored_piece_count']
    assert len(pieces)-mirrored==manifest['website_only_piece_count']
    assert len(list((ROOT/'vendor/ascii-magic-art/pieces').glob('*.js')))==mirrored
    for r in resources:assert (ROOT/'resources'/f"{r['id']}.md").is_file()
    notice=(ROOT/'vendor/ascii-magic-art/NOTICE').read_text(encoding='utf-8')
    provenance=read('catalog/provenance.json')
    assert provenance['upstream_commit']==manifest['upstream_commit']
    for path,digest in provenance['files'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
    for slug in ('ocean-sunset','starry-ridge'):
        assert slug in notice
        assert next(p for p in pieces if p['slug']==slug)['license']['reuse']=='review_photo_notice'
    for md in ROOT.rglob('*.md'):
        if 'vendor' in md.parts:continue
        for target in re.findall(r'\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):continue
            assert (md.parent/target.split('#')[0]).exists(),(md,target)
    print(f'OK: {len(resources)} resources, {len(pieces)} pieces, {len(categories)} categories, {mirrored} source modules; JSON, shards, links and notices consistent.')
if __name__=='__main__':main()
'''

if __name__=='__main__':build()
