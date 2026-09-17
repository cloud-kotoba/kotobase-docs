import io
lines = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_run174_out.txt", encoding="utf-8").read().splitlines()
runs = {}
cur = None
for ln in lines:
    if ln.startswith("=== run174"):
        cur = ln.split()[1]
        runs[cur] = []
    elif ln.startswith("=== landing"):
        cur = "LC"
        runs[cur] = []
    elif ln.startswith(("174A", "174B", "174C", "LC ")):
        parts = ln.split()
        t = float(parts[2])
        code = parts[3]
        runs[cur].append((t, code))
for k, vals in runs.items():
    ts = sorted(t for t, c in vals)
    n = len(ts)
    p50 = ts[10 - 1]  # nearest-rank for n=20
    cold = [t for t in ts if t >= 0.5]
    codes = set(c for t, c in vals)
    print(k, "n=%d" % n, "codes=%s" % sorted(codes), "cold(>=0.5s)=%d %s" % (len(cold), ["%d番目 %ss" % (sorted(vals).index((c, '200'))+1, c) for c in cold]), "p50=%.3fs" % p50, "min=%.3f" % ts[0], "max=%.3f" % ts[-1])
