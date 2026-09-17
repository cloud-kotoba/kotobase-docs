#!/usr/bin/env python3
import sys
for fn in sys.argv[1:]:
    print("===", fn)
    i=0
    for line in open(fn):
        i+=1
        p=line.split()
        if len(p)<2: continue
        try: c=int(p[0]); t=float(p[1])
        except ValueError: continue
        if t>=0.4:
            print(f"  pos={i} code={c} ttfb={t:.4f}")