import re, sys

def sets(path):
    txt = open(path).read()
    out = {}
    cur = None
    for line in txt.splitlines():
        m = re.match(r"SET ([ABC])", line)
        if m:
            cur = m.group(1); out[cur] = []
            continue
        if line.startswith("CONTROL"):
            cur = "CTRL"; out[cur] = []
            continue
        m = re.match(r"^(\d{3}) ([\d.]+)$", line.strip())
        if m and cur:
            out[cur].append((int(m.group(1)), float(m.group(2))))
    return out

d = sets(sys.argv[1])
for k, v in d.items():
    codes = [c for c, _ in v]
    times = sorted(t for _, t in v)
    n = len(times)
    cold = sum(1 for c, t in v if t >= 0.5)
    p50 = times[int(0.50 * n + 0.999) - 1] if n else 0
    p95 = times[max(0, int(0.95 * n + 0.999) - 1)] if n else 0
    print(f"{k}: n={n} non200={sum(1 for c in codes if c!=200)} cold(>=0.5s)={cold} p50={p50*1000:.0f}ms p95={p95*1000:.0f}ms max={max(times)*1000:.0f}ms")
