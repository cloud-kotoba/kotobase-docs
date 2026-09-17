import json

def load(p):
    rows = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            code = parts[0]
            ttfb = float(parts[1])
            rows.append((code, ttfb))
    return rows

def stats(rows):
    ts = sorted(t for c, t in rows)
    n = len(ts)
    codes = [c for c, t in rows]
    cold = [(c, t) for c, t in rows if t >= 0.5]
    out = {
        "n": n,
        "codes_200": codes.count("200"),
        "p50": round(ts[n // 2] * 1000, 1) if n else None,
        "p95": round(ts[int(n * 0.95) - 1] * 1000, 1) if n >= 20 else None,
        "max_s": round(ts[-1], 4) if n else None,
        "cold_ge_0.5s": len(cold),
        "cold_list": [round(t, 4) for c, t in cold],
    }
    return out

res = {}
for s in ["A", "B", "C"]:
    rows = load(".b573_%s.ttfb" % s)
    res["run573" + s] = stats(rows)
res["control"] = stats(load(".b573_ctl.ttfb"))
print(json.dumps(res, ensure_ascii=False, indent=1))
with open(".b573_stats_snapshot.txt", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
