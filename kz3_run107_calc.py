import re

src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run107_out.txt", encoding="utf-8").read().splitlines()
out = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run107_calc_out.txt", "w", encoding="utf-8")

runs = {}
cur = None
ctrl = []
for line in src:
    m = re.match(r"=== run(\S+) (direct-after|elapsed)", line)
    if m:
        cur = m.group(1) + "-" + m.group(2)
        runs[cur] = []
        continue
    if line.startswith("=== landing"):
        cur = "CTRL"
        continue
    m = re.match(r"(\d{3}) ([\d.]+)", line)
    if m and cur:
        (ctrl if cur == "CTRL" else runs[cur]).append((int(m.group(1)), float(m.group(2))))

def stats(name, samples):
    codes = [c for c, _ in samples]
    ts = sorted(t for _, t in samples)
    cold = [t for _, t in samples if t >= 0.5]
    n = len(ts)
    p50 = ts[n // 2] if n % 2 else (ts[n//2 - 1] + ts[n//2]) / 2
    out.write(f"{name}: n={n} non200={sum(1 for c in codes if c != 200)} cold(>=0.5s)={len(cold)} cold_vals={[round(t,3) for t in cold]} p50={p50:.3f}s min={ts[0]:.3f} max={ts[-1]:.3f}\n")
    return len(cold)

direct_cold = 0
elapsed_cold = 0
for name in sorted(runs):
    c = stats(f"run{name}", runs[name])
    if "direct" in name:
        direct_cold += 1 if c > 0 else 0
    else:
        elapsed_cold += 1 if c > 0 else 0
stats("landing-control", ctrl)
out.write(f"\nwindows: direct-after cold>0 {direct_cold}/2, elapsed cold>0 {elapsed_cold}/2\n")
out.close()
print("ok")
