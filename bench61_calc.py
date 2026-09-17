import math

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench61_run175_out.txt"
cold = 0
runs = {}
for line in open(p):
    parts = line.split()
    if len(parts) >= 4 and parts[0].startswith("175") and parts[0] != "175A" or (len(parts) >= 4 and parts[0][:4] in ("175A", "175B", "175C")):
        tag, i, t, code = parts[0], parts[1], float(parts[2]), parts[3]
        runs.setdefault(tag, []).append((t, int(code)))
for tag, vals in sorted(runs.items()):
    times = sorted(t for t, c in vals)
    codes = [c for t, c in vals]
    n = len(times)
    p50 = times[math.ceil(0.50 * n) - 1]
    p95 = times[math.ceil(0.95 * n) - 1]
    mx = max(t for t, c in vals if t < 0.5) if any(t < 0.5 for t, c in vals) else None
    ncold = sum(1 for t, c in vals if t >= 0.5)
    print(f"{tag}: n={n} all200={all(c==200 for c in codes)} cold={ncold} p50={p50:.3f}s p95={p95:.3f}s max_excl_cold={mx if mx is None else round(mx,3)}")
total = sum(len(v) for v in runs.values())
tcold = sum(1 for v in runs.values() for t, c in v if t >= 0.5)
print(f"TOTAL cold {tcold}/{total}")
# 23時台通算: 本 tick が 23時台初計測なら run175 のみ
