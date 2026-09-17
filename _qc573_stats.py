import statistics

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
    cold = [(i, t) for i, (_, t) in enumerate(rows, 1) if t >= 0.5]
    non200 = [c for c in codes if c != '200']
    print(f"{path}: n={len(rows)} non200={len(non200)} cold(>=0.5s)={len(cold)}/{len(rows)}"
          f" cold_posvals=[{', '.join(f'#{i}:{t:.4f}' for i, t in cold)}]"
          f" p50={statistics.median(ts)*1000:.1f}ms max={max(ts)*1000:.1f}ms")

for p in ['_qc573_A.ttfb', '_qc573_B.ttfb', '_qc573_C.ttfb', '_qc573_landing.ttfb']:
    stats(p)
