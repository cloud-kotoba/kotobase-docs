#!/usr/bin/env python3
import csv, datetime

def parse(f):
    vals, codes = [], []
    with open(f) as fh:
        for r in csv.reader(fh):
            if len(r) != 2:
                continue
            code, t = r[1].split()
            codes.append(code)
            vals.append(float(t))
    return vals, codes

for grp in ["A", "B", "C", "CTL"]:
    f = f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b633_{grp}.csv"
    vals, codes = parse(f)
    n = len(vals)
    cold = [v for v in vals if v >= 0.5]
    s = sorted(vals)
    p50 = s[n // 2] * 1000
    p95 = s[max(0, int(n * 0.95) - 1)] * 1000
    print(f"{grp}: n={n} codes={'/'.join(sorted(set(codes)))} cold={len(cold)}/{n} "
          f"cold_ms={[round(v*1000,1) for v in cold]} p50={p50:.1f}ms p95={p95:.1f}ms max={max(vals)*1000:.1f}ms")

tot = cnt = 0
for grp in ["A", "B", "C"]:
    vals, _ = parse(f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b633_{grp}.csv")
    cnt += len(vals)
    tot += sum(1 for v in vals if v >= 0.5)
print(f"SEARCH_TOTAL: cold {tot}/{cnt} = {tot/cnt*100:.1f}%")
print("stats_done", datetime.datetime.now().isoformat())
