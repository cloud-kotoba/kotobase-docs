import glob, statistics
base = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b589/'
def stats(path):
    codes = {}; times = []
    for line in open(path):
        parts = line.split()
        if len(parts) < 3: continue
        code, t = parts[-2], parts[-1]
        codes[code] = codes.get(code, 0) + 1
        times.append(float(t)*1000)
    times.sort()
    cold = sum(1 for t in times if t >= 500)
    coldv = [f'{t/1000:.4f}s' for t in times if t >= 500]
    p50 = statistics.median(times)
    p95 = times[int(len(times)*0.95)-1] if times else 0
    return codes, cold, coldv, p50, p95
for g in ['A','B','C']:
    c, cold, cv, p50, p95 = stats(base+f'run589{g}.raw')
    print(f'run589{g}: codes={c} cold(>=0.5s)={cold}/20 {cv} p50={p50:.1f}ms p95={p95:.1f}ms')
c, cold, cv, p50, p95 = stats(base+'control589.raw')
print(f'control: codes={c} cold={cold}/20 {cv} p50={p50:.1f}ms p95={p95:.1f}ms')
print(open(base+'smoke.txt').read().strip())
print(open(base+'hostload.txt').read().strip())
