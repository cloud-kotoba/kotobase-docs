import statistics, sys
raw = open(sys.argv[1]).read().strip().split("\n")
from collections import defaultdict
data = defaultdict(list)
cur = None
for ln in raw:
    if ln.startswith("==="):
        cur = ln.strip("= ").strip()
        continue
    parts = ln.split()
    if len(parts) < 3:
        continue
    idx, t, code = int(parts[0]), float(parts[1]), parts[2]
    if code != "200":
        print(f"NON200 {cur} {ln}")
        continue
    data[cur].append(t)
cold_thr = 0.5
labels = ["run326A", "run326B", "run326C", "control-signup"]
for lab in labels:
    if lab not in data:
        print(lab, "MISSING")
        continue
    v = data[lab]
    v.sort()
    cold = [x for x in v if x >= cold_thr]
    p50 = statistics.median(v)
    print(f"{lab} n={len(v)} cold={len(cold)} p50={p50*1000:.1f}ms max={max(v)*1000:.1f}ms cold_list={[round(x,4) for x in cold]}")
    print("   sorted:", [round(x*1000,1) for x in v])
search = data["run326A"]+data["run326B"]+data["run326C"]
cs = sum(1 for x in search if x>=cold_thr)
print(f"SEARCH total n={len(search)} cold={cs}/{len(search)} = {cs/len(search)*100:.1f}%")