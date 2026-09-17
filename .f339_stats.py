import statistics, sys

def stats(path, label):
    vals=[]; codes={}; colds=[]
    for line in open(path):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        code, t = parts[0], float(parts[1])
        codes[code]=codes.get(code,0)+1
        vals.append(t)
        if t>=0.5: colds.append(t)
    vals_sorted=sorted(vals)
    p50=vals_sorted[len(vals_sorted)//2]
    mx=max(vals)
    print(f"{label}: n={len(vals)} codes={codes} cold(>=0.5s)={len(colds)}/{len(vals)} {sorted(round(c,3) for c in colds)} p50={p50:.3f}s max={mx:.3f}s")
    return len(colds), len(vals)

for l in ['A','B','C']:
    stats(f'.f339_339{l}.txt', f'run339{l}')
stats('.f339_land.txt', 'control')