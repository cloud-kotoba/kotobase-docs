import json
d = json.load(open("bench42_raw_data.json"))
print("time:", d["time"])
for tag in ("A", "B", "C", "landing"):
    seq = d["data"][tag]
    codes = [r["code"] for r in seq]
    ttfbs = [r["ttfb"] for r in seq]
    ok = sum(1 for c in codes if c == 200)
    colds = [t for t in ttfbs if t >= 0.5]
    s = sorted(ttfbs)
    p50 = s[int(0.50 * len(s) + 0.999) - 1]
    warms = sorted(t for t in ttfbs if t < 0.5)
    line = "%s n=%d ok200=%d cold=%d p50=%.3fs" % (tag, len(seq), ok, len(colds), p50)
    if colds:
        line += " colds=" + " ".join("%.3fs(#%d)" % (t, ttfbs.index(t)+1) for t in colds)
    line += " warm=%.3f-%.3f" % (warms[0], warms[-1])
    print(line)
