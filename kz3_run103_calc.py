import re, statistics

def parse(path):
    runs = {}
    cur = None
    ctrl = []
    mode = None
    for line in open(path):
        m = re.match(r"=== run(\S+) search ===", line)
        if m:
            cur = m.group(1); runs[cur] = []; mode = "s"; continue
        if line.startswith("=== landing control ==="):
            mode = "l"; continue
        m = re.match(r"(\d{3}) ([\d.]+)", line.strip())
        if m:
            code, t = int(m.group(1)), float(m.group(2))
            if mode == "s":
                runs[cur].append((code, t))
            elif mode == "l":
                ctrl.append((code, t))
    return runs, ctrl

runs, ctrl = parse("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run103_out.txt")
for rid, vals in sorted(runs.items()):
    codes = [c for c, _ in vals]
    ts = sorted(t for _, t in vals)
    cold = [t for _, t in vals if t >= 0.5]
    p50 = statistics.median(ts)
    print(f"run{rid}: n={len(vals)} ok={codes.count(200)}/{len(vals)} cold>=0.5s {len(cold)}/20 p50={p50:.3f}s min={ts[0]:.3f} max={ts[-1]:.3f} colds={[round(t,3) for t in cold]}")
codes = [c for c, _ in ctrl]
ts = sorted(t for _, t in ctrl)
cold = [t for _, t in ctrl if t >= 0.5]
print(f"landing control: n={len(ctrl)} ok={codes.count(200)}/{len(ctrl)} cold>=0.5s {len(cold)}/20 p50={statistics.median(ts):.3f}s min={ts[0]:.3f} max={ts[-1]:.3f} colds={[round(t,3) for t in cold]}")
