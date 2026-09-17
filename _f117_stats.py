import re, statistics
out = {}
cur = None
for line in open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f117_run256_out.txt'):
    line=line.strip()
    m = re.match(r'^(run256[ABC]|control) (\d+) ([\d.]+)$', line)
    if m:
        out.setdefault(m.group(1), {'code':m.group(2),'t':[]})
        out[m.group(1)]['t'].append(float(m.group(3)))

def pct(a,k):
    a=sorted(a); n=len(a); idx=int(((k/100.0)*n)+0.999999)-1
    if idx<0: idx=0
    if idx>=n: idx=n-1
    return a[idx]

r=[]
for g,d in sorted(out.items()):
    t=d['t']; c=int(d['code'])
    cold=[x for x in t if x>=0.5]
    r.append("%s: n=%d 200=%d cold(>=0.5)=%d/%d p50=%.3f p90=%.3f max=%.3f%s" % (
        g, len(t), c, len(cold), len(t), pct(t,50), pct(t,90), max(t),
        (" cold=%s" % ["%.3f"%x for x in cold]) if cold else ""))
with open('/tmp/f117_stats.txt','w') as f:
    f.write("\n".join(r)+"\n")
print("OK")