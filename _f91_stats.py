import sys

def pct(vals, p):
    # nearest-rank percentile
    s = sorted(vals)
    k = int(p/100.0*len(s))
    if k==0: k=1
    if k>len(s): k=len(s)
    return s[k-1]

def summarize(name, vals):
    c = len(vals)
    cold = [v for v in vals if v >= 0.5]
    warm = [v for v in vals if v < 0.5]
    warmp50 = pct(warm,50) if warm else None
    warmp95 = pct(warm,95) if warm else None
    maxv = max(vals) if vals else None
    print("%s n=%d cold(%s>=0.5)=%d p50=%s p95=%s max=%s" % (
        name, c, c, len(cold),
        ("%.1fms" % (warmp50*1000)) if warmp50 is not None else "-",
        ("%.1fms" % (warmp95*1000)) if warmp95 is not None else "-",
        ("%.1fms" % (maxv*1000)) if maxv is not None else "-"))
    return cold

runs = {'A':[], 'B':[], 'C':[]}
control = []
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        tag, code = parts[0], parts[1]
        tt = float(parts[2]) if len(parts)>2 else None
        if tt is None: continue
        if tag.startswith('run218') and code=='200':
            runs[tag[-1]].append(tt)
        elif tag=='control' and code=='200':
            control.append(tt)

allcold=0
for k in ['A','B','C']:
    c=summarize('run218'+k, runs[k])
    allcold+=len(c)
summarize('control', control)
print("total cold = %d/60" % allcold)