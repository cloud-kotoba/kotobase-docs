#!/usr/bin/env python3
import subprocess, time, json, sys
from statistics import median

SEARCH = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"

def curl_once(url):
    # separate connection each request (no reuse), cold TTFB
    start = time.perf_counter()
    try:
        r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer} %{time_total}", url],
                           capture_output=True, text=True, timeout=30)
        out = r.stdout.strip()
        parts = out.split()
        code = int(parts[0]) if parts else -1
        ttfb = float(parts[1]) if len(parts) > 1 else -1.0
        total = float(parts[2]) if len(parts) > 2 else ttfb
    except Exception as e:
        return (-1, -1.0, str(e))
    return (code, ttfb, total)

def nearest_rank_p50(vals):
    # nearest-rank percentile p50 over the run sample
    sv = sorted(vals)
    idx = max(1, int(0.50 * len(sv) + 0.5))
    return sv[idx-1]

def run_set(label, n, url):
    codes = []
    ttfbs = []
    cold = []
    for i in range(n):
        code, ttfb, total = curl_once(url)
        codes.append(code)
        ttfbs.append(round(ttfb*1000, 1))
        if ttfb >= 0.5:
            cold.append((i+1, round(ttfb, 4)))
    return {"label": label, "n": n, "codes": codes, "ttfbs": ttfbs,
            "cold": cold, "cold_count": len(cold),
            "raw": [round(t,4) for t in ttfbs]}

results = {}
t0 = time.strftime("%H:%M:%S", time.localtime())
results["start"] = t0

# search runs A/B/C : n=20 each
for tag in ["A","B","C"]:
    results[tag] = run_set(tag, 20, SEARCH)

# landing control n=20
results["ctrl"] = run_set("ctrl", 20, CONTROL)

t1 = time.strftime("%H:%M:%S", time.localtime())
results["end"] = t1
results["uptime"] = None

# summarize
def summ(res):
    scores = [x for x in res["ttfbs"] if x >= 0]
    return {"cold": res["cold_count"], "n": res["n"],
            "p50_ms": round(nearest_rank_p50([x/1000.0 for x in scores])*1000,1) if scores else None,
            "min_ms": round(min(scores),1) if scores else None,
            "max_ms": round(max(scores),1) if scores else None,
            "http_not200": sum(1 for c in res["codes"] if c != 200)}
for k in ["A","B","C","ctrl"]:
    results[k+"_sum"] = summ(results[k])

print(json.dumps(results, ensure_ascii=False, indent=1))