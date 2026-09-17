import time, subprocess, json, statistics, re

EP = 'https://search.yataverse.com/search?q=test'
CTRL = 'https://kotoba.cloud/'
N = 20
series = {}
labels = ['625A','625B','625C']
out = {'ts': time.strftime('%Y-%m-%d %H:%M:%S JST'), 'groups': {}}
for lab in labels + ['CTRL']:
    url = EP if lab != 'CTRL' else CTRL
    times = []
    codes = []
    for i in range(N):
        t0 = time.time()
        p = subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code} %{time_total}','--max-time','15', url], capture_output=True, text=True)
        dt = time.time() - t0
        line = p.stdout.strip()
        try:
            code, tt = line.split()
            codes.append(code)
            times.append(float(tt))
        except Exception:
            codes.append('ERR:'+line[:40])
            times.append(None)
    ok = [t for t in times if t is not None and t < 5]
    colds = sorted([t for t in times if t is not None and t >= 0.5])
    p50 = statistics.median(times) if times else None
    p95 = sorted(times)[int(len(times)*0.95)-1] if times else None
    out['groups'][lab] = {'codes': codes, 'cold': colds, 'p50_ms': round(p50*1000,1) if p50 else None, 'max_ms': round(max(times)*1000,1) if times else None, 'p95_ms': round(p95*1000,1) if p95 else None, 'all': times}
print(json.dumps(out, ensure_ascii=False))
