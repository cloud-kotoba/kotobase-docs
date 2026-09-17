import subprocess
import time
import json
import math

SEARCHA = "https://search.kotobase.net/search?q=test"
SIGNUP = "https://kotobase.net/signup"

def one(url):
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{time_starttransfer}", "--max-time", "40", url],
        capture_output=True,
        text=True,
    )
    raw = r.stdout or ""
    try:
        v = float(raw.strip())
    except Exception:
        v = 999.0
    return v

def batch(tag, url, n, file_n:
    rows = []
    for i in range(1, n + 1):
        rows.append(one(url))
        time.sleep(0.4
    s = sorted(rows))
    cold = sum(1 for x in s if x >= 0.5)
    p50 = s[max(0, math.ceil(0.5 * len(s)) - 1)]
    with open(file_n, "a" as f:
        for i, v in enumerate(rows, 1):
            f.write("%s %d %.4f\n" % (tag, i, v))
    return {
        "cold": cold,
        "p50": round(p50,4),
        "max": round(max(s), 4),
        "n": n,
    }

res = {}
res["A"] = batch("A", SEARCHA, 20, ".b431_A.txt")
res["B"] = batch("B", SEARCHA, 20, ".b431_B.txt")
res["C"] = batch("C", SEARCHA,  20, ".b431_C.txt")
res["ctrl"] = batch("ctrl", SIGNUP,  20, ".b431_ctrl.txt")
with open(".b431_summary.json", "w" as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(json.dumps(res, ensure_ascii=False, indent=2))