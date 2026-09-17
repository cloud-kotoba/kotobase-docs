import json, subprocess, statistics, time

def run(url, n=20):
    tt = []
    codes = []
    for i in range(n):
        out = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w",
                              "%{http_code} %{time_total}", "--max-time", "10", url],
                             capture_output=True, text=True).stdout.strip()
        parts = out.split()
        codes.append(parts[0])
        tt.append(float(parts[1]))
        time.sleep(0.2)
    return tt, codes

def stats(tt):
    s = sorted(tt)
    def pct(p):
        # nearest-rank
        import math
        idx = max(1, math.ceil(p / 100 * len(s)))
        return s[idx - 1]
    cold = [x for x in s if x >= 0.5]
    return {"p50": round(pct(50), 3), "p90": round(pct(90), 3),
            "max": round(s[-1], 3), "min": round(s[0], 3),
            "cold_n": len(cold), "cold_vals": [round(x, 3) for x in cold]}

results = {}
for label, url in [("search", "https://search.kotobase.net/search?q=test"),
                   ("landing", "https://kotobase.net/")]:
    for r in "ABC":
        if label == "landing" and r != "C":
            continue
        tt, codes = run(url, 20)
        results[f"{label}{r}"] = {"stats": stats(tt), "codes": codes}
        print(label + r, results[f"{label}{r}"]["stats"], "codes_ok", all(c == "200" for c in codes))
    # spacer between endpoints
    time.sleep(2)

with open("bench47_out.json", "w") as f:
    json.dump(results, f, indent=1)
print("all_200:", all(all(c == "200" for c in v["codes"]) for v in results.values()))
