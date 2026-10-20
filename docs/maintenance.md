# 更新与维护

这份库是 2026-10-20 的快照。网站 734 条、上游源码 634 条的差异已保留。

## 日常使用

1. 手动向 catalog/resources.json 添加资源时，保留原始链接、用途、核对日期和授权证据。
2. 更完整的再导入应使用仓库中的 `scripts/import_library.py`，它重新生成 JSON、分片、卡片与文档。修改生成内容前优先修改导入器，避免下次覆盖。
3. 导入器最上方的 ROOT / UP / OUT 可通过脚本所在位置推导；在本仓库运行时，克隆上游到 `work/ascii-magic-art`，保存网页到 `work/ascii-magic-library.html`。
4. `work/` 已被 .gitignore 排除；导入前核对 Git 差异，尤其关注上游新 LICENSE / NOTICE、新增依赖和源文件数量。脚本包含 734 条的网站断言，新版数量变化时需人工核对并更新断言和说明。
5. 运行 `python scripts/import_library.py`，再运行 `python scripts/validate.py`；检查中文与英文搜索结果，再提交并 push。
6. 本版导入器对首次快照直接使用已核对的资源说明；更新后应同步 checked_on 和来源证据，不能只改日期。

## 拉取资料（示例）

```sh
git clone --depth 1 https://github.com/kailashsr38/ascii-magic-art.git work/ascii-magic-art
python -c "import urllib.request,pathlib; pathlib.Path('work/ascii-magic-library.html').write_bytes(urllib.request.urlopen('https://www.ascii-magic.com/ascii',timeout=45).read())"
python scripts/import_library.py
python scripts/validate.py
```

源码快照固定到提交 de88962156057cbef583bd265bf55e23d6c5e30d。后续导入的源文件与当前版本可能不同，应以各次提交的 manifest 和差异为准。生成器不会自动删除旧 vendor 文件；如果上游删除或更名，更新时需明确处理旧文件并核对数量。

暂无定时任务、远程执行、账号令牌或依赖安装步骤。通过 Python 标准库可离线检索；播放源码需 Node.js 或浏览器。
