import subprocess, time, json

N = 20
SEARCH = "https://search.kotobase.net/search?q=test"
LANDING = "https://kotobase.net/"

def run_seq(url, n=N):
    res = []
    for _ in range(n):
        r = subprocess.run(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{http_code} %{time_starttransfer}", url],
            capture_output=True, text=True, timeout=30)
        parts = r.stdout.split()
        res.append({"code": int(parts[0]), "ttfb": float(parts[1])})
    return res

out = {"time": time.strftime("%Y-%m-%d %H:%M:%S JST"), "data": {}}
for tag, url in (("A", SEARCH), ("B", SEARCH), ("C", SEARCH), ("landing", LANDING)):
    out["data"][tag] = run_seq(url)
open("bench42_raw_data.json", "w").write(json.dumps(out))
