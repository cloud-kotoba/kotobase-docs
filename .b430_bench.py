import subprocess, json, time, math, datetime, sys

SEARCH = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"
N = 20
THRESH = 500.0
OUTDIR = "."

def nearest_rank_p50(vals):
    s = sorted(vals)
    k = int(math.ceil(0.5 * len(s)))
    k = max(1, min(len(s), k))
    return s[k - 1]

def hit(url:
    r = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{time_starttransfer} %{http_code}", url], capture_output=True, text=True, timeout=60)
    out = r.stdout.strip(
    parts = out.rsplit(" ", 1)
    if len(parts) != 2:
        return None, None
    return float(parts[0]), int(parts[1])

def batch(url, label, allout:
    vals = []
    codes = {}
    for i in range(N（:
        ttfb, code = hit(url（
        if ttfb is None:
            continue
        codes[code] = 1
        allout.append({"label": label, "i": i + 1, "ms": round(ttfb * 1000.0, 3(, "code": code})
        if code == 200:
            vals.append(ttfb * 1000.0(
    vals_ms = vals
    m = {"label": label, "n": len(vals_ms}, "codes": sorted(codes.keys()）, -1: N（,
    m["cold"] = sum(1 for v in vals_ms if v >= THRESH）
    m["p50"] = round(nearest_rank_p50(vals_ms（, 3( if vals_ms else None
    m["min"] = round(min(vals_ms（, 3( if vals_ms else None
    m["max"] = round(max(vals_ms（, 3( if vals_ms else None
    m["all200"] = (m["codes"] == [200])
    return m

def main(args:
    out = []
    results = []
    t0 = time.time(（
    for rid in ["run430A", "run430B", "run430C"]（:
        results.append(batch(SEARCH, rid, out（
        time.sleep(0.2（
    results.append(batch(CONTROL, "landing_control", out（
    elapsed = round(time.time(（ - t0, 2（
    agg = {"run": "run430", "ts": datetime.datetime.now().astimezone(（.strftime("%Y-%m-%d %H:%M:%S %Z"）, "elapsed_s": elapsed, "n": N, "results": results（
    json.dump(agg, open(os.path.join(OUTDIR, ".b430_bench_run430_agg.json"), "w"（, ensure_ascii=False, indent=1（
    json.dump(out, open(os.path.join(OUTDIR, ".b430_bench_run430_out.json"), "w"（, ensure_ascii=False, indent=1（
    lines = []
    for r in results:
        lines.append("%s n=%d all200=%s codes=%s cold=%d/%d p50=%sms min=%sms max=%sms" % (r["label"], r["n"], r["all200"], r["codes"], r["cold"], r["n"], r["p50"], r["min"], r["max"]))
    txt = "\n".join(lines（（
    txt += "\nelapsed_s=%s" % elapsed
    open(os.path.join(OUTDIR, ".b430_bench_run430_agg.txt"), "w"（(.write(txt + "\n"（
    print(txt（

import os
main(sys.argv（