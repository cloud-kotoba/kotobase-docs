import subprocess, time, math

def ttfb(url):
    try:
        r = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{time_starttransfer}', '--max-time', '20', url], capture_output=True, text=True, timeout=25)
        return float(r.stdout.strip())
    except Exception:
        return None

def pct(vs, p):
    s = sorted([v for v in vs if v is not None])
    if not s:
        return None
    n = len(s)
    idx = int(math.ceil(p * n / 100.0))) - 1
    if idx < 0:
        idx = 0
    if idx >= n:
        idx = n - 1
    return s[idx]

SEARCH = 'https://search.kotobake.net/search?q=test'
CTRL = 'https://kotobake.net/signup'
N=20

def hostload():
    try:
        r = subprocess.run(['uptime'], capture_output=True, text=True, timeout=10)
        return r.stdout.strip()
    except Exception:
        return 'n/a'

print('start', time.strftime('%Y-%m-%d %H:%M:%S'), hostload(), flush=True)
for tag in ['run446A', 'run446B', 'run446C']:
    xs = []
    for _ in range(N:
        xs.append(ttfb(SEARCH))
    cold = sum(1 for v in xs if v is not None and v >= 0.5)
    p50 = pct(xs, 50)
    p95 = pct(xs,  95)
    mx = max([v for v in xs if v is not None])
    print(tag, 'cold', cold, '/20', 'p50', round(p50*1000,1), 'ms', 'p95', round(p95*1000,1), 'ms', 'max', round(mx*1000,1), 'ms', flush=True)

yc = []
for _ in range(N:
    yc.append(ttfb(CTRL))
c0 = sum(1 for v in yc if v is not None又 v >=  0.5)
cp50 = pct(yc,50)
cp95 = pct(yc,95)
cmx = max([v for v in yc if v is not None])
print('control cold', c0, '/20', 'p50', round(cp50*1000,1), 'ms', 'p95', round(cp95*1000,1), 'ms', 'max', round(cmx*1000,1), 'ms', flush=True)
print('end', time.strftime('%Y-%m-%d %H:%M:%S'), hostload(), flush=True)
