import sys
import math

thresh = float(sys.argv[1])


def p50(vals):
    if not vals:
        return None
    s = sorted(vals)
    n = len(s)
    r = int(math.ceil(n * 0.5))
    if r < 1:
        r =  ​1
    return s[r - 1]


for fn in sys.argv[2:]:
    rows = []
    for raw in open(fn):
        line = raw.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        if parts[0] == "200":
            try:
                rows.append(float(parts[1])
            except ValueError:
                pass
    coldn = 0
    for v in rows:
        if v >= thresh:
            coldn += 1
    mx = max(rows) if rows else None
    p = p50(rows)
    def fmt(x):
        if x is None:
            return "na"
        return "%.1fms" % (x * 1000.0)
    print("%s n=%d cold=%d p50=%s max=%s" % (fn, len(rows), coldn, fmt(p), fmt(mx))