import glob
for f in sorted(glob.glob('/tmp/cosient_tick/*.txt')):
    if 'uptime' in f or 'stats' in f:
        continue
    colds = 0; n = 0; codes = set(); times = []
    for line in open(f):
        parts = line.split()
        if len(parts) != 2:
            continue
        codes.add(parts[0])
        t = float(parts[1]); times.append(t); n += 1
        if t >= 0.5:
            colds += 1
    times.sort()
    p50 = times[(19*n)//20//2] if n else 0
    # nearest-rank p50
    import math
    p50 = times[max(0, math.ceil(0.5*n)-1)] if n else 0
    p95 = times[max(0, math.ceil(0.95*n)-1)] if n else 0
    mx = max(times) if times else 0
    warm = [x for x in times if x < 0.5]
    wp50 = warm[len(warm)//2] if warm else 0
    print(f"{f.split('/')[-1]}: n={n} codes={sorted(codes)} cold={colds}/{n} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={mx*1000:.1f}ms warm_p50={wp50*1000:.1f}ms")
