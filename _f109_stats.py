lines = open('_f109_run243_out.txt').read().splitlines()
series = {'run243A':[], 'run243B':[], 'run243C':[], 'control':[]}
cold = {'run243A':0, 'run243B':0, 'run243C':0, 'control':0}
for ln in lines:
    p = ln.split()
    if len(p) != 3:
        print("SKIP:", repr(ln)); continue
    key, code = p[0], p[1]
    try: t = float(p[2])
    except: print("FLOATFAIL:", repr(ln)); continue
    if code != '200': print("NON200:", repr(ln)); continue
    if key in series:
        series[key].append(t)
        if t >= 0.5: cold[key]+=1
    else:
        print("UNKNOWNKEY:", repr(ln))
for k in ['run243A','run243B','run243C','control']:
    v = sorted(series[k])
    print(f"{k}: n={len(v)} cold={cold[k]}/20")
for k in ['run243A','run243B','run243C','control']:
    v = sorted(series[k])
    if not v: continue
    p50 = v[len(v)//2]
    print(f"{k}: p50={p50*1000:.1f}ms max={max(v)*1000:.1f}ms all={[round(x*1000,1) for x in v]}")
tot = sum(cold[k] for k in ['run243A','run243B','run243C'])
print(f"TOTAL cold {tot}/60 = {tot/60*100:.1f}%")