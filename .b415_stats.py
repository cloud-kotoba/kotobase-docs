#!/usr/bin/env python3
# stats for K-Z3 run415: per-file cold count (>=0.5s), p50 (nearest-rank), max.
import math, json

def parse(fn):
    vals=[]; codes=[]
    for line in open(fn):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        codes.append(parts[0]); vals.append(float(parts[1]))
    return codes, vals

def p50(vals):
    s=sorted(vals); n=len(s)
    if n==0: return None
    return s[math.ceil(0.50*n)-1]

files = {
  "415A":".b415_415A.txt",
  "415B":".b415_415B.txt",
  "415C":".b415_415C.txt",
  "land":".b415_land.txt",
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
total_cold = out["415A"]["cold"]+out["415B"]["cold"]+out["415C"]["cold"]
print("SEARCH_COLD_TOTAL = %d/60 ~%.1f%%"%(total_cold,total_cold*100/60))
print("LAND_COLD = %d/20"%out["land"]["cold"])