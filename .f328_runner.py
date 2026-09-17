#!/usr/bin/env python3
"""K-Z3 8時台 run328A-C + landing control. Same measurement method as claim contract:
n=20 x3 search (search.kotobase.net/search?q=test) + n=20 landing control (kotobase.net/signup),
separate curl connections, cold threshold >= 0.5s TTFB, nearest-rank p50.
Production HTTP -> exempt from host load gate."""
import subprocess, time, sys, json, math

def run_curl(url, timeout=65):
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer}",
           "--connect-timeout", "20", "--max-time", str(timeout), url]
    start = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+10)
    elapsed = time.time() - start
    out = (p.stdout or "").strip()
    parts = out.split()
    if len(parts) < 2:
        return (None, None, elapsed, p.stderr.strip())
    code, ttfb = parts[0], parts[1]
    try:
        return (int(code), float(ttfb), elapsed, "")
    except ValueError:
        return (None, None, elapsed, out)

def percentile_nearest_rank(data, q):
    s = sorted(data)
    if not s:
        return 0.0
    pos = int(math.ceil(q * len(s)))
    pos = max(1, min(pos, len(s)))
    return s[pos - 1]

def report(name, items):
    codes = [it[0] for it in items]
    ttfbs = [it[1] for it in items if it[1] is not None]
    cold = [it for it in items if it[1] is not None and it[1] >= 0.5]
    n = len(ttfbs)
    p50 = percentile_nearest_rank(ttfbs, 0.5) if ttfbs else 0.0
    p90 = percentile_nearest_rank(ttfbs, 0.9) if ttfbs else 0.0
    mx = max(ttfbs) if ttfbs else 0.0
    errs = [it[4] for it in items if it[0] is None]
    all200 = all(c == 200 for c in codes)
    return {
        "name": name, "n": n, "all200": all200,
        "cold": len(cold), "cold_idxs": [it[5] for it in cold],
        "cold_ttfb": [round(it[1], 4) for it in cold],
        "p50_ms": round(p50 * 1000, 1), "p90_ms": round(p90 * 1000, 1),
        "max_ms": round(mx * 1000, 1), "errors": errs,
        "min_ms": round(min(ttfbs) * 1000, 1) if ttfbs else 0.0,
    }

def measure(url, label, n=20):
    items = []
    for i in range(1, n + 1):
        code, ttfb, elapsed, err = run_curl(url)
        t = time.strftime("%H:%M:%S")
        items.append((code, ttfb, elapsed, err, t, i))
        time.sleep(0.8)
    return report(label, items)

results = {}
search_url = "https://search.kotobase.net/search?q=test"
land_url = "https://kotobase.net/signup"

for tag, url in [("run328A", search_url), ("run328B", search_url), ("run328C", search_url)]:
    results[tag] = measure(url, tag, 20)

results["landing"] = measure(land_url, "landing", 20)

load = subprocess.run(["uptime"], capture_output=True, text=True).stdout.strip()
print(json.dumps({"results": results, "uptime": load,
                  "started": time.strftime("%Y-%m-%d %H:%M:%S JST")}, indent=2))