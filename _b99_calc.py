import sys

lines = open("/tmp/bench99_run246_out.txt").read().splitlines()

runs = {"run246A":[], "run246B":[], "run246C":[], "control":[]}
for ln in lines:
    for tag in runs:
        if ln.startswith(tag + " "):
            parts = ln.split()
            code = parts[1]
            t = float(parts[2])
            runs[tag].append((code, t))
            break

def nearest_rank_p50(vals):
    s = sorted(vals)
    idx = int(0.50 * len(vals) + 0.999) - 1
    return s[idx]

for tag, entries in runs.items():
    codes = [c for c,_ in entries]
    ttfbs = [t for _,t in entries]
    ok = sum(1 for c in codes if c == "200")
    colds = [t for t in ttfbs if t >= 0.5]
    p50 = nearest_rank_p50(ttfbs)
    s = sorted(ttfbs)
    p95 = s[int(0.95*len(s)+0.999)-1]
    line = "%s all=%d ok=%d cold(>=0.5s)=%d p50=%.3fs p95=%.3fs min=%.3fs max=%.3fs" % (
        tag, len(entries), ok, len(colds), p50, p95, min(ttfbs), max(ttfbs))
    if colds:
        line += " colds=" + " ".join("%.3fs(#%d)"%(t, ttfbs.index(t)+1) for t in colds)
    else:
        line += " + warm all"
    print(line)