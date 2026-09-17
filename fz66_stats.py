import re

rows = {}
lc = []
cur = None
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/fz66_run173_out.txt") as f:
    for line in f:
        m = re.match(r"^(173[ABC]|LC)\s+(\d+)\s+([\d.]+)\s+(\d+)", line)
        if m:
            tag, idx, ttfb, code = m.group(1), int(m.group(2)), float(m.group(3)), m.group(4)
            if tag == "LC":
                lc.append((ttfb, code))
            else:
                rows.setdefault(tag, []).append((ttfb, code))

def p50(vals):
    s = sorted(vals)
    n = len(s)
    import math
    k = math.ceil(0.5 * n)  # nearest-rank
    return s[k - 1]

for tag in ["173A", "173B", "173C"]:
    vals = [t for t, c in rows[tag]]
    codes = set(c for t, c in rows[tag])
    cold = [t for t in vals if t >= 0.5]
    print(f"{tag}: n={len(vals)} codes={codes} cold>=0.5s={len(cold)} {cold} p50={p50(vals)*1000:.0f}ms max={max(vals)*1000:.0f}ms")

lvals = [t for t, c in lc]
lcodes = set(c for t, c in lc)
lcold = [t for t in lvals if t >= 0.5]
print(f"LC: n={len(lvals)} codes={lcodes} cold>=0.5s={len(lcold)} {lcold} p50={p50(lvals)*1000:.0f}ms max={max(lvals)*1000:.0f}ms")

allc = sum(1 for tag in rows for t, c in rows[tag] if t >= 0.5)
alln = sum(len(rows[tag]) for tag in rows)
print(f"total cold {allc}/{alln}")
