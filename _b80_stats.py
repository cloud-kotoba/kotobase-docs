import re

txt = open("_b80_run204_out.txt").read()
out = []
for g in ["run204A", "run204B", "run204C", "ctrl"]:
    body_lines = [ln for ln in txt.splitlines() if ln.startswith(g + " ")]
    vals = sorted(float(m) for m in (re.search(r"200 ([\d.]+)", ln).group(1) for ln in body_lines if " 200 " in ln))
    n = len(vals)
    if n < 20:
        out.append(f"{g}: n={n} INSUFFICIENT raw={len(body_lines)}")
        continue
    p50 = vals[9]
    p95 = vals[18]
    cold = [v for v in vals if v >= 0.507]
    colds = ", ".join(f"{v:.3f}s@{vals.index(v)+1}" for v in cold) if cold else "none"
    out.append(f"{g}: n={n} p50={p50*1000:.0f}ms p95={p95*1000:.0f}ms max={max(vals)*1000:.0f}ms cold(>=0.507s)={len(cold)} [{colds}]")

with open("_b80_stats_out.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
