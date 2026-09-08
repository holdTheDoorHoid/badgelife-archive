#!/usr/bin/env python3
"""After a research workflow run: merge reported duplicates, save other-item finds, relocate corrected
entries, validate, regenerate event pages and titles, and print the next batch of ids.
  post_batch.py <run_dir> [--next 60]
"""
import json,glob,os,re,subprocess,sys,collections
ROOT='/home/hoid/Desktop/badgelife-archive'; os.chdir(ROOT)
OUT=os.environ.get('NEXT_BATCH_FILE', os.path.join(ROOT,'data','next_batch.txt'))
D=sys.argv[1]; N=int(sys.argv[sys.argv.index('--next')+1]) if '--next' in sys.argv else 60
res={}
for line in open(D+'/journal.jsonl'):
    j=json.loads(line)
    r=j.get('result')
    if j.get('type')=='result' and isinstance(r,dict) and 'status' in r and r.get('id'): res[r['id']]=r
st=collections.Counter(r['status'] for r in res.values())
print('results:',len(res),dict(st))
batch=set(res)
# other items
others=[o for r in res.values() for o in (r.get('other_items_found') or []) if o.get('title')]
p='data/research_others.json'; old=json.load(open(p)) if os.path.exists(p) else []
seen={(o.get('title','').lower(),o.get('url','')) for o in old}
new=[o for o in others if (o.get('title','').lower(),o.get('url',''))not in seen]
json.dump(old+new,open(p,'w'),indent=1); print('others saved:',len(new),'total',len(old)+len(new))
ALL=glob.glob('_badges/*/*.md')
def find(eid):
    r=subprocess.run(['grep','-rlx',f'id: {eid}','_badges'],capture_output=True,text=True).stdout.split()
    if r: return r[0], eid
    c=[f for f in ALL if os.path.exists(f) and eid.endswith('-'+os.path.basename(f)[:-3])]
    if len(c)==1:
        m=re.search(r'^id: (.+)$',open(c[0]).read(),re.M); return c[0], m.group(1).strip()
    return None,None
done=set(); merged=0
for a,r in res.items():
    b=r.get('duplicate_of')
    if not b or a in done or b in done: continue
    fa,ia=find(a); fb,ib=find(b)
    if not fa or not fb or fa==fb: print('SKIP pair:',a,b,fa,fb); continue
    if b in batch: keep,drop=(ia,ib) if os.path.getsize(fa)>=os.path.getsize(fb) else (ib,ia)
    else: keep,drop=ib,ia
    out=subprocess.run(['python3','scripts/merge_entries.py',keep,drop],capture_output=True,text=True)
    print('MERGE keep',keep,'drop',drop,'->',(out.stdout+out.stderr).strip()[-100:]); merged+=1
    done.add(a); done.add(b)
for cmd in (['python3','scripts/relocate_entries.py'],['python3','scripts/build_index.py','--check'],['python3','scripts/gen_event_pages.py']):
    out=subprocess.run(cmd,capture_output=True,text=True); print(cmd[1].split('/')[-1]+':',(out.stdout+out.stderr).strip().splitlines()[-1] if (out.stdout+out.stderr).strip() else '')
import yaml
rows=[]
for f in glob.glob('_badges/*/*.md'):
    m=re.match(r'^---\n(.*?)\n---',open(f,encoding='utf-8').read(),re.S); fm=yaml.safe_load(m.group(1)) or {}
    mk=', '.join((x.get('name') or '') for x in (fm.get('makers') or []) if isinstance(x,dict))
    rows.append(f"{fm.get('id')} | {fm.get('title')} | {mk}")
open('data/existing_titles.txt','w').write('\n'.join(sorted(rows))+'\n'); print('titles',len(rows),'merged',merged)
print(subprocess.run(['python3','scripts/research_queue.py','--summary'],capture_output=True,text=True).stdout.strip())
ids=subprocess.run(['python3','scripts/research_queue.py','--next',str(N)],capture_output=True,text=True).stdout.split()
open(OUT,'w').write(' '.join(ids))
print('NEXT', len(ids)); print(' '.join(ids))
