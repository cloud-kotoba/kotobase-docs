import sys
fn="query-cosientist.md"
lines=open(fn,encoding='utf-8').read().split('\n')
for i,l in enumerate(lines,start=1):
    if l.startswith('| K-Z3 |'):
        print("LINE=%d LEN=%d"%(i,len(l)))
        print("TAIL:", l[-1200:])
        print("HDRPART:", l[:160])
        break