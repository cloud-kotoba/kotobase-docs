import os

def stats(path):
    codes = []
    vals = []
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        codes.append(parts[0])
        vals.append(float(parts[1]))
    ok = [v for c, v in zip(codes, vals) if c == "200"]
    n = len(ok)
    if n == 0:
        return f"200 0/{len(codes)} n=0 INVALID (non-200: 404 endpoint dead)"
    s = sorted(ok)
    p50 = s[max(0, -(-n // 2) - 1)]
    p95 = s[max(0, -(-n * 95 // 100) - 1)]
    cold = sum(1 for v in ok if v >= 0.5)
    return f"200 {n}/{len(codes)} cold {cold}/{n} p50 {p50*1000:.1f}ms p95 {p95*1000:.1f}ms max {max(s)*1000:.1f}ms"

base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_raw.txt.tag."
out = []
for t in ["A", "B", "C", "CTRL"]:
    out.append(t + ": " + stats(base + t + ".trim"))
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_stats.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
