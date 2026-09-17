import re, statistics
lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f94_run223_out.txt').read().splitlines()
search=[]; control=[]
for ln in lines:
    m = re.match(r'(run\d+[ABC]|control)\s+(\d+)\s+([\d.]+)', ln)
    if not m: continue
    tag, code, t = m.group(1), int(m.group(2)), float(m.group(3))
    if tag=='control': control.append(t)
    else: search.append(t)
def stats(x):
    x=sorted(x)
    return dict(n=len(x), p50=x[len(x)//2], p90=x[int(len(x)*0.9)-1], max=x[-1],
                gt05=sum(1 for v in x if v>0.5), gt1=sum(1 for v in x if v>1.0))
print("SEARCH", stats(search))
print("CONTROL", stats(control))