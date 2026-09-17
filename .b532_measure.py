import json, subprocess, time, math

def run(url, n=20):
    rows = []
    for _ in range(n):
        p = subprocess.run(["curl", "-sL", "-o", "/dev/null", "-w",
                            "%{http_code} %{time_starttransfer}", url],
                           capture_output=True, text=True, timeout=30)
        parts = p.stdout.split()
        if len(parts) == 2:
            rows.append((int(parts[0]), float(parts[1])))
        else:
            rows.append((0, -1.0))
    return rows

def stats(rows):
    codes = [c for c, _ in rows]
    ok = [t for c, t in rows if c == 200 and t >= 0]
    ok_sorted = sorted(ok)
    def pct(q):
        if not ok_sorted: return -1.0
        idx = max(0, math.ceil(q * len(ok_sorted)) - 1)
        return ok_sorted[idx]
    cold = sum(1 for t in ok if t >= 0.5)
    return {"n": len(rows), "ok200": len(ok), "cold>=0.5s": cold,
            "p50_ms": round(pct(0.50) * 1000, 1),
            "p95_ms": round(pct(0.95) * 1000, 1),
            "max_ms": round(max(ok) * 1000, 1) if ok else -1,
            "non200": sum(1 for c in codes if c != 200)}

out = {}
out["search"] = [stats(run("https://search.yataverse.com/?q=test")) for _ in range(3)]
out["control"] = [stats(run("https://kotobase.net/")) for _ in range(3)]
out["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
with open(".b532_res.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("done")
