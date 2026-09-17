import glob, math
for name in ["A","B","C","ctl"]:
    f = ".f613_run613%s.ttfb" % name if name != "ctl" else ".f613_ctl.ttfb"
    rows = [l.split() for l in open(f) if l.strip()]
    codes = [r[0] for r in rows]
    tt = sorted(float(r[1]) for r in rows)
    cold = [t for t in tt if t >= 0.5]
    k50 = max(1, math.ceil(0.5*len(tt)))
    p95 = tt[max(0, math.ceil(0.95*len(tt))-1)]
    print(name, "n=%d" % len(tt), "200=%d" % codes.count("200"),
          "cold=%d" % len(cold), "coldvals=%s" % [round(t,3) for t in cold],
          "p50=%.1fms" % (tt[k50-1]*1000), "p95=%.1fms" % (p95*1000), "max=%.1fms" % (tt[-1]*1000))
