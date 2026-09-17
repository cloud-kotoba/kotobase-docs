import statistics
base = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b611/'
for f in ['A','B','C','landing']:
    rows = [l.split() for l in open(base + f'b611s_{f}.tsv') if l.strip()]
    codes = [r[0] for r in rows]
    ts = [float(r[1])*1000 for r in rows]
    ttfb = [float(r[2])*1000 for r in rows]
    cold = [(i, t) for i, t in enumerate(ts) if t >= 500]
    s = sorted(ts)
    print(f'{f}: n={len(ts)} codes={sorted(set(codes))} cold(>=0.5s)={len(cold)} {[round(t,4) for _, t in cold]} p50={statistics.median(ts):.1f}ms p95={s[int(len(s)*0.95)-1]:.1f}ms max={max(ts):.1f}ms ttfb_p50={statistics.median(ttfb):.1f}ms')
print(open(base + 'meta.txt').read().strip())
