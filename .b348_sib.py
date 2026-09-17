#!/usr/bin/env python3
# read sibling run347 in-flight data for collision context
def load(path):
    rows=[]
    for line in open(path):
        p=line.split()
        rows.append((int(p[0]), float(p[1])))
    return rows

def report(tag, rows):
    times=sorted(t[1] for t in rows)
    cold=[t for t in times if t>=0.5]
    n=len(times); idx=max(1, round(0.5*n))
    p50=times[idx-1] if times else 0
    print(f"{tag}: n={n} cold={len(cold)} ({len(cold)}/{n}) p50={p50:.4f} max={times[-1] if times else 0:.4f}")

for f in [".b347_347A.txt",".b347_347B.txt",".b347_347C.txt",".b347_land.txt"]:
    report(f, load(f))
c=[]
for f in [".b347_347A.txt",".b347_347B.txt",".b347_347C.txt"]:
    c+=load(f)
report("COMBINED(A+B+C)", c)