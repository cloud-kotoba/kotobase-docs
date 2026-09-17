def load(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    return [float(x) for x in lines]

def pct(vals, p):
    s = sorted(vals)
    n = len(s)
    idx = int((p / 100.0) * n + 0.999999)
    if idx < 1:
        idx = 1
    if idx > n:
        idx = n
    return s[idx - 1]

THRESH = 0.5
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b476"
files = {"A": base + "_A.ttfb", "B": base + "_B.ttfb", "C": base + "_C.ttfb", "landing": base + "_landing.ttfb"}

out = []
for k in ["A", "B", "C", "landing"]:
    vals = load(files[k])
    p50 = pct(vals, 50)
    p95 = pct(vals, 95)
    cold = sorted([v for v in vals if v >= THRESH])
    out.append((k, len(vals), len(cold), p50, p95, max(vals) if vals else 0.0, cold[:8]))

for k, n, ncold, p50, p95, mx, coldvals in out:
    cv = ", ".join("%.4f" % v for v in coldvals)
    print("RUN%s n=%d cold=%d/%d p50=%.4fs p95=%.4fs max=%.4fs cold_vals:[%s]" % (k, n, ncold, n, p50, p95, mx, cv))

ac = [o for o in out if o[0] == "A"][0][2]
bc = [o for o in out if o[0] == "B"][0][2]
cc = [o for o in out if o[0] == "C"][0][2]
print("SEARCH per20 cold: A=%d B=%d C=%d => total=%d/60 (%.1f%%)" % (ac, bc, cc, ac+bc+cc, 100.0*(ac+bc+cc)/60))
land = [o for o in out if o[0] == "landing"][0]
print("LANDING cold=%d/20 p50=%.4fs max=%.4fs" % (land[2], land[3], land[5]))