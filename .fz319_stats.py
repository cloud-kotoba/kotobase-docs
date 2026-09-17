import statistics
raw = open("/tmp/fz319.raw").read().strip().split("\n")
from collections import defaultdict
data = defaultdict(list)
for ln in raw:
    parts = ln.split()
    lab, idx, t, code = parts[0], int(parts[1]), float(parts[2]), parts[3]
    assert code == "200", ln
    data[lab].append(t)
cold_thr = 0.5
for lab in ["A","B","C","CTRL"]:
    v = data[lab]
    v.sort()
    cold = [x for x in v if x >= cold_thr]
    p50 = statistics.median(v)
    print(f"{lab} n={len(v)} cold={len(cold)} ({cold_thr:.1f}s) p50={p50*1000:.1f}ms max={max(v)*1000:.1f}ms cold_list={[round(x,4) for x in cold]}")
    print("   sorted:", [round(x*1000,1) for x in v])
total_search = data["A"]+data["B"]+data["C"]
cold_search = sum(1 for x in total_search if x>=cold_thr)
print(f"SEARCH total n={len(total_search)} cold={cold_search}/{len(total_search)} = {cold_search/len(total_search)*100:.1f}%")