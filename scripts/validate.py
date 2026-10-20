"""Validate cross-file catalog integrity and mirrored source provenance."""
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
