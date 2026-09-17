import re, statistics as st
out="_f104_run235_out.txt"
runs={"run235A":[],"run235B":[],"run235C":[],"control":[]}
for line in open(out,encoding="utf-8"):
    line=line.strip()
    m=re.match(r"(run235[ABC]|control) (\d+) ([\d.]+)$",line)
    if not m: continue
    key,code,t=m.groups()
    if code!="200": 
        print(f"non200 {key} {code}"); continue
    runs[key].append(float(t))
def stats(v):
    v=sorted(v)
    return v, low(v,0.5), max(v)
def low(v,th):
    return sum(1 for x in v if x>=th)
for k in ["run235A","run235B","run235C","control"]:
    v=runs[k]
    n=len(v)
    cold=sum(1 for x in v if x>=0.5)
    warm=[x for x in v if x<0.5]
    p50=st.median(v)
    wp50=st.median(warm) if warm else None
    print(f"{k}: n={n} cold={cold}/20 p50_total={p50*1000:.1f}ms warm_p50={wp50*1000:.1f}ms min={min(v)*1000:.1f} max={max(v)*1000:.1f}")
    # list cold vals
    cvals=sorted([x for x in v if x>=0.5])
    if cvals: print(f"   cold_vals: {[round(x,4) for x in cvals]}")
tot=sum(1 for k in ["run235A","run235B","run235C"] for x in runs[k] if x>=0.5)
print(f"search total cold = {tot}/60")
cc=sorted([x for x in runs['control']])
print("control sorted:", [round(x,3) for x in cc])
print("control cold:", sum(1 for x in cc if x>=0.5))