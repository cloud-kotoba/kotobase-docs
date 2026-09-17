#!/usr/bin/env python3
# bench K-Z3 16時台(9/8) n-add run480A-C -- bench 第215回
# 同測定法: n=20 x 3 run + landing control, 別接続 curl (each fresh curl process),
# cold>=0.5s TTFB, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test,
# control kotobase.net/signup. secret 不含 (curl only, no credentials).
import subprocess, json, math, sys, time

SEARCH = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"

def probe(url):
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer}", "--max-time", "30", url],
        capture_output=True, text=True)
    out = r.stdout.strip()
    if not out:
        return None
    code, ttfb = out.split(" ", 1)
    return (code, float(ttfb))

def nearest_rank_p50(vals):
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
    pos = []
    cpos = 0
    for s in samples:
        if s is not None:
            cpos += 1
            if s[1] >= 0.5:
                pos.append(cpos)
    return {
        "label": name, "count": n,
        "http_codes": {c: codes.count(c) for c in set(codes)},
        "cold_ge0.5s": len(cold), "cold_list": [round(t,4) for t in cold], "cold_pos": pos,
        "p50_all_s": round(nearest_rank_p50(ttfb),4) if ttfb else None,
        "p50_warm_s": round(nearest_rank_p50(warm),4) if warm else None,
        "max_s": round(max(ttfb),4) if ttfb else None,
    }

result = {"time_start": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
for run in ["A", "B", "C"]:
    samples = []
    for i in range(20):
        samples.append(probe(SEARCH))
    result["run480" + run] = summarize("run480" + run, samples)

ctrl = []
for i in range(20):
    ctrl.append(probe(CONTROL))
result["control"] = summarize("control(kotobase.net/signup)", ctrl)
result["time_end"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")

sys.stderr.write(json.dumps(result, ensure_ascii=False, indent=1))
with open("/tmp/bench_run480_result.json", "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)