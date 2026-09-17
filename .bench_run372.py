#!/usr/bin/env python3
# bench run372: K-Z3 16hr(9/7) n-add measurement
# method: 同測定法 n=20 x 3 search + n=20 landing control,
# separate curl connections (別接続), cold>=0.5s, nearest-rank p50
# secret 不含 (curl only, no credentials)
import subprocess, time, sys, json

SEARCH = "https://search.kotobase.net/search?q=test"
CTRL   = "https://kotobase.net/signup"

def timed_curl(url):
    # single curl per request (separate connection), measure TTFB via time_starttransfer
    out = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w",
         "%{http_code}|%{time_starttransfer}|%{time_total}", url],
        capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        return None, out.stderr.strip()[:80]
    try:
        code, ttf, tt = out.stdout.strip().split("|")
        return {"code": int(code), "ttfb": float(ttf), "total": float(tt)}, None
    except Exception as e:
        return None, f"parse:{out.stdout.strip()[:80]}"

def run_set(name, url, n):
    res = []
    for i in range(n):
        r, err = timed_curl(url)
        if r is None:
            res.append({"idx": i, "err": err})
        else:
            res.append({"idx": i, **r})
        time.sleep(0.05)
    return res

def analyze(tag, results):
    ok = [r for r in results if r.get("code") == 200]
    cold = [r for r in ok if r["ttfb"] >= 0.5]
    n_ok = len(ok)
    n_cold = len(cold)
    # nearest-rank p50 of ttfb across all ok
    ttfbs = sorted(r["ttfb"] for r in ok)
    p50 = ttfbs[(n_ok + 1) // 2 - 1] if ttfbs else None  # nearest-rank
    maxv = ttfbs[-1] if ttfbs else None
    cold_vals = sorted(r["ttfb"] for r in cold)
    return {
        "tag": tag, "n": len(results), "ok": n_ok, "cold": n_cold,
        "p50": round(p50, 4) if p50 else None,
        "max": round(maxv, 4) if maxv else None,
        "cold_vals": [round(v, 4) for v in cold_vals],
        "errs": [r.get("err") for r in results if "err" in r][:5],
    }

def main():
    out = {}
    # 3 search runs x 20
    for lbl in ["A", "B", "C"]:
        tag = f"run372{lbl}"
        res = run_set(tag, SEARCH, 20)
        out[tag] = analyze(tag, res)
        print(json.dumps(out[tag]), flush=True)
    # landing control
    res = run_set("run372CTRL", CTRL, 20)
    out["run372CTRL"] = analyze("run372CTRL", res)
    print(json.dumps(out["run372CTRL"]), flush=True)
    with open("/tmp/bench_run372_out.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()