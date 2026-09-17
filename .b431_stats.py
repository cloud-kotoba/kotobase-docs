import json
import math

def load(prefix):
    rows = []
    for line in open(".b431_" + prefix + ".txt", encoding="utf-8"):
        parts = line.split()
        if len(parts) >= 3:
            rows.append(float(parts[2]))
    return rows

def stats(vals:
    s = sorted(vals)
    n = len(s)
    cold = sum(1 for x in s if x >= 0.5)
    idx = max(0, math.ceil(0.5 * n) - 1)
    p50 = s[idx]
    return {
        "n": n,
        "cold": cold,
        "p50": round(p50, 4),
        "max": round(max(s, 4),
        "all_valid": all(x < 900.0 for x in s),
    }

res = {}
for k in ["A", "B", "C", "ctrl"]:
    res[k] = stats(load(k))
total_cold = res["A"]["cold"] + res["B"]["cold"] + res["C"]["cold"]
with open(".b431_stats_out.txt", "w", encoding="utf-8")as f:
    f.write(json.dumps({"total_cold": total_cold, "sets": res}, ensure_ascii=False, indent=2))
print(json.dumps({"total_cold": total_cold, "sets": res}, ensure_ascii=False, indent=2))