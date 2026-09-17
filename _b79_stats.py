import re

groups = {}
with open("_b79_run202_out.txt") as f:
    for line in f:
        m = re.match(r"(\S+) (\d+) (\d{3}) (\S+)", line.strip())
        if m:
            g, i, code, t = m.group(1), int(m.group(2)), m.group(3), float(m.group(4))
            groups.setdefault(g, []).append((i, code, t))

out = []
for g, rows in groups.items():
    codes = [r[1] for r in rows]
    times = sorted(r[2] for r in rows)
    n = len(times)
    # nearest-rank p50
    p50 = times[max(0, (n + 1) // 2 - 1)]
    p95 = times[max(0, round(0.95 * n + 0.5) - 1)] if n >= 20 else None
    cold = [t for _, c, t in rows if c == "200" and t >= 0.5]
    non200 = [(i, c, t) for i, c, t in rows if c != "200"]
    out.append(
        f"{g}: n={n} non200={len(non200)} cold>=0.5s={len(cold)} "
        f"cold_vals={[round(t,3) for t in cold]} "
        f"p50={round(p50*1000,1)}ms max={round(times[-1]*1000,1)}ms"
    )
    if non200:
        out.append(f"  non200 detail: {non200}")

with open("_b79_stats_out.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
