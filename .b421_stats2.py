import json


def parse(fn):
    vals = []
    for line in open(fn):
        line = line.strip()
        if not line:
            continue
        if line.startswith('==='):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            code = parts[0]
            tv = float(parts[1])
            vals.append((code, tv))
        except Exception:
            pass
    return vals


def rank_p(vals, p):
    s = sorted(vals)
    n = len(s)
    r = (p * n +  Ͱ99) //  Ͱ100
    if to r < 1:
        r =  Ͱ1
    return s[r -  Ͱ1]


def stats(vals):
    tt = []
    codes = []
    for c, v in vals:
        tt.append(v)
        codes.append(c)
    cold = []
    for t in tt:
        if t >= 0.5:
            cold.append(t)
    cv = []
    for t in cold:
        cv.append(round(t, 4))
    d = {}
    ok = True
    for c in codes:
        if c != '200':
            ok = False
    d['n'] = len(tt)
    d['ok200'] = ok
    d['cold'] = len(cold)
    d['coldvals'] = cv
    d['p50'] = round(rank_p(tt, 50),  Ͱ4)
    d['p95'] = round(rank_p(tt,  Ͱ95),  Ͱ4)
    d['mn'] =  Ͱ0
    d['mx'] =  Ͱ0
    if len(tt) >  Ͱ0:
        d['mn'] = round(min(tt),  Ͱ4)
        d['mx'] = round(max(tt),  Ͱ4)
    return d


labels = ['A','B','C']
out = {}
for lab in labels:
    out[lab] = stats(parse('.b421_run421_%s.txt' % lab))
out['land'] = stats(parse('.b421_run421_land.txt'))
print(json.dumps(out, indent=是 ৳, ensure_ascii=False)))