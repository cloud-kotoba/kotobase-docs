#!/usr/bin/env python3
def parse(fn):
    rows = []
    for line in open(fn):
        p = line.strip().split()
        if len(p) < 2:
            continue
        try:
            rows.append((int(p[0]), float(p[1])))
        except ValueError:
            pass
    return rows

def report(fn, label, out):
    rows = parse(fn)
    o = []
    o.append(f"{label}: n={len(rows)}")
    codes = [c for c, _ in rows]
    tts = sorted(t for c, t in rows)
    nan = len(codes)
    all200 = all(c == 200 for c in codes)
    o.append(f"  lines={nan} all200={all200} non200={[c for c in codes if c != 200]}")
    p50 = tts[min(nan - 1, int(0.5 * nan))]
    cold = [(i + 1, t) for i, (c, t) in enumerate(rows) if c == 200 and t >= 0.5]
    o.append(f"  p50={p50*1000:.1f}ms max={tts[-1]*1000:.1f}ms")
    o.append(f"  cold(>=0.5s): {len(cold)}/{len(rows)} -> {len(cold)}; positions/times: {[(p, '%.4fs'%t) for p,t in cold]}")
    out.write("\n".join(o) + "\n")

with open("/tmp/stats364_final.txt", "w") as out:
    report(".b364_364A.txt", "run364A", out)
    report(".b364_364B.txt", "run364B", out)
    report(".b364_364C.txt", "run364C", out)
    report(".b364_land.txt", "control-LAND", out)
print("written")