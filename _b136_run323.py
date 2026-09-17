import subprocess, time, json, datetime, math

ENDPOINT = "https://search.kotobase.net/search?q=test"
CONTROL = "https://kotobase.net/signup"
GROUPS = ["run323A", "run323B", "run323C"]
N = 20
COLD_THRESH = 0.5  # seconds TTFB

def probe(url):
    # separate connection: each curl is a fresh invocation, no connection reuse
    p = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{time_starttransfer}",
         "--max-time", "15", url],
        capture_output=True, text=True, timeout=30,
    )
    out = p.stdout.strip()
    try:
        code, tt = out.split()
        tt = float(tt)
    except Exception:
        code, tt = "ERR", None
    return code, tt

def pct(sorted_vals, p):
    k = max(1, math.ceil(p / 100 * len(sorted_vals)))
    return sorted_vals[k - 1]

def collect(name, url):
    times, codes = [], []
    for i in range(1, N + 1):
        code, tt = probe(url)
        codes.append(code)
        times.append(tt if tt is not None else 999.0)
        time.sleep(0.15)
    st = sorted(times)
    cold = [t for t in times if t >= COLD_THRESH]
    rec = {
        "n": len(times),
        "ok200": sum(1 for c in codes if c == "200"),
        "p50": round(pct(st, 50) * 1000, 1),
        "p95": round(pct(st, 95) * 1000, 1),
        "max_ms": round(st[-1] * 1000, 1),
        "cold_count": len(cold),
        "cold_times": [round(t, 4) for t in cold],
        "start": datetime.datetime.now().astimezone().isoformat(),
    }
    return rec

results = {}
allcolds, alln = 0, 0
for g in GROUPS:
    rec = collect(g, ENDPOINT)
    results[g] = rec
    allcolds += rec["cold_count"]
    alln += rec["n"]
    time.sleep(2)

results["ctrl"] = collect("ctrl_signup", CONTROL)
results["total_cold"] = allcolds
results["total_n"] = alln

with open("_b136_run323.json", "w") as f:
    json.dump(results, f, indent=1)
for k in ["run323A", "run323B", "run323C", "ctrl", "total_cold", "total_n"]:
    print(k, json.dumps(results[k]))