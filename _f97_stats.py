import re
lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f97_run226_out.txt').read().splitlines()
runs = {'A':[], 'B':[], 'C':[]}
control = []
for ln in lines:
    m = re.match(r'run226(\w) 200 ([\d.]+)', ln)
    if m:
        runs[m.group(1)].append(float(m.group(2)))
        continue
    m = re.match(r'control 200 ([\d.]+)', ln)
    if m:
        control.append(float(m.group(1)))
def stats(v):
    s = sorted(v)
    n = len(s)
    p50 = s[(n-1)//2] if n%2 else (s[n//2-1]+s[n//2])/2
    return n, p50, s[0], s[-1], sum(1 for x in s if x>=0.5)
for k in ['A','B','C']:
    n,p50,mn,mx,cold = stats(runs[k])
    print(f"run226{k}: n={n} p50={p50*1000:.1f}ms min={mn*1000:.1f} max={mx*1000:.1f} cold>={0.5}s={cold}")
n,p50,mn,mx,cold = stats(control)
print(f"control: n={n} p50={p50*1000:.1f}ms min={mn*1000:.1f} max={mx*1000:.1f} cold>={0.5}s={cold}")