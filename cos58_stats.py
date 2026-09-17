import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos58_run169_out.txt"
runs = {}
lc = []
cur = None
with open(path) as f:
    for line in f:
        m = re.match(r"^(169[ABC]|LC) (\d+) ([\d.]+) (\d+)$", line.strip())
        if m:
            key, i, ttfb, code = m.group(1), int(m.group(2)), float(m.group(3)), int(m.group(4))
            if key == "LC":
                lc.append((i, ttfb, code))
            else:
                runs.setdefault(key, []).append((i, ttfb, code))

def p50_nearest_rank(vals):
    s = sorted(vals)
    import math
    k = math.ceil(0.5 * len(s))
    return s[k - 1]

for key in ["169A", "169B", "169C"]:
    rows = runs[key]
    codes = [c for _, _, c in rows]
    vals = [t for _, t, _ in rows]
    cold = [(i, t) for i, t, _ in rows if t >= 0.5]
    s = sorted(vals)
    print(f"{key}: n={len(rows)} non200={codes.count(200) != len(codes) and [c for c in codes if c != 200]} cold(>=0.5s)={len(cold)}/20 positions={[i for i,_ in cold]} cold_vals={[round(t,3) for _,t in cold]} p50={p50_nearest_rank(vals):.3f}s min={min(vals):.3f} max={max(vals):.3f}")
    print(f"  sorted: {[round(v,3) for v in s]}")

codes_lc = [c for _, _, c in lc]
vals_lc = [t for _, t, _ in lc]
cold_lc = [(i, t) for i, t, _ in lc if t >= 0.5]
print(f"LC: n={len(lc)} cold={len(cold_lc)}/20 p50={p50_nearest_rank(vals_lc):.3f}s max={max(vals_lc):.3f}s non200={[c for c in codes_lc if c != 200]}")

# 20時台 cumulative: prior 8/300 (run89-91 180 + run167 60 + run168 60) + this tick 4/60
total_n = 300 + 60
total_cold = 8 + 4
print(f"20時台通算: {total_cold}/{total_n} = {total_cold/total_n*100:.1f}%")
