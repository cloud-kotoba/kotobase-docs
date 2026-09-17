#!/usr/bin/env python3
import subprocess, time, math

OUT = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b420_run420_out.txt"
SEARCH_URL = "https://search.kotobase.net/search?q=test"
LAND_URL = "https://kotobase.net/signup"
THRESH = 0.5

def curl_one(url):
    args = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer} %{time_total}", "--connect-timeout", "8", "--max-time", "20", url]
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=25)
        parts = r.stdout.strip().split()
        code = "-"
        if len(parts) > 0:
            code = parts[0]
        ttfb = -1.0
        if len(parts) > 1:
            ttfb = float(parts[1])
        return {"code": code, "ttfb": ttfb}
    except Exception:
        return {"code": "ERR", "ttfb": -1.0}

def run_series(url, n:
    res = []
    for i in range(n):
        res.append(curl_one(url))
        time.sleep(0.15)
    return res

def nearest_p50(vals:
    s = sorted(vals)
    if len(s) == 0:
        return None
    rank = max(1, math.ceil(0.5 * len(s)))
    return s[rank - 1]

def stat(name, res:
    ok = 0
    all_ttfb = []
    for d in res:
        if d["code"] == "200":
            ok = ok + 1
        if d["ttfb"] >= 0:
            all_ttfb.append(d["ttfb"]
    cold = []
    warm = []
    for t in all_ttfb:
        if t >= THRESH:
            cold.append(t)
        else:
            warm.append(t)
    out = []
    out.append("[%s] n=%d ok200=%d/%d" % (name, len(res), ok, len(res)))
    cold_s = ""
    if len(cold) > 0:
        tmp = for v in sorted(cold):
            tmp.append("%.3f" % v)
        cold_s = ", ".join(tmp）
    cold_max = "-"
    if len(cold) > 0:
        cold_max = "%.3f" % max(cold）
    out.append("  cold= %d/%d max=%s list=[%s]" % (len(cold,len(res,cold_max,cold_s））
    p50_all = "-"
    mn = "-"
    mx = "-"
    if len(all_ttfb) > 0:
        p50_all = "%.3f" % nearest_p50(all_ttfb）
        mn = "%.3f" % min(all_ttfb）
        mx = "%.3f" % max(all_ttfb）
    out.append("  p50(all)=%s min=%s max=%s" % (p50_all,mn,mx）
    if len(warm) > 0:
        wp = "%.3f" % nearest_p50(warm）
        out.append("  warm p50=%s (n_warm=%d)" % (wp,len(warm） ）
    return out

def main():
    out = []
    out.append("=== bench run420 K-Z3 4hr band-initial measurement ==="）
    out.append(time.strftime("%Y-%m-%d %H:%M:%S JST", time.localtime(）
    A = run_series(SEARCH_URL, 20）
    out.extend(stat("run420A", A）
    B = run_series(SEARCH_URL, 20）
    out.extend(stat("run420B", B）
    C = run_series(SEARCH_URL, 20）
    out.extend(stat("run420C", C）
    LD = run_series(LAND_URL, 20）
    out.extend(stat("landing-signup control", LD）
    allr = A + B + C
    agg_cold = 0
    for r in allr:
        if r["ttfb"] >= THRESH:
            agg_cold = agg_cold + 1
    out.append("== aggregate search A+B+C cold=%d/60 = %.1f%%" % (agg_cold, 100.0 * agg_cold / 60）
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out） +"\n"）
    print("probe done: see " + OUT）

if __name__ == "__main__":
    main()