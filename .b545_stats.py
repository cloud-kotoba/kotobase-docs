#!/usr/bin/env python3
import re
DIR="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
labels=[("A",".b545_run545_A.ttfb"),("B",".b545_run545_B.ttfb"),("C",".b545_run545_C.ttfb"),("land",".b545_run545_landing.ttfb")]
tot_n=tot_200=tot_cold=0
allt=[]
for lbl,fn in labels:
    rows=[]
    for line in open(f"{DIR}/{fn}"):
        m=re.match(r"^(\d+) (\d+) ([0-9.]+)$", line.strip())
        if m: rows.append((m.group(2), float(m.group(3))))
    n=len(rows); ok=sum(1 for c,_ in rows if c=="200")
    ts=[t for _,t in rows]
    cold=[t for c,t in rows if c=="200" and t>=0.5]
    ts.sort()
    p50=ts[len(ts)//2] if ts else 0
    mx=max(ts) if ts else 0
    if lbl!="land":
        tot_n+=n; tot_200+=ok; tot_cold+=len(cold); allt+=ts
        print(f"{lbl}: n={n} 200={ok} cold>=0.5s={len(cold)} ({', '.join(f'{t:.4f}' for t in cold)}) p50={p50:.4f} max={mx:.4f}")
    else:
        coldl=[t for c,t in rows if c=="200" and t>=0.5]
        print(f"land: n={n} 200={ok} cold>=0.5s={len(coldl)} p50={p50:.4f} max={mx:.4f}")
allt.sort()
print(f"TOTAL search: n={tot_n} 200={tot_200} cold={tot_cold} ({100.0*tot_cold/tot_n:.1f}%) p50={allt[len(allt)//2]:.4f} max={allt[-1]:.4f}")
