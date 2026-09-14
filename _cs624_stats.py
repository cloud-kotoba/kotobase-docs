import re

def stats(path):
    tt = []
    codes = []
    for line in open(path):
        m = re.match(r'(\d+) ([\d.]+)', line)
        if m:
            codes.append(int(m.group(1)))
            tt.append(float(m.group(2)))
    if not tt:
        return None
    tt_sorted = sorted(tt)
    cold = [x for x in tt if x >= 0.5]
    p50 = tt_sorted[len(tt_sorted)//2 if len(tt_sorted) % 2 == 1 else len(tt_sorted)//2 - 1] if tt_sorted else 0
    # nearest-rank p50
    import math
    k = max(1, math.ceil(0.5 * len(tt_sorted)))
    p50 = tt_sorted[k-1]
    out = {
        "n": len(tt), "ok200": sum(1 for c in codes if c == 200),
        "cold": len(cold), "p50": p50, "max": max(tt), "min": min(tt),
    }
    if cold:
        out["cold_vals"] = cold
    return out

groups = ["A", "B", "C"]
res = {}
for g in groups:
    res[g] = stats(f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_cs624_{g}.ttfb")
res["landing"] = stats("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_cs624_landing.ttfb")
for k, v in res.items():
    print(k, v)
