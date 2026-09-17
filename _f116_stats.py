import re, statistics
out = {}
cur = None
for line in open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f116_run253_out.txt'):
    line=line.strip()
    m = re.match(r'^(run253[ABC]|control) (\d+) ([\d.]+)$', line)
    if m:
        out.setdefault(m.group(1), {'code':m.group(2),'t':[]})
        out[m.group(1)]['t'].append(float(m.group(3)))

def pct(a,k):
    a=sorted(a); n=len(a); idx=int(((k/100.0)*n)+0.999999)-1
    if idx<0: idx=0
    if idx>=n: idx=n-1
    return a[idx]

for g,d in sorted(out.items()):
    t=d['t']; c=int(d['code'])
    cold=[x for x in t if x>=0.5]
    print("%s: n=%d 200=%d cold(>=0.5)=%d/%d p50=%.4f p90=%.4f max=%.4f" % (
        g, len(t), c, len(cold), len(t), pct(t,50), pct(t,90), max(t)))
    if cold: print("   cold vals: %s" % ["%.4f"%x for x in cold])

# band totals commentary
print("\n22時台通算 (run172/173/174 09-05 + run252 + 本tick run253): cold = 5+1+1+9+2 = 18 / 300 = %.1f%%" % (18.0/300*100))