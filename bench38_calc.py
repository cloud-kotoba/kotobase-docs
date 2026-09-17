import io, statistics
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench38_run_out.txt"
txt = io.open(path, encoding="utf-8").read()
sections = {}
cur = None
for ln in txt.splitlines():
    if ln.startswith("==="):
        cur = ln.strip("= ").split(" ", 1)[0]
        sections[cur] = []
    else:
        parts = ln.split()
        if len(parts) == 2 and cur:
            sections[cur].append((int(parts[0]), float(parts[1])))
def nr(vals, p):
    s = sorted(vals)
    import math
    k = max(1, math.ceil(p * len(s)))
    return s[k-1]
for name, data in sections.items():
    codes = [c for c, _ in data]
    ts = [t for _, t in data]
    cold = [t for t in ts if t >= 0.5]
    print(name, "n=", len(ts), "200:", codes.count(200), "cold(>=0.5s):", len(cold), cold,
          "p50:", round(nr(ts, 0.5)*1000, 1), "ms",
          "p95:", round(nr(ts, 0.95)*1000, 1), "ms",
          "min:", round(min(ts)*1000, 1), "max:", round(max(ts)*1000, 1))
