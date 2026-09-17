import re, statistics

f = "_co_run243_out.txt"
data = {}
for line in open(f):
    parts = line.split()
    if len(parts) != 3:
        continue
    tag = parts[0]
    code = parts[1]
    dt = float(parts[2])
    if code != "200":
        print("NON-200:", line.strip())
    data.setdefault(tag, []).append(dt)

for tag in ["run243A","run243B","run243C","control"]:
    xs = sorted(data[tag])
    cold = [x for x in xs if x >= 0.5]
    n = len(xs)
    def pct(p):
        k = max(1, int((p/100.0)*n))
        return xs[k-1]
    p50 = pct(50)
    print(f"{tag}: n={n} cold={len(cold)} p50={p50*1000:.1f}ms min={xs[0]*1000:.1f} max={xs[-1]*1000:.1f} cold_vals={[round(c,3) for c in cold]}")