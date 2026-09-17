import subprocess, time, json, datetime

def run_url(url, n, connect_reuse=False):
    times = []
    statuses = []
    for i in range(n):
        t0 = time.perf_counter()
        p = subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code} %{time_total}',
                            '--max-time','15', url], capture_output=True, text=True)
        dt = time.perf_counter() - t0
        out = p.stdout.strip()
        try:
            code, tt = out.split()
            tt = float(tt)
        except Exception:
            code, tt = 'ERR', dt
        statuses.append(code)
        times.append(tt)
        time.sleep(0.15)
    return times, statuses

def pct(nearest_rank_sorted, p):
    # nearest-rank percentile
    import math
    k = max(1, math.ceil(p/100*len(nearest_rank_sorted)))
    return nearest_rank_sorted[k-1]

results = {}
sets = ['run207A','run207B','run207C']
allcolds = 0; alln = 0
for s in sets:
    times, codes = run_url('https://kotobase.net/', 20)
    codes_ok = sum(1 for c in codes if c=='200')
    st = sorted(times)
    cold = [t for t in times if t > 0.9]
    allcolds += len(cold); alln += len(times)
    results[s] = {'n': len(times), 'ok200': codes_ok,
                  'p50': pct(st,50), 'p95': pct(st,95), 'max': st[-1],
                  'cold_count': len(cold), 'cold_times': cold,
                  'start': datetime.datetime.now().isoformat()}
    time.sleep(2)

ctimes, ccodes = run_url('https://kotobase.net/signup', 20)
cst = sorted(ctimes)
results['control_signup'] = {'n': len(ctimes), 'ok200': sum(1 for c in ccodes if c=='200'),
                             'p50': pct(cst,50), 'p95': pct(cst,95), 'max': cst[-1],
                             'cold_count': sum(1 for t in ctimes if t>0.9),
                             'cold_times': [t for t in ctimes if t>0.9],
                             'start': datetime.datetime.now().isoformat()}
results['total_cold'] = allcolds; results['total_n'] = alln
with open('_b82_run207.json','w') as f:
    json.dump(results, f, indent=1)
for k,v in results.items():
    print(k, json.dumps(v))
