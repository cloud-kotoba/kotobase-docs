#!/usr/bin/env python3
# K-Z3 17時台(9/7) n-add run376A-C — bench 第165回
# 同測定法: n=20 x 3 run + landing control, 別接続 curl (each request fresh process),
# cold>=0.5s TTFB, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test,
# control kotobase.net/signup. secret 不含 (curl only, no credentials).
import subprocess, json, math, sys

SEARCH = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"

def probe(url):
    # fresh curl process = separate connection (別接続)
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer}", "--max-time", "30", url],
        capture_output=True, text=True)
    out = r.stdout.strip()
    if not out:
        return None
    code, ttfb = out.split(" ", 1)
    return (code, float(ttfb))

def nearest_rank_p50(vals):
    # nearest-rank percentile (1-based index = ceil(0.5 * n))
    if not vals:
        return None
    s = sorted(vals)
    idx = max(1, math.ceil(0.5 * len(s)))
    return s[idx - 1]

def summarize(name, samples):
    n = len([s for s in samples if s is not None])
    codes = [s[0] for s in samples if s is not None]
    ttfb = [s[1] for s in samples if s is not None]
    cold = [t for t in ttfb if t >= 0.5]
    warm = [t for t in ttfb if t < 0.5]
    return {
        "label": name, "count": n,
        "http_codes": {c: codes.count(c) for c in set(codes)},
        "cold_ge0.5s": len(cold), "cold_list": [round(t,4) for t in cold],
        "p50_all_s": round(nearest_rank_p50(ttfb), 4) if ttfb else None,
        "p50_warm_s": round(nearest_rank_p50(warm), 4) if warm else None,
        "max_s": round(max(ttfb), 4) if ttfb else None,
        "min_s": round(min(ttfb), 4) if ttfb else None,
    }

result = {}
for run in ["A", "B", "C"]:
    samples = []
    for i in range(20):
        samples.append(probe(SEARCH))
    result[f"run376{run}"] = summarize(f"run376{run}", samples)

ctrl = []
for i in range(20):
    ctrl.append(probe(CONTROL))
result["control"] = summarize("control(kotobase.net/signup)", ctrl)

sys.stderr.write(json.dumps(result, ensure_ascii=False, indent=1))
# also write file, terminal stdout unreliable
with open("/tmp/bench_run376_result.json", "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)