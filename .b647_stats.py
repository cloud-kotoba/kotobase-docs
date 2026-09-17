import csv, glob, statistics, os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
lines = []
for name in ["A", "B", "C", "ctl"]:
    f = os.path.join(base, f".b647_{name}.csv")
    ts = []
    codes = []
    with open(f) as fh:
        for row in csv.reader(fh):
            if len(row) != 2:
                continue
            code, t = row[1].split()
            codes.append(code)
            ts.append(float(t) * 1000.0)
    ts_sorted = sorted(ts)
    p50 = statistics.median(ts)
    p95 = ts_sorted[max(0, int(len(ts_sorted) * 0.95) - 1)] if ts_sorted else 0
    cold = [t for t in ts if t >= 500.0]
    lines.append(
        f"{name}: n={len(ts)} codes={'/'.join(sorted(set(codes)))} "
        f"cold(>=500ms)={len(cold)}/{len(ts)} cold_ms={[round(t,1) for t in cold]} "
        f"p50={p50:.1f}ms p95={p95:.1f}ms max={max(ts):.1f}ms"
    )
with open(os.path.join(base, ".b647_stats.txt"), "w") as out:
    out.write("\n".join(lines) + "\n")
with open(os.path.join(base, ".b647_meta.txt")) as fh:
    out.write(fh.read())
