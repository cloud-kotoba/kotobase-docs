import re
from statistics import median

def load(name, lines):
    vals=[]
    for ln in lines:
        if ln.startswith(name+' '):
            parts=ln.split()
            vals.append(float(parts[2]))
    return vals

with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f115_run252_out.txt') as f:
    lines=[l.rstrip('\n') for l in f]

def report(prefix):
    vals=load(prefix, lines)
    cold=[v for v in vals if v>=0.5]
    warm=[v for v in vals if v<0.5]
    print(f"{prefix} n={len(vals)} cold(>=0.5)={len(cold)} p50={median(vals):.4f}s "
          f"warm_p50={median(warm):.4f}s max={max(vals):.4f}s"
          + (f" cold_vals={[round(c,4) for c in cold]}" if cold else ""))
    return len(cold)

cA=report('run252A')
cB=report('run252B')
cC=report('run252C')
cCtl=report('control')
tot=cA+cB+cC
print(f"TOTAL search cold = {tot}/60 ({tot/60*100:.1f}%) | control cold = {cCtl}/20")