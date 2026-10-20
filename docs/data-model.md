# 数据字段与文件约定

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
