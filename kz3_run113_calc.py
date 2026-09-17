import re, statistics

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run113_out.txt"
src = open(p, encoding="utf-8").read().splitlines()

runs = {}
cur = None
for line in src:
    m = re.match(r"=== (run\S+|landing control\S*)", line)
    if m:
        cur = m.group(1).strip()
        runs.setdefault(cur, [])
        continue
    m = re.match(r"(\d{3}) ([\d.]+)", line)
    if m and cur:
        runs[cur].append((int(m.group(1)), float(m.group(2))))

out = []
total_cold_runs = 0
for name, samples in runs.items():
    codes = [c for c, _ in samples]
    ts = sorted(t for _, t in samples)
    cold = [t for _, t in samples if t >= 0.5]
    n = len(ts)
    p50 = statistics.median(ts)
    out.append(f"{name}: n={n} non200={sum(1 for c in codes if c != 200)} "
               f"cold(>=0.5s)={len(cold)} cold_vals={[round(t,3) for t in cold]} "
               f"p50={p50:.3f}s min={ts[0]:.3f} max={ts[-1]:.3f}")
    if "control" not in name and len(cold) > 0:
        total_cold_runs += 1

out.append(f"\nsearch runs cold>0: {total_cold_runs} / {sum(1 for k in runs if 'control' not in k)}")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run113_calc_out.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("ok")
