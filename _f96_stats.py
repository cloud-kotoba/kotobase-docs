import re

f = "_f96_run225_out.txt"
groups = {"A": [], "B": [], "C": [], "control": []}
for line in open(f):
    line = line.strip()
    m = re.match(r"(run225[ABC]|control)\s+(\d+)\s+([\d.]+)", line)
    if m:
        k = m.group(1).replace("run225", "")
        if k == "control":
            k = "control"
        groups[k].append(float(m.group(3)))

def stats(vals, label):
    vals = sorted(vals)
    n = len(vals)
    med = vals[n//2] if n % 2 else (vals[n//2-1]+vals[n//2])/2.0
    p95 = vals[min(n-1, int(0.95*n))]
    cold = [v for v in vals if v >= 0.5]
    print(f"{label}: n={n} cold={len(cold)} p50={med*1000:.1f}ms p95={p95*1000:.1f}ms min={vals[0]*1000:.1f} max={vals[-1]*1000:.1f}")
    for v in sorted(vals):
        if v >= 0.5:
            print(f"    cold {v*1000:.1f}ms")

for k in ["A","B","C","control"]:
    stats(groups[k], f"run225{k}")

allc = [v for k in ["A","B","C"] for v in groups[k] if v >= 0.5]
print(f"TOTAL 16時台 search 60 試行: cold={len(allc)}/60")