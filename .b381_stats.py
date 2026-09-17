#!/usr/bin/env python3
# stats for K-Z3 run381: per-file cold count (>=0.5s), p50 (nearest-rank), max.
import sys, statistics, json

def parse(fn):
    # lines: "<http_code> <time_starttransfer>"
    vals=[]; codes=[]
    for line in open(fn):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        codes.append(parts[0])
        vals.append(float(parts[1]))
    return codes, vals

def p50(vals):
    s=sorted(vals)
    # nearest-rank: smallest value s.t. rank >= ceil(0.5*n)
    import math
    n=len(s)
    if n==0: return None
    rank=math.ceil(0.50*n)
    return s[rank-1]

files = {
  "381A":".b381_381A.txt",
  "381B":".b381_381B.txt",
  "381C":".b381_381C.txt",
  "land":".b381_land.txt",
}
out={}
for k,fn in files.items():
    codes,vals=parse(fn)
    cold=[v for v in vals if v>=0.5]
    out[k]={"n":len(vals),"codes_200":codes.count("200"),"non200":[c for c in codes if c!="200"],
            "cold":len(cold),"p50":round(p50(vals),4) if vals else None,
            "max":round(max(vals),4) if vals else None,
            "cold_vals":[round(v,4) for v in cold]}
print(json.dumps(out,ensure_ascii=False,indent=1))
total_cold = out["381A"]["cold"]+out["381B"]["cold"]+out["381C"]["cold"]
print("SEARCH_COLD_TOTAL = %d/60 ~%.1f%%"%(total_cold,total_cold*100/60))
print("LAND_COLD = %d/20"%out["land"]["cold"])