import re, math
lines = open("kz3_run156_out.txt").read().splitlines()
sections = {}
cur = None
for ln in lines:
    m = re.match(r"=== run(\w+) search", ln)
    if m:
        cur = "run" + m.group(1); sections[cur] = []; continue
    if ln.startswith("=== landing"):
        cur = "control"; sections[cur] = []; continue
    m = re.match(r"(\d{3}) ([\d.]+)", ln)
    if m and cur:
        sections[cur].append((int(m.group(1)), float(m.group(2))))
out_lines = []
total_cold = 0; total_n = 0
for name, vals in sections.items():
    codes = [c for c, t in vals]
    ts = sorted(t for c, t in vals if c == 200)
    cold = [t for t in ts if t >= 0.5]
    n = len(ts)
    if "run" in name:
        total_cold += len(cold); total_n += n
    if ts:
        def pct(p):
            k = max(1, math.ceil(p * n))
            return ts[k - 1]
        out_lines.append(
            f"{name}: n200={codes.count(200)}/{n} cold>=0.5s={len(cold)} "
            f"p50={pct(0.5)*1000:.1f}ms p90={pct(0.9)*1000:.1f}ms max={max(ts)*1000:.1f}ms "
            f"colds={[round(t,3) for t in cold]}")
out_lines.append(f"run total: cold {total_cold}/{total_n} ({100.0*total_cold/max(1,total_n):.1f}%)")
out = "\n".join(out_lines)
print(out)
open("kz3_run156_calc.txt", "w").write(out + "\n")
