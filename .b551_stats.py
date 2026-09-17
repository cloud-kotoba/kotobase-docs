import statistics as st
files = [".b551_run551A.ttfb",".b551_run551B.ttfb",".b551_run551C.ttfb",".b551_run551_landing.ttfb"]
tot_cold = tot_n = tot_200 = 0
out = []
for f in files:
    rows = []
    for ln in open(f):
        p = ln.split()
        if len(p) == 2:
            rows.append((float(p[0]), p[1]))
    ts = [r[0] for r in rows]
    codes = [r[1] for r in rows]
    cold = [t for t in ts if t >= 0.5]
    n200 = codes.count("200")
    p50 = st.median(ts)
    mx = max(ts)
    label = f.split("_")[1].replace(".ttfb","")
    out.append(f"{label}: n={len(ts)} 200={n200} cold={len(cold)} p50={p50*1000:.1f}ms max={mx*1000:.1f}ms" + (f" cold_list={[round(c,4) for c in cold]}" if cold else ""))
    if "landing" not in f:
        tot_cold += len(cold); tot_n += len(ts)
    tot_200 += n200
out.append(f"TOTAL search: {tot_cold}/{tot_n} cold ({tot_cold/tot_n*100:.1f}%), all 200 = {tot_200}/80")
print("\n".join(out))
open(".b551_stats_out.txt","w").write("\n".join(out)+"\n")
