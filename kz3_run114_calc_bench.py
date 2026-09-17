import re, statistics

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run114_out.txt"
src = open(p, encoding="utf-8").read().splitlines()
runs, cur = {}, None
for line in src:
    m = re.match(r"=== (run114[A-C]|landing control)", line)
    if m:
        cur = m.group(1).strip(); runs.setdefault(cur, []); continue
    m = re.match(r"(\d{3}) ([\d.]+)", line)
    if m and cur:
        runs[cur].append((int(m.group(1)), float(m.group(2))))
out = []
n_cold_runs = 0
n_search = 0
for name, samples in runs.items():
    codes = [c for c, _ in samples]; ts = sorted(t for _, t in samples)
    cold = [t for _, t in samples if t >= 0.5]; n = len(ts)
    out.append(f"{name}: n={n} non200={sum(1 for c in codes if c != 200)} cold={len(cold)} vals={[round(t,3) for t in cold]} p50={statistics.median(ts):.3f} min={ts[0]:.3f} max={ts[-1]:.3f}")
    if "control" not in name:
        n_search += 1
        if len(cold) > 0: n_cold_runs += 1
out.append(f"\nsearch runs cold>0: {n_cold_runs}/{n_search}")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run114_calc_out.txt", "w").write("\n".join(out) + "\n")
print("ok")
