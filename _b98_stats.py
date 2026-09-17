lines = open('_b98_run244_out.txt').read().splitlines()
series = {'run244A':[], 'run244B':[], 'run244C':[], 'control':[]}
cold = {'run244A':0, 'run244B':0, 'run244C':0, 'control':0}
for ln in lines:
    p = ln.split()
    if len(p) != 3:
        print("SKIP:", repr(ln)); continue
    key, code = p[0], p[1]
    try:
        t = float(p[2])
    except:
        print("FLOATFAIL:", repr(ln)); continue
    if code != '200':
        print("NON200:", repr(ln)); continue
    if key in series:
        series[key].append(t)
        if t >= 0.5: cold[key]+=1
    else:
        print("UNKNOWNKEY:", repr(ln))
for k in ['run244A','run244B','run244C','control']:
    v = sorted(series[k])
    print(f"{k}: n={len(v)} cold={cold[k]}/20")
for k in ['run244A','run244B','run244C','control']:
    v = sorted(series[k])
    if not v: continue
    p50 = v[len(v)//2]
    print(f"{k}: p50={p50*1000:.1f}ms max={max(v)*1000:.1f}ms all={[round(x*1000,1) for x in v]}")