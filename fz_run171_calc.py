import re
vals = {"171A": [], "171B": [], "171C": [], "LC": []}
for ln in open("fz_run171_out.txt"):
    m = re.match(r"(171[ABC]|LC)\s+\d+\s+([\d.]+)\s+(\d+)", ln)
    if m:
        vals[m.group(1)].append((float(m.group(2)), int(m.group(3))))
for k in ["171A", "171B", "171C", "LC"]:
    v = vals[k]
    ts = sorted(x[0] for x in v)
    codes = set(x[1] for x in v)
    p50 = ts[len(ts)//2] if ts else None
    cold = sum(1 for t in ts if t >= 0.5)
    print(k, "n=%d" % len(v), "codes=%s" % codes, "cold=%d/20" % cold,
          "p50=%.3f" % p50 if p50 else "", "min=%.3f" % ts[0] if ts else "",
          "max=%.3f" % ts[-1] if ts else "", "coldvals=%s" % [t for t in ts if t >= 0.5])
