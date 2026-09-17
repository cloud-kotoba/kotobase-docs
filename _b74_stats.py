import re

src = open("_b74_run194_out.txt").read()
blocks = re.findall(r"=== (run194[ABC]) search ===\n((?:\d+ [\d.]+\n)+)", src)
m_ctrl = re.search(r"=== landing control ===\n((?:\d+ [\d.]+\n)+)", src)

def stats(lines):
    vals = []
    cold = 0
    codes = []
    for ln in lines.strip().splitlines():
        code, t = ln.split()
        codes.append(code)
        t = float(t)
        vals.append(t)
        if t >= 0.5:
            cold += 1
    vals.sort()
    n = len(vals)
    p50 = vals[max(0, int(0.50 * n + 0.5) - 1)]
    mx = vals[-1]
    warm_sorted = sorted(v for v in vals if v < 0.5)
    wp50 = warm_sorted[max(0, int(0.50 * len(warm_sorted) + 0.5) - 1)] if warm_sorted else None
    return cold, p50, wp50, mx, codes

for name, body in blocks:
    cold, p50, wp50, mx, codes = stats(body)
    ok = codes.count("200")
    print(f"{name}: 200 {ok}/20, cold {cold}/20, p50 {p50*1000:.0f}ms, warm p50 {wp50*1000:.0f}ms, max {mx*1000:.0f}ms")
if m_ctrl:
    cold, p50, wp50, mx, codes = stats(m_ctrl.group(1))
    ok = codes.count("200")
    print(f"control: 200 {ok}/20, cold {cold}/20, p50 {p50*1000:.0f}ms, max {mx*1000:.0f}ms")
tail = src.split("=== landing control ===")[-1]
print(tail.strip().splitlines()[-2:])
