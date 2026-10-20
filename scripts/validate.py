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
    ideas=read('catalog/design-ideas.json')
    assert len({r['id'] for r in ideas})==len(ideas)
    assert not ({r['id'] for r in ideas}&({r['id'] for r in resources}|{p['id'] for p in pieces}))
    for r in ideas:
        assert r['kind']=='design_idea'
        assert r['status'] in ('candidate','user_proposed','approved_experiment','reference_note')
        assert (ROOT/r['document_path']).is_file()
        assert r['source_status']=='editorial_design_note'
        assert r['document_url'].startswith('https://github.com/Yihancheng0/ascii-game-library/blob/main/ideas/')
        assert r['license']['reuse']=='original_notes_only; third_party_works_reference_only'
    fish=read('catalog/fish-species.json');combos=read('catalog/fish-combinations.json');interactions=read('catalog/fish-interactions.json')
    fish_ids={f['id'] for f in fish};combo_ids={c['id'] for c in combos}
    assert len(fish)==60 and len(fish_ids)==len(fish)
    assert len({f['name'] for f in fish})==len(fish)
    assert [f['number'] for f in fish]==list(range(1,61))
    assert len(combos)==15 and len(combo_ids)==len(combos)
    assert len(interactions)==24
    for f in fish:
        assert f['kind']=='fish_design' and f['status']=='candidate'
        assert all(f.get(key) for key in ('ability','trigger','cost','counter','visual','scale'))
        assert set(f['combo_ids'])<=combo_ids
        assert f['combo_ids']==[c['id'] for c in combos if f['id'] in c['fish_ids']]
        assert f['interactions']==[r for r in interactions if f['id'] in r['fish_ids']]
    for c in combos:
        assert c['kind']=='fish_combo' and c['status']=='candidate'
        assert len(c['fish_ids'])==len(set(c['fish_ids']))==3
        assert set(c['fish_ids'])<=fish_ids
        assert c['fish_names']==[next(f['name'] for f in fish if f['id']==ident) for ident in c['fish_ids']]
        assert all(c.get(key) for key in ('sequence','result','failure','smallest_validation'))
    for r in interactions:
        assert len(r['fish_ids'])==len(set(r['fish_ids']))==2
        assert set(r['fish_ids'])<=fish_ids and r['relation'] and r['note']
    for r in fish+combos:
        assert r['source_status']=='editorial_design_note'
        assert r['license']['reuse']=='original_notes_only; third_party_works_reference_only'
        assert (ROOT/r['document_path']).is_file()
        anchor=r['document_url'].split('#')[1]
        assert f'id="{anchor}"' in (ROOT/r['document_path']).read_text(encoding='utf-8')
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
    print(f'OK: {len(resources)} resources, {len(pieces)} pieces, {mirrored} source modules, {len(ideas)} design notes, {len(fish)} fish, {len(combos)} triples, {len(interactions)} interactions; indexes, links and notices consistent.')
if __name__=='__main__':main()
