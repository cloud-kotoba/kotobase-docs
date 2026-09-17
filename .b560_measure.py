import subprocess, json

URLS = [
    ("run", "https://search.kotobase.net/search?q=test"),
    ("control", "https://kotobase.net/signup"),
]
OUT = {}

for label, url in URLS:
    groups = []
    for gi in range(3):
        samples = []
        codes = []
        for i in range(20):
            r = subprocess.run(
                ["curl", "-sS", "-o", "/dev/null",
                 "-w", "%{http_code} %{time_starttransfer} %{time_total}",
                 url],
                capture_output=True, text=True, timeout=30)
            line = r.stdout.strip()
            try:
                code_s, ttfb_s, tt_s = line.split()
                code, ttfb, tt = int(code_s), float(ttfb_s), float(tt_s)
            except Exception:
                code, ttfb, tt = 0, -1.0, -1.0
            codes.append(code)
            samples.append((ttfb, tt))
        groups.append((codes, samples))
    OUT[label] = groups

def stats_for(samples):
    ttfbs = sorted(t for t, _ in samples)
    n = len(ttfbs)
    p50 = ttfbs[max(0, int(round(0.50 * n + 0.5)) - 1)]
    p95 = ttfbs[max(0, int(round(0.95 * n + 0.5)) - 1)]
    cold = sum(1 for t in ttfbs if t >= 0.5)
    return cold, p50, p95, max(ttfbs)

report = {}
for label, groups in OUT.items():
    all_codes = []
    all_samples = []
    per = []
    for gi, (codes, samples) in enumerate(groups):
        all_codes.extend(codes)
        all_samples.extend(samples)
        cold, p50, p95, mx = stats_for(samples)
        per.append({"g": gi + 1, "n": len(samples), "non200": sum(1 for c in codes if c != 200),
                    "cold": cold, "p50_ms": round(p50 * 1000, 1), "p95_ms": round(p95 * 1000, 1),
                    "max_ms": round(mx * 1000, 1)})
    cold, p50, p95, mx = stats_for(all_samples)
    report[label] = {"non200_total": sum(1 for c in all_codes if c != 200),
                     "n_total": len(all_samples), "cold_total": cold,
                     "p50_ms": round(p50 * 1000, 1), "p95_ms": round(p95 * 1000, 1),
                     "max_ms": round(mx * 1000, 1), "per": per}

with open(".b560_result.json", "w") as f:
    json.dump(report, f, indent=1)
