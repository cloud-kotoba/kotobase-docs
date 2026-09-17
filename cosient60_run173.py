import subprocess, time, math, json

def run_series(url, n=20):
    results = []
    for i in range(n):
        r = subprocess.run(
            ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code} %{time_total} %{time_starttransfer}",
             "--max-time", "20", url],
            capture_output=True, text=True)
        parts = r.stdout.split()
        if len(parts) == 3 and parts[0] == "200":
            results.append((float(parts[1]), float(parts[2])))
        else:
            results.append((None, None, r.stdout, r.stderr[:200]))
        time.sleep(0.2)
    return results

def summarize(res):
    totals = sorted(t for t, _ in res if t is not None)
    cold = [(i + 1, round(t, 3)) for i, (t, _) in enumerate(res) if t is not None and t >= 0.5]
    p50 = totals[math.ceil(0.5 * len(totals)) - 1] if totals else None
    return {
        "n_ok": len(totals),
        "cold": cold,
        "p50": round(p50, 3) if p50 else None,
        "min": round(totals[0], 3) if totals else None,
        "max": round(totals[-1], 3) if totals else None,
    }

SEARCH = "https://search.kotobase.net/search?q=test"
LANDING = "https://kotobase.net/"

summary = {}
for tag, url in [("A", SEARCH), ("B", SEARCH), ("C", SEARCH), ("L", LANDING)]:
    res = run_series(url)
    summary[tag] = summarize(res)

with open("/tmp/cosient60_run173_out.txt", "w") as f:
    f.write(json.dumps(summary, ensure_ascii=False, indent=1))
print("done")
