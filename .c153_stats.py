import statistics

def load(path):
    rows = []
    with open(path) as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                rows.append((int(parts[0]), float(parts[1])))
    return rows

def p50(xs):
    xs = sorted(xs)
    import math
    k = max(0, math.ceil(0.5 * len(xs)) - 1)
    return xs[k]

def p95(xs):
    xs = sorted(xs)
    import math
    k = max(0, math.ceil(0.95 * len(xs)) - 1)
    return xs[k]

total_cold = 0
total_n = 0
for label in ("A", "B", "C", "CTRL"):
    rows = load(f".c153_run625_{label}.ttfb" if label != "CTRL" else ".c153_run625_landing.ttfb")
    codes = [c for c, _ in rows]
    tt = [t for _, t in rows]
    colds = [(i + 1, t) for i, t in enumerate(tt) if t >= 0.5]
    cold = len(colds)
    ok = codes.count(200)
    if label != "CTRL":
        total_cold += cold
        total_n += len(tt)
    print(f"run625{label}: 200 {ok}/{len(rows)} cold(>=0.5s) {cold}/20 "
          f"p50 {p50(tt)*1000:.1f}ms p95 {p95(tt)*1000:.1f}ms max {max(tt)*1000:.1f}ms "
          f"cold_pos {colds}")
print(f"SEARCH TOTAL: cold {total_cold}/{total_n} ({100*total_cold/total_n:.1f}%)")
