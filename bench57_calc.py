import sys
f='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench57_run167_out.txt'
sections={}
cur=None
for l in open(f):
    l=l.strip()
    if l.startswith('==='):
        cur=l.strip('= ').strip()
        sections[cur]=[]
    elif cur and l and not l.startswith('Sat') and not l.startswith('20:'):
        parts=l.split()
        sections[cur].append((parts[0], int(parts[1]), float(parts[2]), parts[3]))
for name, rows in sections.items():
    vals=[r[2] for r in rows]
    codes=set(r[3] for r in rows)
    s=sorted(vals); n=len(s)
    p50=s[(n-1)//2]
    cold=[(i+1,v) for i,v in enumerate(vals) if v>=0.5]
    colds=' '.join(f"{i}:{v:.3f}s" for i,v in cold) or 'none'
    print(f"{name}: n={n} codes={codes} cold(>=0.5s) {len(cold)}/{n} [{colds}] p50={p50:.3f}s min={min(vals):.3f} max={max(vals):.3f}")
