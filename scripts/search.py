"""Search local ASCII reference metadata. Python 3.10+, standard library only."""
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
