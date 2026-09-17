import statistics, sys

def stats(path):
    rows = []
    for line in open(path):
        parts = line.split()
        if len(parts) != 2:
            continue
        code, ttfb = parts[0], float(parts[1])
        rows.append((code, ttfb))
    codes = [r[0] for r in rows]
    ts = [r[1] for r in rows]
    cold = [t for _, t in rows if t >= 0.5]
    non200 = [c for c in codes if c != '200']
    print(f"{path}: n={len(rows)} non200={len(non200)} cold(>=0.5s)={len(cold)}/{len(rows)}"
          f" cold_vals={[round(t,4) for t in cold]}"
          f" p50={statistics.median(ts)*1000:.1f}ms p95={sorted(ts)[int(len(ts)*0.95)-1]*1000:.1f}ms max={max(ts)*1000:.1f}ms")

for p in ['_cos547_A.ttfb', '_cos547_B.ttfb', '_cos547_C.ttfb', '_cos547_landing.ttfb']:
    stats(p)
