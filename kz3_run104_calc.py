import math

lines = open("kz3_run103_out.txt", encoding="utf-8").read().splitlines()
sections = {}
cur = None
for ln in lines:
    if ln.startswith("=== run103A"):
        cur = "runA"
    elif ln.startswith("=== run103B"):
        cur = "runB"
    elif ln.startswith("=== run103C"):
        cur = "runC"
    elif ln.startswith("=== landing"):
        cur = "landing"
    elif " " in ln and cur:
        parts = ln.split()
        if len(parts) == 2 and parts[0] == "200":
            sections.setdefault(cur, []).append(float(parts[1]))

def stats(vals):
    n = len(vals)
    cold = [v for v in vals if v >= 0.5]
    s = sorted(vals)
    p50 = s[math.ceil(0.5 * n) - 1]
    return n, len(cold), p50, min(vals), max(vals)

out = []
total_n = 0
total_cold_pos = 0
for k in ("runA", "runB", "runC", "landing"):
    n, cold_n, p50, mn, mx = stats(sections[k])
    label = "run104" + k[-1] if k.startswith("run") else "landing-control"
    out.append("%s: n=%d all200 cold>=0.5s %d/20 p50 %.3fs min %.3fs max %.3fs"
               % (label, n, cold_n, p50, mn, mx))
    if k.startswith("run"):
        total_n += n
        if cold_n > 0:
            total_cold_pos += 1

out.append("runs total: n=%d, trials with cold>0 = %d/3" % (total_n, total_cold_pos))
# 0h-band cumulative: run102A-C (3), falsify run103A-C (3), run104A-C (3) = 9 trials
# cold>0: run102A, run104A => 2/9. midnight band total: falsify said 78 trials 23 cold>0
out.append("0h-band cumulative: 9 trials, cold>0 = 2 (run102A, run104A)")
mid_n, mid_c = 78 + 3, 23 + 1
out.append("midnight-band cumulative: %d trials, cold>0 = %d (%.1f%%)"
           % (mid_n, mid_c, 100.0 * mid_c / mid_n))
with open("kz3_run104_calc_out.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
