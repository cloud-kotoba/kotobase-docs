import io, json, subprocess, time, datetime

BASE = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/"
N = 20
WARMUP = 0  # falsify/bench K-Z2/K-Z3 runs use n=20 direct, no warmup exclusion
COLD_MS = 500.0

def nearest_rank(sorted_s, p):
    return sorted_s[max(0, -(-int(p*len(sorted_s))//1) - 1)] if False else sorted_s[max(0, int(-(-p*len(sorted_s)//1)) - 1)]

# curl -w times, separate connection each request
def curl_time(url):
    fmt = "%{time_starttransfer} %{time_total} %{http_code}"
    r = subprocess.run(["/usr/bin/curl", "-s", "-o", "/dev/null", "-w", fmt, "--max-time", "10", url],
                       capture_output=True, text=True)
    parts = r.stdout.strip().split()
    return float(parts[0]), float(parts[1]), int(parts[2])

runs = []
for name, url in [("search", BASE), ("control", CONTROL)]:
    ttfbs = []
    codes = []
    for i in range(N):
        ttfb, total, code = curl_time(url)
        ttfbs.append(ttfb)
        codes.append(code)
        time.sleep(0.2)
    cold = [t for t in ttfbs if t >= 0.5]
    warm = sorted(t for t in ttfbs if t < 0.5)
    s = sorted(ttfbs)
    runs.append({
        "name": name, "n": N,
        "codes_ok": sum(1 for c in codes if c == 200),
        "cold_count": len(cold),
        "cold_range": [min(cold), max(cold)] if cold else None,
        "warm_count": len(warm),
        "p50_all": s[N//2 - 1],
        "warm_p50": nearest_rank(warm, 0.5) if len(warm) >= 2 else None,
        "warm_min": min(warm) if warm else None,
        "warm_max": max(warm) if warm else None,
        "ttfbs": ttfbs,
    })

load = subprocess.run(["/usr/bin/uptime"], capture_output=True, text=True).stdout.strip()
now = datetime.datetime.now().astimezone().strftime("%H:%M:%S")
out = {"time": now, "load": load, "runs": runs}
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench37_out.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in out.items() if k != "runs"}, ensure_ascii=False))
for r in runs:
    print(r["name"], "ok=%d/%d" % (r["codes_ok"], r["n"]), "cold=%d/%d" % (r["cold_count"], r["n"]),
          "cold_range=", r["cold_range"], "warm_p50=", r["warm_p50"], "p50_all=", r["p50_all"])
