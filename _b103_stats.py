import re
out = {}
cur = None
path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b103_run255_out.txt'
import datetime
for line in open(path):
    line=line.strip()
    m = re.match(r'^(run255[ABC]|control) (\d+) ([\d.]+)$', line)
    if m:
        out.setdefault(m.group(1), {'code':m.group(2),'t':[]})
        out[m.group(1)]['t'].append(float(m.group(3)))
    elif line.startswith('2026-') and len(line)<40:
        cur=line
    elif line.startswith('control 2'):
        pass
    elif 'load averages' in line and cur:
        print("tick", cur)
        print("load", line)
        cur=None

def pct(a,k):
    a=sorted(a); n=len(a); idx=int(((k/100.0)*n)+0.999999)-1
    if idx<0: idx=0
    if idx>=n: idx=n-1
    return a[idx]

for g,d in sorted(out.items()):
    t=d['t']; c=int(d['code'])
    cold=[x for x in t if x>=0.5]
    warm=[x for x in t if x<0.5]
    wp50 = pct(warm,50) if warm else 0
    print("%s: n=%d 200=%d cold(>=0.5)=%d/%d p50=%.4f warm_p50=%.4f p90=%.4f max=%.4f" % (
        g, len(t), c, len(cold), len(t), pct(t,50), wp50, pct(t,90), max(t)))
    if cold: print("   cold vals: %s (positions)" % ["%.4f"%x for x in cold])