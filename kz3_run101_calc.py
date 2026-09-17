import re, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run101_out.txt"
lines = open(path).read().splitlines()
runs = {}
cur = None
ctrl = []
for ln in lines:
    m = re.match(r"=== run(\S+) search ===", ln)
    if m:
        cur = m.group(1); runs[cur] = []; continue
    if ln.startswith("=== landing control ==="):
        cur = "CTRL"; continue
    m = re.match(r"(\d{3}) ([\d.]+)", ln)
    if m and cur:
        (ctrl if cur == "CTRL" else runs[cur]).append((int(m.group(1)), float(m.group(2))))

def stats(name, xs, cold_th=0.5):
    codes = [c for c, t in xs]
    ts = sorted(t for c, t in xs)
    n = len(ts)
    ok = codes.count(200)
    cold = [t for t in ts if t >= cold_th]
    # nearest-rank percentile: ceil(p/100 * n), 1-indexed
    import math
    p50 = ts[math.ceil(0.5 * n) - 1]
    p95 = ts[math.ceil(0.95 * n) - 1]
    print(f"{name}: n={n} ok200={ok} cold(>={cold_th}s)={len(cold)}/{n} "
          f"cold_vals={[round(t,3) for t in cold]} p50={p50:.3f}s p95={p95:.3f}s min={ts[0]:.3f} max={ts[-1]:.3f}")

for rid in ["101A", "101B", "101C"]:
    stats(f"run{rid}", runs[rid])
stats("control(landing)", ctrl)
