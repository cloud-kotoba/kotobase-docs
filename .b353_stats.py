import re

data = {}
cur = None
with open("/tmp/b353_out.txt") as f:
    for line in f:
        line = line.strip()
        m = re.match(r"===\s*(.+?)\s*===", line)
        if m:
            cur = m.group(1); data[cur] = []
            continue
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            code = parts[0]
            val_ms = float(parts[1].lstrip('0') or '0')  # ms with fraction
            data[cur].append(val_ms)

for tag, vals in data.items():
    n20 = vals[:20]
    n = len(n20)
    cold = [v for v in n20 if v >= 500.0]
    s = sorted(n20)
    p50 = s[min(n-1, int(0.5*n))]  # nearest-rank
    mx = max(n20)
    print(f"{tag}: n={n} cold(>=500ms)={len(cold)}/20 p50={p50:.1f}ms max={mx:.1f}ms")
    if cold:
        print("   cold values:", ", ".join(f"{v:.1f}" for v in cold))