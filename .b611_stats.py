import glob, statistics
for f in ['A','B','C','CTL']:
    path = f'/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b611_{f}.csv'
    rows = [l.strip().split(',') for l in open(path) if l.strip()]
    codes = [r[1].split()[0] for r in rows]
    ts = [float(r[1].split()[1])*1000 for r in rows]
    cold = [t for t in ts if t >= 500]
    p50 = statistics.median(ts)
    p95 = sorted(ts)[int(len(ts)*0.95)-1]
    mx = max(ts)
    print(f'{f}: n={len(ts)} codes={set(codes)} cold(>=0.5s)={len(cold)} cold_vals={[round(c,4) for c in cold]} p50={p50:.1f}ms p95={p95:.1f}ms max={mx:.1f}ms')
print(open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b611_uptime.txt').read().strip())
