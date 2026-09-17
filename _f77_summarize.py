import re, statistics

lines = open("_f77_run198_out.txt").read().splitlines()
res = {}
ctrl = []
cur = None
for ln in lines:
    m = re.match(r"== run198(\w) ==", ln)
    if m:
        cur = m.group(1); res[cur] = []
        continue
    if ln.startswith("== control"):
        cur = "CTRL"; continue
    m = re.match(r"(\d+) ([\d.]+)", ln)
    if m and cur:
        (res[cur] if cur != "CTRL" else ctrl).append((int(m.group(1)), float(m.group(2))))

def summarize(vals):
    codes = [c for c, t in vals]
    times = [t for c, t in vals if c == 200]
    p50 = statistics.median(times) * 1000
    mx = max(times) * 1000
    cold = sum(1 for t in times if t >= 0.5)
    return f"200:{codes.count(200)}/{len(codes)} cold(>=0.5s):{cold} p50:{p50:.0f}ms max:{mx:.0f}ms"

for k in ["A", "B", "C"]:
    print(f"run198{k}: {summarize(res[k])}")
print(f"control: {summarize(ctrl)}")
