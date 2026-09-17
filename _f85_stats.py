import re, statistics
lat = []
cold = {"A": 0, "B": 0, "C": 0}
runs = {"A": [], "B": [], "C": []}
ctrl = []
codes_bad = 0
with open("_f85_run211_out.txt") as f:
    for line in f:
        m = re.match(r"run211([ABC]) (\d{3}) ([\d.]+)", line)
        c = re.match(r"control (\d{3}) ([\d.]+)", line)
        if m:
            r, code, t = m.group(1), int(m.group(2)), float(m.group(3))
            runs[r].append(t)
            if code != 200:
                codes_bad += 1
            if t >= 0.5:
                cold[r] += 1
        elif c:
            code, t = int(c.group(1)), float(c.group(2))
            ctrl.append((code, t))
with open("_f85_stats_out.txt", "w") as out:
    for r in "ABC":
        v = runs[r]
        out.write(f"run211{r}: n={len(v)} cold={cold[r]} p50={statistics.median(v)*1000:.1f}ms max={max(v)*1000:.1f}ms\n")
    cc = [t for _, t in ctrl]
    ctrlcold = sum(1 for t in cc if t >= 0.5)
    out.write(f"control: n={len(cc)} cold={ctrlcold} p50={statistics.median(cc)*1000:.1f}ms max={max(cc)*1000:.1f}ms\n")
    tot = sum(cold.values())
    out.write(f"total cold={tot}/60 non200={codes_bad}\n")
    cl = [t for v in runs.values() for t in v if t >= 0.5]
    out.write("cold latencies: " + ", ".join(f"{t:.3f}s" for t in sorted(cl)) + "\n")
