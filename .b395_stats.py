#!/usr/bin/env python3
import json

COLD = 0.5
N = 20

def load(fn):
    rows = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            try:
                ttfb = float(parts[0])
                code = int(parts[1])
            except ValueError:
                continue
            rows.append((ttfb, code))
    return rows

def nearest_rank_p50(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return None
    rank = int(-(-50 * n / 100.0))  # ceil(0.5*n)
    rank = max(1, min(rank, n))
    v = s[rank - 1]
    return None if v is None else round(v, 4)

def stats(rows):
    ttfb = [r[0] for r in rows]
    codes = [r[1] for r in rows]
    colds = [t for t in ttfb if t >= COLD]
    warm = [t for t in ttfb if t < COLD]
    return {
        "n": len(ttfb),
        "all200": all(c == 200 for c in codes),
        "non200": sum(1 for c in codes if c != 200),
        "cold": len(colds),
        "cold_vals": [round(t, 4) for t in colds],
        "p50": nearest_rank_p50(ttfb),
        "warm_p50": nearest_rank_p50(warm),
        "max": round(max(ttfb), 4) if ttfb else None,
        "min": round(min(ttfb), 4) if ttfb else None,
    }

result = {}
for label in ["A", "B", "C", "land"]:
    fn = f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b395_395{label}.txt"
    result[label] = stats(load(fn))

with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b395_stats_out.txt", "w") as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps(result, indent=2, ensure_ascii=False))