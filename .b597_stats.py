import glob, statistics as st
out = []
for grp in ['A','B','C','landing']:
    p = f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b597/b597_{grp}.tsv"
    rows = []
    for line in open(p):
        parts = line.split()
        if len(parts) >= 3:
            rows.append((parts[0], float(parts[1]), float(parts[2])))
    tt = sorted(r[1] for r in rows)
    n = len(rows)
    codes = set(r[0] for r in rows)
    cold = sum(1 for r in rows if r[1] >= 0.5)
    p50 = tt[n//2]
    p95 = tt[int(n*0.95)] if n > 1 else tt[0]
    mx = tt[-1]
    out.append(f"{grp}: n={n} codes={sorted(codes)} cold(>=0.5s)={cold} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={mx*1000:.1f}ms")
print("\n".join(out))
