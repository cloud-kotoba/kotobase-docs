import glob
for grp in ["A","B","C","CTRL"]:
    f = f"/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b642_out/.b642_{grp}.tsv"
    lat = []
    codes = {}
    colds = []
    for line in open(f):
        parts = line.split()
        if len(parts) < 3: continue
        i, code, t = parts[0], parts[1], parts[2]
        codes[code] = codes.get(code, 0) + 1
        sec = float(t)
        lat.append(sec)
        if sec >= 0.5:
            colds.append((i, sec))
    lat_s = sorted(lat)
    n = len(lat)
    p50 = lat_s[n//2]*1000 if n else 0
    p95 = lat_s[int(n*0.95)]*1000 if n else 0
    mx = lat_s[-1]*1000 if n else 0
    coldstr = ", ".join(f"#{i} {s*1000:.1f}ms" for i, s in colds) or "none"
    print(f"{grp}: n={n} codes={codes} cold(>=0.5s)={len(colds)}/{n} p50={p50:.1f}ms p95={p95:.1f}ms max={mx:.1f}ms cold_detail=[{coldstr}]")
