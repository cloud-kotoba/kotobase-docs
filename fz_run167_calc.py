import re, sys
f = open('fz_run167_out2.txt').read()
blocks = re.findall(r'=== (.+?) ===\n((?:.*\n)*?)(?==== |\Z)', f)
for name, body in blocks:
    vals = []
    bad = []
    for line in body.strip().splitlines():
        parts = line.split()
        if len(parts) < 3 or not parts[-1].isdigit():
            continue
        try:
            ttfb = float(parts[-2])
        except ValueError:
            continue
        code = parts[-1]
        vals.append(ttfb)
        if code != '200': bad.append((line, code))
    if not vals:
        continue
    s = sorted(vals); n = len(s)
    p50 = s[(n-1)//2]
    cold = [(i+1, v) for i, v in enumerate(vals) if v >= 0.5]
    print(f"{name}: n={n} cold>=0.5s {len(cold)}/{n} p50={p50:.3f}s min={min(vals):.3f} max={max(vals):.3f} non200={len(bad)}")
    for i, v in cold: print(f"  cold #{i} {v:.3f}s")
