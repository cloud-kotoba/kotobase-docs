import re, math

f = "_b93_run226_out.txt"
groups = {"A": [], "B": [], "C": [], "control": []}
for line in open(f):
    line = line.strip()
    if not line:
        continue
    m = re.match(r"run226([ABC])\s+(\d+)\s+([\d.]+)", line)
    if m:
        groups[m.group(1)].append(float(m.group(3)))
        continue
    m2 = re.match(r"control\s+(\d+)\s+([\d.]+)", line)
    if m2:
        groups["control"].append(float(m2.group(2)))

def stats(vals, label):
    sv = sorted(vals)
    n = len(sv)
    if n == 0:
        print(f"{label}: n=0")
        return
    k50 = math.ceil(0.50 * n)
    p50 = sv[k50-1]
    k95 = math.ceil(0.95 * n)
    p95 = sv[min(k95-1, n-1)]
    cold = [v for v in sv if v >= 0.5]
    warm = [v for v in sv if v < 0.5]
    wp50 = None
    if warm:
        wk = math.ceil(0.50 * len(warm))
        wp50 = sorted(warm)[wk-1]
        wmsg = f"warm_p50={wp50*1000:.1f}ms"
    else:
        wmsg = "warm_p50=n/a"
    print(f"{label}: n={n} cold(>=0.5s)={len(cold)}/{n} p50(all)={p50*1000:.1f}ms p95={p95*1000:.1f}ms min={sv[0]*1000:.1f} max={sv[-1]*1000:.1f} {wmsg}")
    for c in cold:
        print(f"    cold {c*1000:.1f}ms")

for k in ["A","B","C","control"]:
    stats(groups[k], f"run226{k}" if k != "control" else "control(signup)")

allc = [v for k in ["A","B","C"] for v in groups[k] if v >= 0.5]
allv = [v for k in ["A","B","C"] for v in groups[k]]
print(f"TOTAL 17時台 search 60試行: cold={len(allc)}/60 ({len(allc)/60*100:.1f}%)")
print(f"search 全60試行 p50(all)={(sorted(allv)[math.ceil(0.5*len(allv))-1])*1000:.1f}ms")