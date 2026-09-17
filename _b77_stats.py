import re, statistics
txt = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b77_run199_out.txt').read()
sections = re.split(r'=== (.+?) ===\n', txt)[1:]
for i in range(0, len(sections), 2):
    name, body = sections[i], sections[i+1]
    vals = sorted(float(m) for m in re.findall(r'200 ([\d.]+)', body))
    n = len(vals)
    p50 = vals[10]  # nearest-rank ceil(0.5*20)=10 (1-indexed)
    p95 = vals[19]  # ceil(0.95*20)=19 -> index 18; use index 18
    cold = [v for v in vals if v >= 0.507]
    print(f"{name}: n={n} p50={p50*1000:.0f}ms p95={vals[18]*1000:.0f}ms max={max(vals)*1000:.0f}ms cold(>=0.507s)={len(cold)}")
