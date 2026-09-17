import sys, glob
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b584"
for label in ["run584A", "run584B", "run584C", "control"]:
    vals = []
    try:
        with open(f"{base}/{label}.txt") as f:
            for line in f:
                line = line.strip()
                if line:
                    vals.append(float(line))
    except FileNotFoundError:
        print(f"{label}: MISSING")
        continue
    if not vals:
        print(f"{label}: EMPTY")
        continue
    s = sorted(vals)
    n = len(s)
    def p(q):
        import math
        k = max(1, math.ceil(q * n))
        return s[k - 1]
    cold = [v for v in s if v >= 0.5]
    print(f"{label}: n={n} cold(>=0.5s)={len(cold)} p50={p(0.5)*1000:.1f}ms p95={p(0.95)*1000:.1f}ms min={s[0]*1000:.1f}ms max={s[-1]*1000:.1f}ms")
    if cold:
        print(f"  cold values: {[round(v,3) for v in cold]}")
